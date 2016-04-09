# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from template.items import templateItem    #这个错误是eclipse自己的编译器错误，不用管
from misc.log import log, pp
from misc.xpathspider import XpathSpider
from misc.cssspider import CssSpider
from scrapy_redis.spiders import RedisMixin

class templateXpathSpider(XpathSpider):
    name = "template"
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/subject/\d+/?$")), callback="parse_test", follow=True),
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
        super(templateXpathSpider, self).__init__(*args, **kwargs)
        
    def parse_test(self, response):
        log.info('Parse '+response.url)
        pp.pprint(self.parse_with_rules(response, self.item_rules, dict))      

    def parse_template(self, response):
        log.info('Parse '+response.url)
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
        Rule(LinkExtractor(allow=("/subject/\d+/?$")), callback="parse_test", follow=True),
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
        super(templateXpathRedisSpider, self).__init__(*args, **kwargs)
    
    def parse_test(self, response):
        log.info('Parse '+response.url)
        pp.pprint(self.parse_with_rules(response, self.item_rules, dict))
    
    def _set_crawler(self, crawler):
        CrawlSpider._set_crawler(self, crawler)
        RedisMixin.setup_redis(self)
        
    def parse_template(self, response):
        log.info('Parse '+response.url)
        item = self.parse_with_rules(response, self.item_rules, templateItem)
        pp.pprint(item)
        return item 
        
class templateCssSpider(CssSpider):
    name = "template"
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/subject/\d+/?$"), callback="parse_test", follow=True)),
        # Rule(LinkExtractor(allow=("/subject/\d+/?$"), callback="parse_template", follow=True)),
    ]  
    
    item_rules = {
    
    }
      
    def __init__(self, *args, **kwargs):
        super(templateCssSpider, self).__init__(*args, **kwargs)
        
    def parse_test(self, response):
        log.info('Parse '+response.url)
        pp.pprint(self.parse_with_rules(response, self.item_rules, dict))      

    def parse_template(self, response):
        log.info('Parse '+response.url)
        item = self.parse_with_rules(response, self.item_rules, templateItem)
        pp.pprint(item)
        return item   
    
    
class templateCssRedisSpider(RedisMixin, CssSpider):
    name = 'template_redis'
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/subject/\d+/?$"), callback="parse_test", follow=True)),
        # Rule(LinkExtractor(allow=("/subject/\d+/?$"), callback="parse_template", follow=True)),
    ]  
    
    item_rules = {
    
    }
      
    def __init__(self, *args, **kwargs):
        super(templateCssRedisSpider, self).__init__(*args, **kwargs)
        
    def parse_test(self, response):
        log.info('Parse '+response.url)
        pp.pprint(self.parse_with_rules(response, self.item_rules, dict))   
        
    def _set_crawler(self, crawler):
        CrawlSpider._set_crawler(self, crawler)
        RedisMixin.setup_redis(self)           

    def parse_template(self, response):
        log.info('Parse '+response.url)
        item = self.parse_with_rules(response, self.item_rules, templateItem)
        pp.pprint(item)
        return item      
      