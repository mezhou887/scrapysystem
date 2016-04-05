
from scrapy.selector import Selector

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from cnbeta.items import *
from misc.log import log, pp
from misc.spider import CommonSpider

class cnbetaSpider(CommonSpider):
    name = "cnbeta"
    allowed_domains = ["cnbeta.com"]
    start_urls = [
        "http://www.cnbeta.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_cnbeta', follow=True),
    ]

    item_rules = { 
        'title': '//title/text()',    
        '__link': 'pagelink',
    }     
    
    def __init__(self, *args, **kwargs):
        super(cnbetaSpider, self).__init__(*args, **kwargs)

    def parse_cnbeta(self, response):
        for k, v in self.item_rules.items():
            print(k,v)
        log.info('Parse '+response.url)
        item = self.parse_with_rules(response, self.item_rules, cnbetaItem)
        return item 
        
        
        
        
