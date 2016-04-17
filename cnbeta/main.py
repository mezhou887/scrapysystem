# -*- coding: utf-8 -*-

from scrapy import cmdline 

if __name__ =="__main__":
    
    # 1. simplespider: 使用最基本的Spider来完成,以meizitu为模板来完成的
    cmdline.execute("scrapy crawl cnbeta_base".split());
    
    #2. 使用XpathSpider
    # cmdline.execute("scrapy crawl cnbeta_xpath".split());
    
    #3. 使用RedisSpider
    # cmdline.execute("scrapy crawl cnbeta_redis".split());
