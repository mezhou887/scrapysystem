# -*- coding: utf-8 -*-
import logging
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from proxylist.items import *    #这个错误是eclipse自己的编译器错误，不用管
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider


# 范例1，使用最基本的Spider来完成
class ProxylistSpider(CrawlSpider):
    name = "proxylist"
    allowed_domains = ["free-proxy-list.net"]
    start_urls = [
        "https://free-proxy-list.net/",
    ]
    
    rules = [
        Rule(LinkExtractor(allow=("/$")), callback='parse_proxylist', follow=True),
    ]

    def parse_proxylist(self, response):
        logging.info('content page: %s', response.url);  
        sel = Selector(response)
        items = []
        for td_content in sel.xpath('//tbody/tr').extract(): 
            content = Selector(text=td_content)
            item = proxylistItem()
            item["ip"] = content.xpath('//td[1]/text()').extract()
            item["port"] = content.xpath('//td[2]/text()').extract()
            item["code"] = content.xpath('//td[3]/text()').extract()
            item["country"] = content.xpath('//td[4]/text()').extract()
            item["anonymity"] = content.xpath('//td[5]/text()').extract()
            item["google"] = content.xpath('//td[6]/text()').extract()
            item["https"] = content.xpath('//td[7]/text()').extract()
            item["last_checked"] = content.xpath('//td[8]/text()').extract()
            items.append(item)
             
        return items