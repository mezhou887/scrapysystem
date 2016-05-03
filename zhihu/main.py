# -*- coding: utf-8 -*-

from scrapy import cmdline 

if __name__ =="__main__":
    
#     cmdline.execute("scrapy crawl zhihu_login".split());
    cmdline.execute("scrapy crawl zhihu_user".split());
#     cmdline.execute("scrapy crawl zhihu_ask".split());
#     cmdline.execute("scrapy crawl zhihu_answer".split());
