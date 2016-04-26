# -*- coding: utf-8 -*-
import scrapy
import logging

from woaidu.items import *    #这个错误是eclipse自己的编译器错误
from scrapy.selector import Selector
from scrapy.http import Request
from misc.utils import list_first_item,clean_url

# 范例1，使用最基本的Spider来完成
# 1. 从主页得到所有列表页的首页链接
# 2. 根据列表页的首页链接去得到下一页的链接，递归的遍历完整个列表页
# 3. 在每个列表页中找到内容页的链接，然后去访问具体的内容页
class WoaiduSpider(scrapy.Spider):
    name = "woaidu_base"
    allowed_domains = ["woaidu.org"]
    start_urls = [
        "http://www.woaidu.org/sitemap_1.html",
    ]

    def parse(self, response):
        logging.info('list page: %s', response.url)
        sel = Selector(response)
        next_text = u'下一页'
        next_link = list_first_item(sel.xpath('//div[@class="k2"]/div/a[text()="'+next_text+'"]/@href').extract())
        print next_link
        if next_link:
            next_link = clean_url(response.url,next_link,response.encoding)
            yield Request(url=next_link, callback=self.parse)

        for detail_link in sel.xpath('//div[contains(@class,"sousuolist")]/a/@href').extract():
            if detail_link:
                detail_link = clean_url(response.url,detail_link,response.encoding)
                yield Request(url=detail_link, callback=self.parse_detail)  
                      
    def parse_detail(self, response):
        item = woaiduItem()
        
        sel = Selector(response)
        item['book_name'] = list_first_item(sel.xpath('//div[@class="zizida"][1]/text()').extract())
        item['author'] = [list_first_item(sel.xpath('//div[@class="xiaoxiao"][1]/text()').extract())[5:].strip(),]
        item['book_description'] = list_first_item(sel.xpath('//div[@class="lili"][1]/text()').extract()).strip()
        item['book_covor_image_url'] = list_first_item(sel.xpath('//div[@class="hong"][1]/img/@src').extract())
        item['original_url'] = response.url                
        return item   
    
