# -*- coding: utf-8 -*-

from scrapy import cmdline 

if __name__ =="__main__":
    
    # 1. simplespider
    # cmdline.execute("scrapy crawl template_v1".split());
    cmdline.execute("scrapy crawl template_v1 -o template.json".split())
    
    # cmdline.execute("scrapy crawl template_redis".split())
    # cmdline.execute("scrapy runspider template.py -o template.json".split());