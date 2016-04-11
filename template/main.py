# -*- coding: utf-8 -*-

from scrapy import cmdline 

if __name__ =="__main__":
    
    # 1. simplespider: 使用最基本的Spider来完成,以meizitu为模板来完成的
    # cmdline.execute("scrapy crawl template_v1".split());
    cmdline.execute("scrapy crawl template_v1 -o template.json".split())
    
    # cmdline.execute("scrapy crawl template_redis".split())
    # cmdline.execute("scrapy runspider template.py -o template.json".split());