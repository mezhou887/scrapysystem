# -*- coding: utf-8 -*-
import logging
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from cnbeta.items import *    #这个错误是eclipse自己的编译器错误，不用管

# 范例1，使用最基本的Spider来完成
class CnbetaSpider(CrawlSpider):
    name = "cnbeta_base"
    allowed_domains = ["cnbeta.com"]
    start_urls = [
        "http://www.cnbeta.com/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/articles/.*\.htm")), callback='parse_cnbeta', follow=True)
    ]
    
    def parse_cnbeta(self, response):
        logging.debug('content page: %s', response.url);  
        item = cnbetaItem()
        item['pagelink'] = response.url
        item['title'] = response.xpath('//title/text()').extract()
        return item
    