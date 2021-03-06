# -*- coding: utf-8 -*-
import scrapy
import logging

from xxxiao.items import xxxiaoItem    #这个错误是eclipse自己的编译器错误
from xxxiao.config import xxxiaoConfig #这个错误是eclipse自己的编译器错误
from scrapy.selector import Selector

# 范例1，使用最基本的Spider来完成
# 1. 从主页得到所有列表页的首页链接
# 2. 根据列表页的首页链接去得到下一页的链接，递归的遍历完整个列表页
# 3. 在每个列表页中找到内容页的链接，然后去访问具体的内容页
class XxxiaoSpider(scrapy.Spider):
    
    name = "xxxiao_base"
    allowed_domains = ["m.xxxiao.com"]
    start_urls = [
        "http://m.xxxiao.com/",
    ]

    def parse(self, response):
        sel = Selector(response)
        for link in sel.xpath(xxxiaoConfig.list_page_rule2).extract(): # 找到列表页的首页链接 
            request = scrapy.Request(link, callback=self.parse_list)
            yield request

        
    def parse_list(self, response):
        logging.info('list page: %s', response.url)
        sel = Selector(response)
        for link in sel.xpath(xxxiaoConfig.detail_page_rule1).extract(): # 找到具体的内容页链接
            yield scrapy.Request(link, callback=self.parse_detail)
        
        for link in sel.xpath(xxxiaoConfig.list_page_rule1).extract(): # 找到列表页的下一页链接
            yield scrapy.Request(link, callback=self.parse_list)                

           
    def parse_detail(self, response):
        logging.debug('content page: %s', response.url);  
        item = xxxiaoItem()
        item['pagelink'] = response.url
        item['title'] = response.xpath('//title/text()').extract()
        item['image_urls'] = response.xpath(xxxiaoConfig.detail_page_rule2).extract()
#         item['file_urls'] = response.xpath(xxxiaoConfig.detail_page_rule2).extract()
        return item   