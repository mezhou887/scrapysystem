# -*- coding: utf-8 -*-

from scrapy import cmdline 

if __name__ =="__main__":
    
    # 3. 使用RedisSpider
    cmdline.execute("scrapy crawl manong".split());
