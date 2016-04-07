# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from template.items import *    #这个错误是eclipse自己的编译器错误
from misc.log import log, pp

class templateSpider(CrawlSpider):
    name = "template"
    allowed_domains = ["template.com"]
    start_urls = [
        "http://www.template.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/position.php\?&start=\d{,4}#a")), callback='parse_template', follow=True)
    ]

    def parse_template(self, response):
        item = templateItem()
        item['pagelink'] = response.url
        pp.pprint(item)
        log.info('parsed ' + str(response))
        return item

