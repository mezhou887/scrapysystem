# -*- coding: utf-8 -*-
'''
Created on 2016年4月27日

@author: 周茂恩
'''
from scrapy.selector import Selector
from scrapy.spiders.crawl import CrawlSpider
from scrapy.http.request.form import FormRequest

from zhihu.settings import HEADER, COOKIES

class ZhihuUserSpider(CrawlSpider):
    name = 'zhihu_user'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://www.zhihu.com/people/raymond-wang/about']
    
    def __init__(self):
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
        print response.url
        print response.body
    