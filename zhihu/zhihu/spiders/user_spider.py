# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from scrapy.http import FormRequest, Request
from datetime import datetime

from zhihu.settings import HEADER, COOKIES
from zhihu.items import *

host = 'http://www.zhihu.com'

class ZhihuUserSpider(CrawlSpider):
   
    name = "zhihu_user"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        'https://www.zhihu.com/people/raymond-wang',
    ]

    def __init__(self,  *a,  **kwargs):
        super(ZhihuUserSpider, self).__init__(*a, **kwargs)
        self.user_names = []
        self.headers = HEADER
        self.cookies = COOKIES
        
    def start_requests(self):
        for url in self.start_urls:
            yield FormRequest(url, headers = self.headers,
                cookies = self.cookies, callback = self.parse_zhihu)           

    # 处理的是个人主页
    def parse_zhihu(self, response):
        print 'parse_zhihu', response.url
        sel = Selector(response)
        
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
            if len(statistics) == 6:
                user['ask_num'] = statistics[1]             # 提问
                user['answer_num'] = statistics[2]          # 回答
                user['post_num'] = statistics[3]            # 文章
                user['collection_num'] = statistics[4]      # 收藏
                user['log_num'] = statistics[5]             # 公共编辑

            ## 详细资料
            # 个人成就
            statistics = sel.xpath('//div[@class="zm-profile-module-desc"]/span/strong/text()').extract()
            if len(statistics) == 4:
                user['agree_num'] = statistics[0]           # 赞同
                user['thank_num'] = statistics[1]           # 感谢
                user['fav_num'] = statistics[2]             # 收藏
                user['share_num'] = statistics[3]           # 分享
             
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
            user['followee_num'] = statistics[0]        # 关注了的数量
            user['follower_num']= statistics[1]         # 关注者的数量
 
            yield user
            self.user_names.append(user['username'])    # 这个以后要保存到数据库中
 
            headers = self.headers;
            headers['Referer'] = response.url
            
            ## 以下链接
            followees_link = host+sel.xpath('//div[@class="zu-main-sidebar"]/div/a/@href').extract()[0]
            followers_link = host+sel.xpath('//div[@class="zu-main-sidebar"]/div/a/@href').extract()[1]
#             asks_link = host+sel.xpath('//div[@class="profile-navbar clearfix"]/a/@href').extract()[1]
#             answers_link = host+sel.xpath('//div[@class="profile-navbar clearfix"]/a/@href').extract()[2]

            yield scrapy.FormRequest(followees_link, headers = headers, cookies=self.cookies, callback=self.parse_followees)
            yield scrapy.FormRequest(followers_link, headers = headers, cookies=self.cookies, callback=self.parse_followers)
#             yield scrapy.FormRequest(asks_link, headers = headers, cookies=self.cookies, callback=self.parse_asks)
#             yield scrapy.FormRequest(answers_link, headers = headers, cookies=self.cookies, callback=self.parse_answers)
 
        except Exception, e:
            open('error_pages/about_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e)         


    def parse_followees(self, response):
        print 'parse_followees', response.url
        sel = Selector(response)

        followees = []
        followee = ZhihuFolloweesItem()
        followee['_id'] = followee['username'] = response.url.split('/')[-2]
        try:
            links = sel.xpath('//div[@class="zm-list-content-medium"]/h2/a/@href').extract()
 
            for link in links:
                username_tmp = link.split('/')[-1]
                followees.append(username_tmp)
            followee['followees'] = followees
            yield followee

            for link in links:
                username_tmp = link.split('/')[-1]
                if username_tmp in self.user_names:
                    print 'Already Get:' + '%s' % username_tmp
                    continue
 
                headers = self.headers;
                headers['Referer'] = response.url
                yield Request(link, headers = headers, cookies=self.cookies, callback=self.parse_zhihu)
                
 
        except Exception, e:
            open('error_pages/followees_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e)
                 
                            
    def parse_followers(self, response):
        print 'parse_followers', response.url
        sel = Selector(response)
        
        followers = []
        follower = ZhihuFollowersItem()
        follower['_id'] = follower['username'] = response.url.split('/')[-2]
        try:
            links = sel.xpath('//div[@class="zm-list-content-medium"]/h2/a/@href').extract()
  
            for link in links:
                username_tmp = link.split('/')[-1]
                followers.append(username_tmp)
            follower['followers'] = followers
            yield follower

            for link in links:
                username_tmp = link.split('/')[-1]
                if username_tmp in self.user_names:
                    print 'Already Get:' + '%s' % username_tmp
                    continue
  
                headers = self.headers;
                headers['Referer'] = response.url
                yield Request(link, headers = headers, cookies=self.cookies, callback=self.parse_zhihu)
  
        except Exception, e:
            open('error_pages/followers_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e)

    
#     def parse_asks(self, response):
#         print 'parse_asks', response.url
#         sel = Selector(response)
#         items = []
#         try:
#             for record in sel.xpath('//div[@id="zh-profile-ask-list"]/div'):
#                 item = ZhihuAskItem()
#                 item['_id'] = response.url
#                 item['username'] = response.url.split('/')[-2]
#                 item['view_num'] = record.xpath('//span/div[1]/text()')[0].extract()
#                 item['title'] = record.xpath('//div/h2/a/text()')[0].extract()
#                 item['answer_num'] = record.xpath('//div/div/span[1]/following-sibling::text()')[0].extract().split(' ')[0].replace('\n','').strip() #取数字
#                 item['follower_num'] = record.xpath('//div/div/span[2]/following-sibling::text()')[0].extract().split(' ')[0].replace('\n','').strip() #取数字
#                 item['url'] = host+record.xpath('//div/h2/a/@href')[0].extract()
#                   
#                 items.append(item)
#             yield items
#           
#         except Exception, e:
#             open('error_pages/asks' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
#             print '='*10 + str(e)
#   
#   
#     def parse_answers(self, response, sel):
#         print 'parse_answers', response.url
#         items = []
#         try:
#             for record in sel.xpath('//div[@id="zh-profile-answer-list"]/div'):
#                 item = ZhihuAnswerItem()
#  
#                 item['_id'] = response.url
#                 item['username'] = response.url.split('/')[-2]
#                 item['ask_title'] = ''.join(record.xpath('//h2/a/text()').extract())
#                 url = host + ''.join(record.xpath('//h2/a/@href').extract())
#                 item['ask_url'] = url.split('//answer')[0]
#                 item['agree_num'] = ''.join(record.xpath('//div/div[2]/a/text()').extract())
#                 item['summary'] = ''.join(record.xpath('//div/div[4]/div/text()').extract()).replace('\n','').strip()
#                 item['content'] = ''.join(record.xpath('//div/div[4]/textarea/text()').extract()).replace('\n','').strip()
#   
#                 comment_num = record.xpath('//div/div[5]/div/a[2]/text()')[1].extract() #'添加评论'或者'3 条评论'
#                 comment_num = comment_num.split(' ')[0] #取数字
#                 if comment_num.startswith(u'添加评论'):
#                     comment_num = '0'
#                 item['comment_num'] = comment_num 
#                 
#                 items.append(item)
#             yield items
#              
#         except Exception, e:
#             open('error_pages/answers_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
#             print '='*10 + str(e)
