# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

from scrapy.spiders import Spider, CrawlSpider, XMLFeedSpider, CSVFeedSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor 

from cnbeta.items import *    #这个错误是eclipse自己的编译器错误
from misc.log import *
from misc.xpathspider import XpathSpider
from scrapy_redis.spiders import RedisMixin

class cnbetaSpider(XpathSpider):
    name = "cnbeta"
    allowed_domains = ["cnbeta.com"]
    start_urls = [
        "http://www.cnbeta.com/",
    ]
    
    rules = [
        #Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_test', follow=True),
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_cnbeta', follow=True)
    ]

    item_rules = { 
        '//title': {
            '__use': 'dump',                    
            'title': 'text()',
            '__link': 'pagelink',
        }   
    }     
    
    def __init__(self, *args, **kwargs):
        super(cnbetaSpider, self).__init__(*args, **kwargs)
        
    def parse_test(self, response):
        log.info('Parse '+response.url)
        pp.pprint(self.parse_with_rules(response, self.item_rules, dict))      

    def parse_cnbeta(self, response):
        log.info('Parse '+response.url)
        item = self.parse_with_rules(response, self.item_rules, cnbetaItem)
        pp.pprint(item)
        return item
        
        
class cnbetaRedisSpider(RedisMixin, XpathSpider):  
    name = 'cnbeta_redis'
    allowed_domains = ["cnbeta.com"]
    start_urls = [
        "http://www.cnbeta.com/",
    ]
    
    rules = [
        #Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_test', follow=True),
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_cnbeta', follow=True)
    ] 

    item_rules = { 
        '//title': {
            '__use': 'dump',                    
            'title': 'text()',
            '__link': 'pagelink',
        }   
    }        
    
    def __init__(self, *args, **kwargs):
        super(cnbetaRedisSpider, self).__init__(*args, **kwargs)
    
    def parse_test(self, response):
        log.info('Parse '+response.url)
        pp.pprint(self.parse_with_rules(response, self.item_rules, dict))
    
    def _set_crawler(self, crawler):
        CrawlSpider._set_crawler(self, crawler)
        RedisMixin.setup_redis(self)
        
    def parse_cnbeta(self, response):
        log.info('Parse '+response.url)
        item = self.parse_with_rules(response, self.item_rules, cnbetaItem)
        pp.pprint(item)
        return item     
