# -*- coding: utf-8 -*-

from scrapy import cmdline 

if __name__ =="__main__":
    
    # 1. simplespider: 使用最基本的Spider来完成,以meizitu为模板来完成的
    #cmdline.execute("scrapy crawl template_base".split());
    #cmdline.execute("scrapy crawl template_base -o meizitu.json".split())
    
    #2. 使用XpathSpider
    cmdline.execute("scrapy crawl template_xpath".split());
    
    #3. 使用CssSpider
    # cmdline.execute("scrapy crawl template_css".split());
    
    #4. 使用RedisSpider
    # cmdline.execute("scrapy crawl template_redis".split());
    
    # cmdline.execute("scrapy crawl template_redis".split())
    # cmdline.execute("scrapy runspider template.py -o template.json".split());