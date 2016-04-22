# -*- coding: utf-8 -*-
import logging
import pprint
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from xxxiao.items import *    #这个错误是eclipse自己的编译器错误，不用管
from misc.log import pp
from misc.xpathspider import XpathSpider
from scrapy_redis.spiders import RedisMixin
from bs4 import BeautifulSoup


# 范例1，使用最基本的Spider来完成
class XxxiaoSpider(CrawlSpider):
    name = "xxxiao_base"
    allowed_domains = ["xxxiao.com"]
    start_urls = [
        "http://www.xxxiao.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_xxxiao', follow=True)
    ]
    
    def parse_xxxiao(self, response):
        logging.debug('content page: %s', response.url);  
        item = xxxiaoItem()
        item['pagelink'] = response.url
        item['title'] = response.xpath('//title/text()').extract()
        return item
    

# 范例2，在范例1的基础上用item_rules来指明存储的字段 
class XxxiaoXpathSpider(XpathSpider):
    name = "xxxiao_xpath"
    allowed_domains = ["xxxiao.com"]
    start_urls = [
        "http://www.xxxiao.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_xxxiao', follow=True)
    ]

    item_rules = { 
        '//title': {
            '__use': 'dump',                    
            'title': 'text()',
            '__link': 'pagelink',
        }   
    }           

    def parse_xxxiao(self, response):
        logging.debug('content page: %s', response.url);  
        # pp.pprint(self.parse_with_rules(response, self.item_rules, dict)) 
        item = self.parse_with_rules(response, self.item_rules, xxxiaoItem)
        pp.pprint(item)
        return item
        
 
# 范例3，在范例2的基础上加入Redis           
class XxxiaoXpathRedisSpider(RedisMixin, XpathSpider):  
    name = 'xxxiao_redis'
    allowed_domains = ["xxxiao.com"]
    start_urls = [
        "http://www.xxxiao.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_xxxiao', follow=True)
    ]

    item_rules = { 
        '//title': {
            '__use': 'dump',                    
            'title': 'text()',
            '__link': 'pagelink',
        }   
    }                 
    
    def _set_crawler(self, crawler):
        XpathSpider._set_crawler(self, crawler)
        RedisMixin.setup_redis(self)
        
    def parse_xxxiao(self, response):
        logging.debug('content page: %s', response.url);  
        soup = BeautifulSoup(response.body, "lxml")
        logging.debug(soup.prettify())
        # pp.pprint(self.parse_with_rules(response, self.item_rules, dict))
        item = self.parse_with_rules(response, self.item_rules, xxxiaoItem)
        # pp.pprint(item)
        pprint.pprint(item)        
        return item 
