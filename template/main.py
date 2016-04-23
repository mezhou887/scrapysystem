# -*- coding: utf-8 -*-

from scrapy import cmdline 

if __name__ =="__main__":
    
    # 1. simplespider: 使用最基本的Spider来完成,以meizitu为模板来完成的
    #cmdline.execute("scrapy crawl template_base".split());
    
    # 2. 使用XpathSpider
    # cmdline.execute("scrapy crawl template_xpath".split());
    
    # 3. 使用RedisSpider
    cmdline.execute("scrapy crawl template_redis".split());
    
    # 4. 持久化一个爬虫，使它能暂停/继续爬取
    #cmdline.execute("scrapy crawl template_base -s JOBDIR=crawls/templatespider-1".split());
    
    # 5. 导出Json, xml, csv文件
    # cmdline.execute("scrapy crawl template_base -o template_data.json".split());
    # cmdline.execute("scrapy crawl template_base -o template_data.jsonlines".split());
    # cmdline.execute("scrapy crawl template_base -o template_data.xml".split());
    # cmdline.execute("scrapy crawl template_base -o template_data.csv".split());    