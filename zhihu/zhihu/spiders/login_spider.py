# -*- coding: utf-8 -*-
'''
Created on 2016年4月27日
@author: 周茂恩
'''

from scrapy.spiders.crawl import CrawlSpider
from scrapy.http.request.form import FormRequest

from zhihu.settings import HEADER, COOKIES

host = 'http://www.zhihu.com'
home = 'http://www.zhihu.com/people/raymond-wang/about'

class ZhihuLoginSpider(CrawlSpider):
    name = 'zhihu_login'
    allowed_domains = ['zhihu.com']
    start_urls = [home]
    
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
        print response.url
        if "Raymond Wang" in response.body:
            print 'successs'
        else:
            print 'fail'
    