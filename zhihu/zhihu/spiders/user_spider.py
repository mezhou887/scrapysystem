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
import urlparse

host = 'http://www.zhihu.com'

class ZhihuUserSpider(CrawlSpider):
    name = 'zhihu_user'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://www.zhihu.com/people/raymond-wang/about',
                  'https://www.zhihu.com/people/Neal-Vermillion/about',
                  'https://www.zhihu.com/people/abigail-z/about',]
    
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

    def parse_item(self, response):
        sel = Selector(response)
        typeinfo = response.url.split('/')[-1]
         
        if typeinfo.startswith('about'):
            try:
                user = ZhihuUserItem()
                
                ## 通用参数
                user['_id']=user['username']=response.url.split('/')[-2]
                user['url']= response.url
                _xsrf=''.join(sel.xpath('//input[@name="_xsrf"]/@value').extract())
                hash_id=''.join(sel.xpath('//div[@class="zm-profile-header-op-btns clearfix"]/button/@data-id').extract())
                
                ## 基本信息
                user['nickname'] = ''.join(sel.xpath('//div[@class="title-section ellipsis"]/a[@class="name"]/text()').extract())                   # 姓名
                user['location'] = ''.join(sel.xpath('//span[@class="location item"]/a/text()').extract())                                          # 地址
                user['industry'] = ''.join(sel.xpath('//span[@class="business item"]/a/text()').extract())                                          # 产业
                user['sex'] = ''.join(sel.xpath('//span[@class="item gender"]/i/@class').extract())                                                 # 性别
                user['description'] = ''.join(sel.xpath('//span[@class="description unfold-item"]/span/text()').extract()).strip().replace("\n",'') # 描述信息
                user['view_num'] = ''.join(sel.xpath('//span[@class="zg-gray-normal"]/strong/text()').extract())                                    # 浏览次数
                user['update_time'] = str(datetime.now())
                
                statistics = sel.xpath('//div[@class="profile-navbar clearfix"]/a/span/text()').extract()
                if len(statistics) ==6:
                    user['ask_num'] = statistics[1]             # 提问
                    user['answer_num'] = statistics[2]          # 回答
                    user['post_num'] = statistics[3]            # 文章
                    user['collection_num'] = statistics[4]      # 收藏
                    user['log_num'] = statistics[5]             # 公共编辑
                    

                ## 详细资料
                # 个人成就
                statistics = sel.xpath('//div[@class="zm-profile-module-desc"]/span/strong/text()').extract()
                if len(statistics) ==4:
                    user['agree_num'] = statistics[0] # 赞同
                    user['thank_num'] = statistics[1] # 感谢
                    user['fav_num'] = statistics[2]   # 收藏
                    user['share_num'] = statistics[3] # 分享
                
                # 职业经历
                user['jobs'] = []
                job_nodes = sel.xpath('//div[@class="zm-profile-module zg-clear"][1]/div')
                for node in job_nodes:
                    company = '/'.join(node.xpath('//div[@class="ProfileItem-text ProfileItem-text--bold"]/a/text()').extract())
                    title = ''.join(node.xpath('//div[@class="ProfileItem-text ProfileItem-text--bold"]/span[2]/text()').extract())
                    user['jobs'].append({'company': company, 'title':title})
                    
                # 居住信息    
                user['locations'] = []
                location_nodes = sel.xpath('//div[@class="zm-profile-module zg-clear"][2]/div')
                for node in location_nodes:
                    local = '/'.join(node.xpath('//div[@class="ProfileItem-text ProfileItem-text--bold"]/a/text()').extract())
                    user['locations'].append({'local': local})
    
                # 教育经历
                user['educations'] = []
                edu_nodes = sel.xpath('//div[@class="zm-profile-module zg-clear"][3]/div')
                for node in edu_nodes:
                    school = ''.join(node.xpath('@data-title').extract())
                    major = ''.join(node.xpath('@data-sub-title').extract())
                    user['educations'].append({'school':school, 'major':major})
    
    
                ## 关注了和关注者
                statistics = sel.xpath('//a[@class="item"]/strong/text()').extract()
                followee_num =user['followee_num'] = statistics[0] # 关注了的数量
                follower_num = user['follower_num']= statistics[1] # 关注者的数量
    
                yield user
                self.user_names.append(user['username'])
    
                base_url = '/'.join(response.url.split('/')[:-1])
                headers = self.headers
                headers['Referer'] = response.url
    
                '''
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
                '''
                    
            except Exception, e:
                open('error_pages/about_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
                print '='*10 + str(e) 
        
        elif typeinfo.startswith('followees'):
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
                yield ZhihuFolloweesItem(_id=username, username=username, followees=followees)
            except Exception, e:
                open('error_pages/followees_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
                print '='*10 + str(e)

        elif typeinfo.startswith('followers'):
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
                yield ZhihuFollowersItem(_id=username, username=username, followers=followers)
            except Exception, e:
                open('error_pages/followers_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
                print '='*10 + str(e)
            
        elif typeinfo.startswith('answers'):
            username = response.url.split('/')[-2]
            try:
                for record in sel.xpath('//div[@id="zh-profile-answer-list"]/div'):
                    
                    ask_title = ''.join(record.xpath('/h2/a/text()').extract())
                    url = host + ''.join(record.xpath('/h2/a/@href').extract()) # answer_url
                    ask_url = url.split('/answer')[0]
    
                    agree_num = ''.join(record.xpath('/div/div[2]/a/text()').extract())
                    summary = ''.join(record.xpath('/div/div[4]/div/text()').extract()).replace('\n','').strip()
                    content = ''.join(record.xpath('/div/div[4]/textarea/text()').extract()).replace('\n','').strip()
    
                    comment_num = record.xpath('/div/div[5]/div/a[2]/text()')[1].extract() #'添加评论'或者'3 条评论'
                    comment_num = comment_num.split(' ')[0] #取数字
                    if comment_num.startswith(u'添加评论'):
                        comment_num = '0'
    
                    yield ZhihuAnswerItem(_id=url,username = username,url = url, ask_title = ask_title, \
                                          ask_url = ask_url, agree_num = agree_num, summary = summary, \
                                          content = content, comment_num = comment_num)
            except Exception, e:
                open('error_pages/answers_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
                print '='*10 + str(e)
            
        elif typeinfo.startswith('asks'):
            username = response.url.split('/')[-2]
            try:
                for record in sel.xpath('//div[@id="zh-profile-ask-list"]/div'):
                    
                    view_num = record.xpath('/span/div[1]/text()')[0].extract()
                    title = record.xpath('/div/h2/a/text()')[0].extract()
                    answer_num = record.xpath('/div/div/span[1]/following-sibling::text()')[0].extract().split(' ')[0].replace('\n','').strip() #取数字
                    follower_num = record.xpath('/div/div/span[2]/following-sibling::text()')[0].extract().split(' ')[0].replace('\n','').strip() #取数字
                    url = host+record.xpath('/div/h2/a/@href')[0].extract()
    
                    yield ZhihuAskItem(_id=url,username = username,url = url, view_num = view_num, \
                                       title = title, answer_num = answer_num, follower_num = follower_num)
            except Exception, e:
                open('error_pages/asks' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
                print '='*10 + str(e)
            self.parse_asks(response, sel)
