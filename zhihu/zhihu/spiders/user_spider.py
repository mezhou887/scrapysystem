# -*- coding: utf-8 -*-
'''
Created on 2016年4月27日

@author: 周茂恩
'''
# link1: http://blog.javachen.com/2014/06/08/using-scrapy-to-cralw-zhihu.html


from scrapy.selector import Selector
from scrapy.spiders.crawl import CrawlSpider
from scrapy.http import Request,FormRequest
from datetime import datetime
from urllib import urlencode

from zhihu.settings import HEADER, COOKIES
from zhihu.items import *

import json

host = 'http://www.zhihu.com'
home = 'http://www.zhihu.com/people/raymond-wang/about'

class ZhihuUserSpider(CrawlSpider):
    name = 'zhihu_user'
    allowed_domains = ['zhihu.com']
    start_urls = [home]
    
    def __init__(self):
        self.user_names = []
        self.headers = HEADER
        self.cookies = COOKIES
    
    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield FormRequest(url, meta = {'cookiejar': i},
                headers = self.headers,
                cookies = self.cookies,
                callback = self.parse_item)
    
    def parse_about(self, response, sel):
        try:
            user = ZhihuUserItem()
            user['_id']=user['username']=response.url.split('/')[-2]
            user['url']= response.url
            user['nickname'] = ''.join(sel.xpath("//div[@class='title-section ellipsis']/a[@class='name']/text()").extract())
            user['location'] = ''.join(sel.xpath("//span[@class='location item']/@title").extract())
            user['industry'] = ''.join(sel.xpath("//span[@class='business item']/@title").extract())
            user['sex'] = ''.join(sel.xpath('//div[@class="item editable-group"]/span/span[@class="item"]/i/@class').extract()).replace("zg-icon gender ","")
            user['description'] = ''.join(sel.xpath("//span[@class='description unfold-item']/span/text()").extract()).strip().replace("\n",'')
            user['view_num'] = ''.join(sel.xpath("//span[@class='zg-gray-normal']/strong/text()").extract())
            user['update_time'] = str(datetime.now())

            user['jobs'] = []
            job_nodes = sel.xpath('//div[@class="zm-profile-module zg-clear"][1]/div/ul[@class="zm-profile-details-items"]/li')
            for node in job_nodes:
                company = ''.join(node.xpath('@data-title').extract())
                title = ''.join(node.xpath('@data-sub-title').extract())
                user['jobs'].append({'company': company, 'title':title})

            user['educations'] = []
            edu_nodes = sel.xpath('//div[@class="zm-profile-module zg-clear"][3]/div/ul[@class="zm-profile-details-items"]/li')
            for node in edu_nodes:
                school = ''.join(node.xpath('@data-title').extract())
                major = ''.join(node.xpath('@data-sub-title').extract())
                user['educations'].append({'school':school, 'major':major})

            for node in sel.xpath("//a[@class='zm-profile-header-user-weibo']/@href").extract():
                if node.startswith('http://weibo.com'):
                    user['sinaweibo'] = node
                elif node.startswith('http://t.qq.com'):
                    user['tencentweibo'] = node

            statistics = sel.xpath("//a[@class='item']/strong/text()").extract()
            followee_num =user['followee_num'] = statistics[0]
            follower_num = user['follower_num']= statistics[1]

            statistics = sel.xpath("//div[@class='zm-profile-module-desc']/span/strong/text()").extract()
            if len(statistics) ==4:
                user['agree_num'] = statistics[0]
                user['thank_num'] = statistics[1]
                user['fav_num'] = statistics[2]
                user['share_num'] = statistics[3]

            statistics = sel.xpath("//div[@class='profile-navbar clearfix']/a/span/text()").extract()
            if len(statistics) ==6:
                user['ask_num'] = statistics[1]
                user['answer_num'] = statistics[2]
                user['post_num'] = statistics[3]
                user['collection_num'] = statistics[4]
                user['log_num'] = statistics[5]

            _xsrf=''.join(sel.xpath('//input[@name="_xsrf"]/@value').extract())
            hash_id=''.join(sel.xpath('//div[@class="zm-profile-header-op-btns clearfix"]/button/@data-id').extract())

            print 'NEW:%s' % user['username']

            yield user
            self.user_names.append(user['username'])
            print 'NEW:%s' % user['username']

            base_url = '/'.join(response.url.split('/')[:-1])
            headers = self.headers
            headers['Referer'] = response.url

            # followees
            num = int(followee_num) if followee_num else 0
            page_num = num/20
            page_num += 1 if num%20 else 0

            for i in xrange(page_num):
                params = json.dumps({"hash_id":hash_id,"order_by":"created","offset":i*20})
                payload = {"method":"next", "params": params, "_xsrf":_xsrf,"username":user['username']}
                yield Request("http://www.zhihu.com/node/ProfileFolloweesListV2?"+urlencode(payload), headers = headers, cookies = self.cookies)

            # followers
            num = int(follower_num) if follower_num else 0
            page_num = num/20
            page_num += 1 if num%20 else 0

            for i in xrange(page_num):
                params = json.dumps({"hash_id":hash_id,"order_by":"created","offset":i*20})
                payload = {"method":"next", "params": params, "_xsrf":_xsrf,"username":user['username']}
                yield Request("http://www.zhihu.com/node/ProfileFollowersListV2?"+urlencode(payload), headers = headers, cookies = self.cookies)

            # questions
            num = int(user['ask_num']) if user['ask_num'] else 0
            page_num = num/20
            page_num += 1 if num%20 else 0
            for i in xrange(page_num):
                if i > 0:
                    headers['Referer'] = base_url + '/asks?page=%d' % (i-1)
                else:
                    headers['Referer'] = base_url + '/asks'
                yield Request(base_url + '/asks?page=%d' % (i+1), headers = headers, cookies = self.cookies)

            # answers
            num = int(user['answer_num']) if user['answer_num'] else 0
            page_num = num/20
            page_num += 1 if num%20 else 0
            for i in xrange(page_num):
                if i > 0:
                    headers['Referer'] = base_url + '/answers?page=%d' % (i-1)
                else:
                    headers['Referer'] = base_url + '/answers'

                yield Request(base_url + '/answers?page=%d' % (i+1), headers = headers, cookies = self.cookies)
                
        except Exception, e:
            open('error_pages/about_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e) 
        
    def parse_followees(self, response, sel):
        followees = []
        try:
            links = sel.xpath('//div[@class="zm-list-content-medium"]/h2/a/@href').extract()

            for link in links:
                username_tmp = link.split('/')[-1]
                followees.append(username_tmp)
                if username_tmp in self.user_names:
                    print 'GET:' + '%s' % username_tmp
                    continue

                headers = self.headers;
                headers['Referer'] = response.url
                yield Request(link+'/about', headers = headers, cookies=self.cookies)

            username=urlparse.parse_qs(urlparse.urlparse(response.url).query,True)['username'][0]
            yield ZhihuFolloweesItem(_id=username,username = username,followees = followees)
        except Exception, e:
            open('error_pages/followees_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e)
            
    def parse_followers(self, response, sel):
        followers = []
        try:
            links = sel.xpath('//div[@class="zm-list-content-medium"]/h2/a/@href').extract()

            for link in links:
                username_tmp = link.split('/')[-1]
                followers.append(username_tmp)
                if username_tmp in self.user_names:
                    print 'GET:' + '%s' % username_tmp
                    continue

                headers = self.headers;
                headers['Referer'] = response.url
                yield Request(link+'/about', headers = headers, cookies=self.cookies)

            username = response.url.split('/')[-2]
            # 保存到文件时，没有合并
            #yield ZhihuFollowersItem(_id=username,username = username,followers = followers)
        except Exception, e:
            open('error_pages/followers_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e)
        
    def parse_answers(self, response, sel):
        username = response.url.split('/')[-2]
        try:
            for record in sel.xpath(r"id('zh-profile-answer-list')/div"):
                ask_title = ''.join(record.xpath(r"h2/a/text()").extract())
                url = host + ''.join(record.xpath("h2/a/@href").extract()) # answer_url
                ask_url = url.split('/answer')[0]

                agree_num = ''.join(record.xpath('div/div[2]/a/text()').extract())
                summary = ''.join(record.xpath(r"div/div[4]/div/text()").extract()).replace("\n","").strip()  #TODO
                content = ''.join(record.xpath(r"div/div[4]/textarea/text()").extract()).replace("\n","").strip()

                comment_num = record.xpath(r"div/div[5]/div/a[2]/text()")[1].extract() #'添加评论'或者'3 条评论'
                comment_num = comment_num.split(' ')[0] #取数字
                if comment_num.startswith(u'添加评论'):
                    comment_num = '0'

                yield ZhihuAnswerItem(_id=url,username = username,url = url, ask_title = ask_title, \
                                      ask_url = ask_url, agree_num = agree_num, summary = summary
                                      , content = content, comment_num = comment_num)
        except Exception, e:
            open('error_pages/answers_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e)
        
    def parse_asks(self, response, sel):
        username = response.url.split('/')[-2]
        try:
            for record in sel.xpath(r"id('zh-profile-ask-list')/div"):
                view_num = record.xpath(r'span/div[1]/text()')[0].extract()
                title = record.xpath(r"div/h2/a/text()")[0].extract()
                answer_num = record.xpath(r"div/div/span[1]/following-sibling::text()")[0].extract().split(' ')[0].replace('\n','')
                follower_num = record.xpath(r"div/div/span[2]/following-sibling::text()")[0].extract().split(' ')[0].replace('\n','')
                url = host+record.xpath(r"div/h2/a/@href")[0].extract()

                yield ZhihuAskItem(_id=url,username = username,url = url, view_num = view_num, title = title, answer_num = answer_num, follower_num = follower_num)
        except Exception, e:
            open('error_pages/asks' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e)

        
    def parse_item(self, response):
        sel = Selector(response)
        typeinfo = response.url.split('/')[-1]
         
        if typeinfo.startswith('about'):
            self.parse_about(response, sel)
        
        elif typeinfo.startswith('followees') or typeinfo.startswith('ProfileFolloweesListV2'):
            self.parse_followees(response, sel)

        elif typeinfo.startswith('followers') or typeinfo.startswith('ProfileFollowersListV2'):
            self.parse_followers(response, sel)
            
        elif typeinfo.startswith('answers'):
            self.parse_answers(response, sel)
            
        elif typeinfo.startswith('asks'):
            self.parse_asks(response, sel)
