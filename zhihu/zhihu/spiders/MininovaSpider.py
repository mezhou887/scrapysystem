# -*- coding: utf-8 -*-
'''
Created on 2016年5月3日

@author: Administrator
'''
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.response import get_base_url
from scrapy.linkextractors import LinkExtractor
from zhihu.items import *

class bobao_spider(CrawlSpider):
    
    name="bobao"
    allowed_domains=["360.cn"]
    start_urls=["http://bobao.360.cn/learning/index&page=1"]
    rules=[
        Rule(LinkExtractor(allow=("/learning/index&page=\d{1,3}")),follow=True,callback='parse_item')
    ]#定义提取链接的规则，继续跟进，提取到的链接回调给parse_item函数作为参数
    
    def parse_item(self,response):
        print response.url
        base_url=get_base_url(response)
        for site in response.xpath('//ul[@id="learning-list"]'):
            item=BobaoItem()
            item['name']=site.xpath('li/div/a/text()').extract()
            item['link']=site.xpath('li/div/a/@href').extract()
            item['time']=site.xpath('li/div/p/span[@class="time"]/text()').extract()
        return item