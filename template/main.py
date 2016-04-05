# -*- coding: utf-8 -*-

from scrapy import cmdline 

if __name__ =="__main__":
    cmdline.execute("scrapy crawl template".split());
    cmdline.execute("scrapy crawl template -o template.json".split());
    # cmdline.execute("scrapy runspider template.py -o template.json".split());