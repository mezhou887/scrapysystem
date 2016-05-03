# -*- coding: utf-8 -*-
'''
Created on 2016年4月27日

@author: 周茂恩
'''

# link1: http://blog.javachen.com/2014/06/08/using-scrapy-to-cralw-zhihu.html
import urlparse
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest, Request
from datetime import datetime
from scrapy.linkextractors import LinkExtractor

from zhihu.settings import HEADER, COOKIES
from zhihu.items import *
from scrapy.item import Item
from twisted.cred.credentials import UsernameHashedPassword


class ZhihuUserSpider(CrawlSpider):
   
    name = "zhihu_user"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        'http://www.zhihu.com/people/raymond-wang/asks',
        'http://www.zhihu.com/people/Neal-Vermillion/asks',
        'http://www.zhihu.com/people/abigail-z/asks',
        'http://www.zhihu.com/people/ben-cao-gang-mu-72/asks',
        'https://www.zhihu.com/people/ben-cao-gang-mu-72/answers',
        'http://www.zhihu.com/people/Neal-Vermillion/answers',
        'http://www.zhihu.com/people/abigail-z/answers',
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

    def parse_zhihu(self, response):
        print 'parse_zhihu', response.url
        sel = Selector(response)
        typeinfo = response.url.split('/')[-1]
         
        if typeinfo == 'followees':
            self.parse_followees(response, sel)

        elif typeinfo == 'followers':
            self.parse_followers(response, sel)
            
        elif typeinfo == 'answers':
            self.parse_answers(response, sel)
            
        elif typeinfo == 'asks':
            self.parse_asks(response, sel)  
        else:
            print 'typeinfo is: %s', typeinfo
         
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
            
            item = ZhihuFolloweesItem()
            item['_id'] = item['username'] = username
            item['followees'] = followees
            return item 
            
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
            item = ZhihuFollowersItem()
            item['_id'] = item['username'] = username
            item['followers'] = followers
            return item 

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

