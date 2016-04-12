# -*- coding: utf-8 -*-
import logging
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from template.items import *    #这个错误是eclipse自己的编译器错误，不用管
from misc.log import pp
from misc.xpathspider import XpathSpider
from scrapy_redis.spiders import RedisMixin

class templateXpathSpider(XpathSpider):
    name = "template"
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/a/[0-9]+\.html")), callback='parse_template', follow=True),
    ]

    item_rules = { 
        '//title': {
            '__use': 'dump',                    
            'title': 'text()',
            '__link': 'pagelink',
        }   
    }           

    def parse_template(self, response):
        logging.debug('Parse '+response.url)
        # pp.pprint(self.parse_with_rules(response, self.item_rules, dict)) 
        item = self.parse_with_rules(response, self.item_rules, templateItem)
        pp.pprint(item)
        return item
        
        
class templateXpathRedisSpider(RedisMixin, XpathSpider):  
    name = 'template_redis'
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/a/[0-9]+\.html")), callback='parse_template', follow=True),
    ] 

    item_rules = { 
        '//title': {
            '__use': 'dump',                    
            'title': 'text()',
            '__link': 'pagelink',
        }   
    }                 
    
    def _set_crawler(self, crawler):
        super(templateXpathRedisSpider, self)._set_crawler(crawler)
        self.setup_redis()
        
    def parse_template(self, response):
        logging.debug('Parse '+response.url)
        # pp.pprint(self.parse_with_rules(response, self.item_rules, dict))
        item = self.parse_with_rules(response, self.item_rules, templateItem)
        pp.pprint(item)
        return item 