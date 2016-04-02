
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

from scrapy.contrib.spiders import Spider, CrawlSpider, XMLFeedSpider, CSVFeedSpider
from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor 

from template.template.items import *
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
        Rule(LinkExtractor(allow=("/subject/\d+/?$")), callback='parse_template', follow=True),
    ]

    item_rules = { 
        '.linkto': {
            'url': 'a::attr(href)',
            'name': 'a::text',
        }   
    }     
    
    def __init__(self, *args, **kwargs):
        super(templateSpider, self).__init__(*args, **kwargs)

    def parse_template(self, response):
        log.info('Parse '+response.url)
        items = self.parse_with_rules(response, self.item_rules, templateItem)
        pp.pprint(items)
        return items
        
        
class templateRedisSpider(RedisMixin, CrawlSpider):  
    name = 'template_redis'
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(), callback='parse_template', follow=True),
    ] 

    item_rules = { 
        '.linkto': {
            'url': 'a::attr(href)',
            'name': 'a::text',
        }   
    }        
    
    def __init__(self, *args, **kwargs):
        super(templateRedisSpider, self).__init__(*args, **kwargs)
    
    
    def _set_crawler(self, crawler):
        CrawlSpider._set_crawler(self, crawler)
        RedisMixin.setup_redis(self)
        
    def parse_template(self, response):
        log.info('Parse '+response.url)
        items = self.parse_with_rules(response, self.item_rules, templateItem)
        pp.pprint(items)
        return items   
        
        
        
        