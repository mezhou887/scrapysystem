# -*- coding: utf-8 -*-
'''
Created on 2016年4月27日

@author: 周茂恩
'''
# link1: http://blog.javachen.com/2014/06/08/using-scrapy-to-cralw-zhihu.html

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest
from scrapy.linkextractors import LinkExtractor

from zhihu.settings import HEADER, COOKIES
from zhihu.items import *

host = 'http://www.zhihu.com'

class ZhihuUserSpider(CrawlSpider):
    name = 'zhihu_user_test'
    allowed_domains = ['zhihu.com']
    start_urls = [
                'https://www.zhihu.com/people/zhoumaoen',
                  ]
    
    def __init__(self,  *a,  **kwargs):
        super(ZhihuUserSpider, self).__init__(*a, **kwargs)
        self.user_names = []
        self.headers = HEADER
        self.cookies = COOKIES
        
    def start_requests(self):
        for url in self.start_urls:
            yield FormRequest(url,
                headers = self.headers,
                cookies = self.cookies,
                callback = self.parse_item)        
    
    rules = [
        Rule(LinkExtractor(allow=("/people/.*/asks")), callback='parse_asks', process_request='add_cookie', follow=True),
        Rule(LinkExtractor(allow=("/people/.*/about")), callback='parse_about', process_request='add_cookie', follow=True),
        Rule(LinkExtractor(allow=("/people/.*/followees")), callback='parse_followees', process_request='add_cookie', follow=True),
        Rule(LinkExtractor(allow=("/people/.*/followers")), callback='parse_followers', process_request='add_cookie', follow=True),
        Rule(LinkExtractor(allow=("/people/.*/answers")), callback='parse_answers', process_request='add_cookie', follow=True),
    ]
    
    def add_cookie(self, request):
        request.replace(cookies=self.cookies);
        return request;        

    def parse_item(self, response):
        sel = Selector(response)
        print 'parse_item', response.url, sel
        print response.body

    def parse_asks(self, response, sel):
        print 'parse_asks', response.url

 
    def parse_about(self, response, sel):
        print 'parse_about', response.url
    
     
    def parse_followees(self, response, sel):
        print 'parse_followees', response.url

     
    def parse_followers(self, response, sel):
        print 'parse_followers', response.url
 
 
    def parse_answers(self, response, sel):
        print 'parse_answers', response.url
