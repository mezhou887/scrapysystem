# -*- coding: utf-8 -*-
import scrapy
import logging
import pprint

from template.items import templateItem    #这个错误是eclipse自己的编译器错误
from template.config import templateConfig #这个错误是eclipse自己的编译器错误
from misc.xpathspider import BaseXpathSpider
from misc.log import pp
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisMixin
from bs4 import BeautifulSoup

# 范例1，使用最基本的Spider来完成
# 1. 从主页得到所有列表页的首页链接
# 2. 根据列表页的首页链接去得到下一页的链接，递归的遍历完整个列表页
# 3. 在每个列表页中找到内容页的链接，然后去访问具体的内容页
class templateSpider(scrapy.Spider):
    name = "template_base"
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]

    def parse(self, response):
        sel = Selector(response)
        for list_link in sel.xpath(templateConfig.list_page_rule1).extract(): # 找到列表页的首页链接
            request = scrapy.Request(list_link, callback=self.parse_list)
            yield request
        
    def parse_list(self, response):
        logging.info('list page: %s', response.url)
        sel = Selector(response)
        for detail_link in sel.xpath(templateConfig.detail_page_rule1).extract(): # 找到具体的内容页链接
            yield scrapy.Request(detail_link, callback=self.parse_detail)
        
        for list_link in sel.xpath(templateConfig.list_page_rule2).extract(): # 找到列表页的下一页链接
            yield scrapy.Request(list_link, callback=self.parse_list)                
           
    def parse_detail(self, response):
        logging.debug('content page: %s', response.url);  
        item = templateItem()
        item['pagelink'] = response.url
        item['title'] = response.xpath('//title/text()').extract()
        item['name'] = response.xpath('//h2/a/text()').extract()
        item['image_urls'] = response.xpath('//div[@id="picture"]/p/img/@src').extract()
#        item['file_urls'] = response.xpath('//div[@id="picture"]/p/img/@src').extract()
        return item   
    
    
# 范例2，在范例1的基础上用item_rules来指明存储的字段    
class templateXpathSpider(BaseXpathSpider):
    name = "template_xpath"
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]
    
    item_rules = { 
        '//title': {
            '__use': 'dump',                    
            'title': 'text()',
            '__link': 'pagelink'
        },
        '//body': {
            '__use': 'dump', 
            'name': '//h2/a/text()',
            'image_urls': '//div[@id="picture"]/p/img/@src',                           
#            'file_urls': '//div[@id="picture"]/p/img/@src'                             
        }             
    }
    
    def parse(self, response):
        sel = Selector(response)
        for list_link in sel.xpath(templateConfig.list_page_rule1).extract(): # 找到列表页的首页链接
            yield scrapy.Request(list_link, callback=self.parse_list)
        
    def parse_list(self, response):
        logging.info('list page: %s', response.url)
        sel = Selector(response)
        for detail_link in sel.xpath(templateConfig.detail_page_rule1).extract(): # 找到具体的内容页链接
            yield scrapy.Request(detail_link, callback=self.parse_detail)
        
        for list_link in sel.xpath(templateConfig.list_page_rule2).extract(): # 找到列表页的下一页链接
            yield scrapy.Request(list_link, callback=self.parse_list)
            
    def parse_detail(self, response):
        logging.debug('content page: %s', response.url);  
        item = self.parse_with_rules(response, self.item_rules, meizituItem)
        pp.pprint(item)
        return item
    

# 范例3，在范例2的基础上加入Redis      
class templateXpathRedisSpider(RedisMixin, BaseXpathSpider):
    name = "template_redis"
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]
    
    item_rules = { 
        '//title': {
            '__use': 'dump',                    
            'title': 'text()',
            '__link': 'pagelink'
        },
        '//body': {
            '__use': 'dump', 
            'name': '//h2/a/text()',
            'image_urls': '//div[@id="picture"]/p/img/@src',                             
#            'file_urls': '//div[@id="picture"]/p/img/@src'                             
        }             
    }         
        
    def _set_crawler(self, crawler):
        super(templateXpathRedisSpider, self)._set_crawler(crawler)
        self.setup_redis()            
        
    def parse(self, response):
        soup = BeautifulSoup(response.body, "lxml")
        logging.debug(soup.prettify())
        sel = Selector(response)
        for list_link in sel.xpath(templateConfig.list_page_rule1).extract(): # 找到列表页的首页链接
            yield scrapy.Request(list_link, callback=self.parse_list)
        
    def parse_list(self, response):
        logging.info('list page: %s', response.url)
        sel = Selector(response)
        for detail_link in sel.xpath(templateConfig.detail_page_rule1).extract(): # 找到具体的内容页链接
            yield scrapy.Request(detail_link, callback=self.parse_detail)
        
        for list_link in sel.xpath(templateConfig.list_page_rule2).extract(): # 找到列表页的下一页链接
            yield scrapy.Request(list_link, callback=self.parse_list)
            
    def parse_detail(self, response):
        logging.debug('content page: %s', response.url);  
        item = self.parse_with_rules(response, self.item_rules, meizituItem)
        pprint.pprint(item)
        return item
