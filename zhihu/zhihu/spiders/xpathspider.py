# -*- coding: utf-8 -*-
import logging
import pprint
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from zhihu.items import *    #这个错误是eclipse自己的编译器错误，不用管
from misc.log import pp
from misc.xpathspider import XpathSpider
from scrapy_redis.spiders import RedisMixin
from bs4 import BeautifulSoup


# 范例1，使用最基本的Spider来完成
class ZhihuSpider(CrawlSpider):
    name = "zhihu_base"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        "http://www.zhihu.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_zhihu', follow=True)
    ]
    
    def parse_zhihu(self, response):
        logging.debug('content page: %s', response.url);  
        item = zhihuItem()
        item['pagelink'] = response.url
        item['title'] = response.xpath('//title/text()').extract()
        return item
    

# 范例2，在范例1的基础上用item_rules来指明存储的字段 
class ZhihuXpathSpider(XpathSpider):
    name = "zhihu_xpath"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        "http://www.zhihu.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_zhihu', follow=True)
    ]

    item_rules = { 
        '//title': {
            '__use': 'dump',                    
            'title': 'text()',
            '__link': 'pagelink',
        }   
    }           

    def parse_zhihu(self, response):
        logging.debug('content page: %s', response.url);  
        # pp.pprint(self.parse_with_rules(response, self.item_rules, dict)) 
        item = self.parse_with_rules(response, self.item_rules, zhihuItem)
        pp.pprint(item)
        return item
        
 
# 范例3，在范例2的基础上加入Redis           
class ZhihuXpathRedisSpider(RedisMixin, XpathSpider):  
    name = 'zhihu_redis'
    allowed_domains = ["zhihu.com"]
    start_urls = [
        "http://www.zhihu.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_zhihu', follow=True)
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
        
    def parse_zhihu(self, response):
        logging.debug('content page: %s', response.url);  
        soup = BeautifulSoup(response.body, "lxml")
        logging.debug(soup.prettify())
        # pp.pprint(self.parse_with_rules(response, self.item_rules, dict))
        item = self.parse_with_rules(response, self.item_rules, zhihuItem)
        # pp.pprint(item)
        pprint.pprint(item)        
        return item 
