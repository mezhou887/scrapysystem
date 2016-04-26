# -*- coding: utf-8 -*-

from jiandan.items import jiandanItem    #这个错误是eclipse自己的编译器错误
from scrapy_redis.spiders import RedisSpider

class JiandanSpider(RedisSpider):
    name = "jiandan_redis"
    allowed_domains = ["jandan.net"]
    start_urls = [
        "http://jandan.net/ooxx",
    ]
    start_urls = ['http://jandan.net/ooxx/page-'+str(i)+'#comments' for i in range(1500, 2000)]
        
    # http://jandan.net/ooxx/page-1953#comments
    def parse(self, response):
        print response.url;  
        item = jiandanItem()
        item['pagelink'] = response.url
        item['title'] = response.xpath('//title/text()').extract()
        item['image_urls'] = response.xpath('//div[@class="text"]/p/a/@href').extract()
        return item