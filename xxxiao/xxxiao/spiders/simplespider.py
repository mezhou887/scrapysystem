# -*- coding: utf-8 -*-
import scrapy
import logging
import pprint

from xxxiao.items import *    #这个错误是eclipse自己的编译器错误
from misc.xpathspider import BaseXpathSpider
from misc.log import pp
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisMixin
from bs4 import BeautifulSoup

# 范例1，使用最基本的Spider来完成
# 1. 从主页得到所有列表页的首页链接
# 2. 根据列表页的首页链接去得到下一页的链接，递归的遍历完整个列表页
# 3. 在每个列表页中找到内容页的链接，然后去访问具体的内容页
class XxxiaoSpider(scrapy.Spider):
    name = "xxxiao_base"
    allowed_domains = ["xxxiao.com"]
    start_urls = [
        "http://www.xxxiao.com/",
    ]

    def parse(self, response):
        logging.debug('start page: %s', response.url)
        sel = Selector(response)
        for link in sel.xpath('//div[@class="tags"]/span/a/@href').extract(): # 找到列表页的首页链接
            request = scrapy.Request(link, callback=self.parse_list)
            yield request
        
    def parse_list(self, response):
        logging.debug('list page: %s', response.url)
        sel = Selector(response)
        for link in sel.xpath('//div[@class="inWrap"]/ul/li/div/div/a/@href').extract(): # 找到具体的内容页链接
            yield scrapy.Request(link, callback=self.parse_detail)
        
        for link in sel.xpath('//div[@class="navigation"]/div[@id="wp_page_numbers"]/ul/li/a[contains(text(), "下一页")]/@href').extract(): # 找到列表页的下一页链接
            yield scrapy.Request(link, callback=self.parse_list)                
           
    def parse_detail(self, response):
        logging.debug('content page: %s', response.url);  
        item = xxxiaoItem()
        item['pagelink'] = response.url
        item['title'] = response.xpath('//title/text()').extract()
        item['name'] = response.xpath('//h2/a/text()').extract()
        item['image_urls'] = response.xpath('//div[@id="picture"]/p/img/@src').extract()
        return item   
    
    
# 范例2，在范例1的基础上用item_rules来指明存储的字段    
class XxxiaoXpathSpider(BaseXpathSpider):
    name = "xxxiao_xpath"
    allowed_domains = ["xxxiao.com"]
    start_urls = [
        "http://www.xxxiao.com/",
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
            'image_urls': '//div[@id="picture"]/p/img/@src'                             
        }             
    }
    
    def parse(self, response):
        logging.debug('start page: %s', response.url)
        sel = Selector(response)
        for link in sel.xpath('//div[@class="tags"]/span/a/@href').extract(): # 找到列表页的首页链接
            yield scrapy.Request(link, callback=self.parse_list)
        
    def parse_list(self, response):
        logging.debug('list page: %s', response.url)
        sel = Selector(response)
        for link in sel.xpath('//div[@class="inWrap"]/ul/li/div/div/a/@href').extract(): # 找到具体的内容页链接
            yield scrapy.Request(link, callback=self.parse_detail)
        
        for link in sel.xpath('//div[@class="navigation"]/div[@id="wp_page_numbers"]/ul/li/a[contains(text(), "下一页")]/@href').extract(): # 找到列表页的下一页链接
            yield scrapy.Request(link, callback=self.parse_list)
            
    def parse_detail(self, response):
        logging.debug('content page: %s', response.url);  
        item = self.parse_with_rules(response, self.item_rules, meizituItem)
        pp.pprint(item)
        return item
    

# 范例3，在范例2的基础上加入Redis      
class XxxiaoXpathRedisSpider(RedisMixin, BaseXpathSpider):
    name = "xxxiao_redis"
    allowed_domains = ["xxxiao.com"]
    start_urls = [
        "http://www.xxxiao.com/",
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
            'image_urls': '//div[@id="picture"]/p/img/@src'                             
        }             
    }         
        
    def _set_crawler(self, crawler):
        super(xxxiaoXpathRedisSpider, self)._set_crawler(crawler)
        self.setup_redis()            
        
    def parse(self, response):
        logging.debug('start page: %s', response.url)
        soup = BeautifulSoup(response.body, "lxml")
        logging.debug(soup.prettify())
        sel = Selector(response)
        for link in sel.xpath('//div[@class="tags"]/span/a/@href').extract(): # 找到列表页的首页链接
            yield scrapy.Request(link, callback=self.parse_list)
        
    def parse_list(self, response):
        logging.debug('list page: %s', response.url)
        sel = Selector(response)
        for link in sel.xpath('//div[@class="inWrap"]/ul/li/div/div/a/@href').extract(): # 找到具体的内容页链接
            yield scrapy.Request(link, callback=self.parse_detail)
        
        for link in sel.xpath('//div[@class="navigation"]/div[@id="wp_page_numbers"]/ul/li/a[contains(text(), "下一页")]/@href').extract(): # 找到列表页的下一页链接
            yield scrapy.Request(link, callback=self.parse_list)
            
    def parse_detail(self, response):
        logging.debug('content page: %s', response.url);  
        item = self.parse_with_rules(response, self.item_rules, meizituItem)
        pprint.pprint(item)
        return item
