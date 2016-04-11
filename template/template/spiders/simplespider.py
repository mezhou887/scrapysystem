# -*- coding: utf-8 -*-
import scrapy

from template.items import *    #这个错误是eclipse自己的编译器错误
from misc.log import log
from scrapy.selector import Selector

# 范例1，使用最基本的Spider来完成,以meizitu为模板来完成的
# 1. 从主页得到所有列表页的首页链接
# 2. 根据列表页的首页链接去得到下一页的链接，递归的遍历完整个列表页
# 3. 在每个列表页中找到内容页的链接，然后去访问具体的内容页
class templateSpider(scrapy.Spider):
    name = "template_v1"
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]

    def parse(self, response):
        log.info('start page: ', response.url)
        sel = Selector(response)
        for link in sel.xpath('//div[@class="tags"]/span/a/@href').extract(): # 找到列表页的首页链接
            request = scrapy.Request(link, callback=self.parse_list)
            yield request
        
    def parse_list(self, response):
        log.info('list page: '  + response.url)
        sel = Selector(response)
        for link in sel.xpath('//div[@class="inWrap"]/ul/li/div/div/a/@href').extract(): # 找到具体的内容页链接
            request = scrapy.Request(link, callback=self.parse_detail)
            yield request
        
        for link in sel.xpath('//div[@class="navigation"]/div[@id="wp_page_numbers"]/ul/li/a[contains(text(), "下一页")]/@href').extract(): # 找到列表页的下一页链接
            request = scrapy.Request(link, callback=self.parse_list)
            yield request                
        
        
    def parse_detail(self, response):
        log.info('content page: '  + response.url);  
        item = templateItem()
        item['pagelink'] = response.url
        item['title'] = response.xpath('//title/text()').extract()
        return item          

