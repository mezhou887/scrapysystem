# -*- coding: utf-8 -*-

from scrapy import cmdline 

if __name__ =="__main__":
    
    # 1. simplespider: 使用最基本的Spider来完成,以meizitu为模板来完成的
    #cmdline.execute("scrapy crawl meizitu_v1".split());
    #cmdline.execute("scrapy crawl meizitu_v1 -o meizitu.json".split())
    
    #2. 使用XpathSpider
    cmdline.execute("scrapy crawl meizitu_v2".split());
    
    # cmdline.execute("scrapy crawl meizitu_redis".split())
    # cmdline.execute("scrapy runspider meizitu.py -o meizitu.json".split());
