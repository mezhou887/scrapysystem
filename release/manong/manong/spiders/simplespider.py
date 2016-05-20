# -*- coding: utf-8 -*-
import scrapy
from manong.items import manongItem
from scrapy.selector import Selector

class manongSpider(scrapy.Spider):
    name = "manong"
    allowed_domains = ["weekly.manong.io"]
    
    # http://weekly.manong.io/issues/118
    start_urls = ['http://weekly.manong.io/issues/'+str(i) for i in range(1, 200)]
        
    def parse(self, response):
        print response.url
        sel = Selector(response)
        items = []
        articles  = sel.xpath('//h4').extract()
        for article in articles:
            article_sel  = Selector(text=article)
            item         = manongItem()
            item['name'] = article_sel.xpath('//a/text()').extract()[0].strip()
            item['link'] = article_sel.xpath('//a/@href').extract()[0].strip()
            items.append(item)
            
        return items        
