# -*- coding: utf-8 -*-
'''
Created on 2016年4月27日

@author: 周茂恩
'''

# link1: http://blog.javachen.com/2014/06/08/using-scrapy-to-cralw-zhihu.html
import urlparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest, Request
from datetime import datetime
from scrapy.linkextractors import LinkExtractor

from zhihu.settings import HEADER, COOKIES
from zhihu.items import *

host = 'http://www.zhihu.com'

class ZhihuUserSpider(CrawlSpider):
    name = "zhihu_user"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        'https://www.zhihu.com/people/raymond-wang/about',
        'https://www.zhihu.com/people/Neal-Vermillion/about',
        'https://www.zhihu.com/people/abigail-z/about',
        'https://www.zhihu.com/people/ben-cao-gang-mu-72/about',
        'https://www.zhihu.com/people/raymond-wang/asks',
        'https://www.zhihu.com/people/Neal-Vermillion/asks',
        'https://www.zhihu.com/people/abigail-z/asks',
        'https://www.zhihu.com/people/ben-cao-gang-mu-72/asks',
        'https://www.zhihu.com/people/ben-cao-gang-mu-72/answers',
        'https://www.zhihu.com/people/Neal-Vermillion/answers',
        'https://www.zhihu.com/people/abigail-z/answers',
    ]

    
    rules = [
        Rule(LinkExtractor(allow=(".*")), callback='parse_test', follow=True),
        Rule(LinkExtractor(allow=("/people/.*/asks")), callback='parse_asks', follow=True),
        Rule(LinkExtractor(allow=("/people/.*/about")), callback='parse_about', follow=True),
        Rule(LinkExtractor(allow=("/people/.*/followees")), callback='parse_followees', follow=True),
        Rule(LinkExtractor(allow=("/people/.*/followers")), callback='parse_followers', follow=True),
        Rule(LinkExtractor(allow=("/people/.*/answers")), callback='parse_answers', follow=True),
    ]
    
    
    def __init__(self,  *a,  **kwargs):
        super(ZhihuUserSpider, self).__init__(*a, **kwargs)
        self.user_names = []
        self.headers = HEADER
        self.cookies = COOKIES


    def make_requests_from_url(self, url):
        print 'make_requests_from_url'
        return FormRequest(url,headers = self.headers, cookies = self.cookies, dont_filter=True)
     
    def parse_test(self, response):
        print 'parse_test', response
# #         return scrapy.FormRequest(response.url,
# #                     headers = self.headers, 
# #                     cookies = self.cookies,
# #                     callback=self.parse_other_zhihu)
#         
#     def parse_other_test(self, response):
#         print 'parse_other_test', response.url

        
    def parse_asks(self, response, sel):
        print 'parse_asks', response.url
        items = []
        try:
            for record in sel.xpath('//div[@id="zh-profile-ask-list"]/div'):
                item = ZhihuAskItem()
                item['_id'] = response.url
                item['username'] = response.url.split('/')[-2]
                item['view_num'] = record.xpath('//span/div[1]/text()')[0].extract()
                item['title'] = record.xpath('//div/h2/a/text()')[0].extract()
                item['answer_num'] = record.xpath('//div/div/span[1]/following-sibling::text()')[0].extract().split(' ')[0].replace('\n','').strip() #取数字
                item['follower_num'] = record.xpath('//div/div/span[2]/following-sibling::text()')[0].extract().split(' ')[0].replace('\n','').strip() #取数字
                item['url'] = host+record.xpath('//div/h2/a/@href')[0].extract()
                 
                items.append(item)
            return items
         
        except Exception, e:
            open('error_pages/asks' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e)

 
    def parse_about(self, response, sel):
        print 'parse_about', response.url
        typeinfo = response.url.split('/')[-1]
        print typeinfo
         
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
 
        except Exception, e:
            open('error_pages/about_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e) 
    
     
    def parse_followees(self, response, sel):
        print 'parse_followees', response.url
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

     
    def parse_followers(self, response, sel):
        print 'parse_followers', response.url
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
 
 
    def parse_answers(self, response, sel):
        print 'parse_answers', response.url
        items = []
        try:
            for record in sel.xpath('//div[@id="zh-profile-answer-list"]/div'):
                item = ZhihuAnswerItem()

                item['_id'] = response.url
                item['username'] = response.url.split('/')[-2]
                item['ask_title'] = ''.join(record.xpath('//h2/a/text()').extract())
                url = host + ''.join(record.xpath('//h2/a/@href').extract()) # answer_url
                item['ask_url'] = url.split('//answer')[0]
                item['agree_num'] = ''.join(record.xpath('//div/div[2]/a/text()').extract())
                item['summary'] = ''.join(record.xpath('//div/div[4]/div/text()').extract()).replace('\n','').strip()
                item['content'] = ''.join(record.xpath('//div/div[4]/textarea/text()').extract()).replace('\n','').strip()
 
                comment_num = record.xpath('//div/div[5]/div/a[2]/text()')[1].extract() #'添加评论'或者'3 条评论'
                comment_num = comment_num.split(' ')[0] #取数字
                if comment_num.startswith(u'添加评论'):
                    comment_num = '0'
                item['comment_num'] = comment_num 
            items.append(item)
            
        except Exception, e:
            open('error_pages/answers_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e)

