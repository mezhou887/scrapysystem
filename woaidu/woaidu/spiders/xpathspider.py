# -*- coding: utf-8 -*-
import logging
import pprint
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from woaidu.items import *    #这个错误是eclipse自己的编译器错误，不用管
from misc.log import pp
from misc.xpathspider import XpathSpider
from scrapy_redis.spiders import RedisMixin
from bs4 import BeautifulSoup


# 范例1，使用最基本的Spider来完成
class WoaiduSpider(CrawlSpider):
    name = "woaidu_base"
    allowed_domains = ["woaidu.com"]
    start_urls = [
        "http://www.woaidu.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_woaidu', follow=True)
    ]
    
    def parse_woaidu(self, response):
        logging.debug('content page: %s', response.url);  
        item = woaiduItem()
        item['pagelink'] = response.url
        item['title'] = response.xpath('//title/text()').extract()
        return item
    

# 范例2，在范例1的基础上用item_rules来指明存储的字段 
class WoaiduXpathSpider(XpathSpider):
    name = "woaidu_xpath"
    allowed_domains = ["woaidu.com"]
    start_urls = [
        "http://www.woaidu.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_woaidu', follow=True)
    ]

    item_rules = { 
        '//title': {
            '__use': 'dump',                    
            'title': 'text()',
            '__link': 'pagelink',
        }   
    }           

    def parse_woaidu(self, response):
        logging.debug('content page: %s', response.url);  
        # pp.pprint(self.parse_with_rules(response, self.item_rules, dict)) 
        item = self.parse_with_rules(response, self.item_rules, woaiduItem)
        pp.pprint(item)
        return item
        
 
# 范例3，在范例2的基础上加入Redis           
class WoaiduXpathRedisSpider(RedisMixin, XpathSpider):  
    name = 'woaidu_redis'
    allowed_domains = ["woaidu.com"]
    start_urls = [
        "http://www.woaidu.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_woaidu', follow=True)
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
        
    def parse_woaidu(self, response):
        logging.debug('content page: %s', response.url);  
        soup = BeautifulSoup(response.body, "lxml")
        logging.debug(soup.prettify())
        # pp.pprint(self.parse_with_rules(response, self.item_rules, dict))
        item = self.parse_with_rules(response, self.item_rules, woaiduItem)
        # pp.pprint(item)
        pprint.pprint(item)        
        return item 
