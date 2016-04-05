# -*- coding: utf-8 -*-

from scrapy import cmdline 

if __name__ =="__main__":
    cmdline.execute("scrapy crawl cnbeta".split());
    # cmdline.execute("scrapy crawl cnbeta -o cnbeta.json".split());
    # cmdline.execute("scrapy runspider cnbeta.py -o cnbeta.json".split());
