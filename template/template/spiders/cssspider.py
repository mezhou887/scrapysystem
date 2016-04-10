# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from template.items import *    #这个错误是eclipse自己的编译器错误，不用管
from misc.log import log, pp
from misc.cssspider import CssSpider
from scrapy_redis.spiders import RedisMixin

class templateCssSpider(CssSpider):
    name = "template"
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/a/[0-9]+\.html"), callback="parse_template", follow=True)),
    ]  
    
    item_rules = {
    
    }
      
    def __init__(self, *args, **kwargs):
        super(templateCssSpider, self).__init__(*args, **kwargs)
        log.debug('__init__')                   

    def parse_template(self, response):
        log.info('Parse '+response.url)
        # pp.pprint(self.parse_with_rules(response, self.item_rules, dict)) 
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
        Rule(LinkExtractor(allow=("/a/[0-9]+\.html"), callback="parse_template", follow=True)),
    ]  
    
    item_rules = {
    
    }
      
    def __init__(self, *args, **kwargs):
        super(templateCssRedisSpider, self).__init__(*args, **kwargs)
        log.debug('__init__')     
        
    def _set_crawler(self, crawler):
        CrawlSpider._set_crawler(self, crawler)
        RedisMixin.setup_redis(self)           

    def parse_template(self, response):
        log.info('Parse '+response.url)
        # pp.pprint(self.parse_with_rules(response, self.item_rules, dict))
        item = self.parse_with_rules(response, self.item_rules, templateItem)
        pp.pprint(item)
        return item      
    
    