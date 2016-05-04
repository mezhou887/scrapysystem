# -*- coding: utf-8 -*-
'''
Created on 2016年4月27日

@author: 周茂恩
'''

# link1: http://blog.javachen.com/2014/06/08/using-scrapy-to-cralw-zhihu.html
import urlparse
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
        
        # 得到followees的链接
        followees_link = sel.xpath('//div[@class="zu-main-sidebar"]/div/a/@href').extract()[0]
        headers = self.headers;
        headers['Referer'] = response.url
        yield scrapy.FormRequest(host+followees_link, headers = headers, cookies=self.cookies, callback=self.parse_followees)
        
        #得到followers的链接
        followers_link = sel.xpath('//div[@class="zu-main-sidebar"]/div/a/@href').extract()[1]
        headers = self.headers;
        headers['Referer'] = response.url
        yield scrapy.FormRequest(host+followers_link, headers = headers, cookies=self.cookies, callback=self.parse_followers)
                 
        #得到asks的链接
        asks_link = sel.xpath('//div[@class="profile-navbar clearfix"]/a/@href').extract()[1]
        headers = self.headers;
        headers['Referer'] = response.url
        yield scrapy.FormRequest(host+asks_link, headers = headers, cookies=self.cookies, callback=self.parse_asks)
        
        #得到answers的链接
        answers_link = sel.xpath('//div[@class="profile-navbar clearfix"]/a/@href').extract()[2]
        headers = self.headers;
        headers['Referer'] = response.url
        yield scrapy.FormRequest(host+answers_link, headers = headers, cookies=self.cookies, callback=self.parse_answers)

    def parse_followees(self, response):
        print 'parse_followees', response.url
        sel = Selector(response)
#         username=urlparse.parse_qs(urlparse.urlparse(response.url).query,True)['username'][0]

        followees = []
        item = ZhihuFolloweesItem()
        try:
            links = sel.xpath('//div[@class="zm-list-content-medium"]/h2/a/@href').extract()
 
            for link in links:
                username_tmp = link.split('/')[-1]
                followees.append(username_tmp)
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
#         username = response.url.split('/')[-2]
        
        followers = []
        item = ZhihuFollowersItem()
        try:
            links = sel.xpath('//div[@class="zm-list-content-medium"]/h2/a/@href').extract()
  
            for link in links:
                username_tmp = link.split('/')[-1]
                followers.append(username_tmp)
                if username_tmp in self.user_names:
                    print 'Already Get:' + '%s' % username_tmp
                    continue
  
                headers = self.headers;
                headers['Referer'] = response.url
                yield Request(link, headers = headers, cookies=self.cookies, callback=self.parse_zhihu)
  
        except Exception, e:
            open('error_pages/followers_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e)

    
    def parse_asks(self, response):
        print 'parse_asks', response.url
        sel = Selector(response)
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
  
  
    def parse_answers(self, response, sel):
        print 'parse_answers', response.url
        items = []
        try:
            for record in sel.xpath('//div[@id="zh-profile-answer-list"]/div'):
                item = ZhihuAnswerItem()
 
                item['_id'] = response.url
                item['username'] = response.url.split('/')[-2]
                item['ask_title'] = ''.join(record.xpath('//h2/a/text()').extract())
                url = host + ''.join(record.xpath('//h2/a/@href').extract())
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
