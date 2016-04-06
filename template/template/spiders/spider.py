# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

from scrapy.spiders import Spider, CrawlSpider, XMLFeedSpider, CSVFeedSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor 

from template.items import *    #这个错误是eclipse自己的编译器错误
from misc.log import *
from misc.spider import CommonSpider
from scrapy_redis.spiders import RedisMixin

class templateSpider(CommonSpider):
    name = "template"
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/subject/\d+/?$")), callback='parse_test', follow=True),
        # Rule(LinkExtractor(allow=("/subject/\d+/?$")), callback='parse_template', follow=True),
    ]

    item_rules = { 
        '//title': {
            '__use': 'dump',                    
            'title': 'text()',
            '__link': 'pagelink',
        }   
    }     
    
    def __init__(self, *args, **kwargs):
        super(templateSpider, self).__init__(*args, **kwargs)
        
    def parse_test(self, response):
        log.info('Parse '+response.url)
        pp.pprint(self.parse_with_rules(response, self.item_rules, dict))      

    def parse_template(self, response):
        log.info('Parse '+response.url)
        item = self.parse_with_rules(response, self.item_rules, templateItem)
        item['link'] = response.url
        return item
        
        
class templateRedisSpider(RedisMixin, CrawlSpider):  
    name = 'template_redis'
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/subject/\d+/?$")), callback='parse_test', follow=True),
    ] 

    item_rules = { 
        '//title': {
            '__use': 'dump',                    
            'title': 'text()',
            '__link': 'pagelink',
        }   
    }        
    
    def __init__(self, *args, **kwargs):
        super(templateRedisSpider, self).__init__(*args, **kwargs)
    
    def parse_test(self, response):
        log.info('Parse '+response.url)
        pp.pprint(self.parse_with_rules(response, self.item_rules, dict))
    
    def _set_crawler(self, crawler):
        CrawlSpider._set_crawler(self, crawler)
        RedisMixin.setup_redis(self)
        
    def parse_template(self, response):
        log.info('Parse '+response.url)
        item = self.parse_with_rules(response, self.item_rules, templateItem)
        item['link'] = response.url
        return item 
        
        
        
        