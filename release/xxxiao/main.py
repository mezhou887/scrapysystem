# -*- coding: utf-8 -*-

from scrapy import cmdline 

if __name__ =="__main__":
    
    # 1. simplespider: 使用最基本的Spider来完成,以meizitu为模板来完成的
    cmdline.execute("scrapy crawl xxxiao_base".split());
    
    # 2. 持久化一个爬虫，使它能暂停/继续爬取
    # cmdline.execute("scrapy crawl xxxiao_base -s JOBDIR=crawls/xxxiaospider-1".split());
    
    # 3. 导出Json, xml, csv文件
    # cmdline.execute("scrapy crawl xxxiao_base -o xxxiao_data.json".split());
    # cmdline.execute("scrapy crawl xxxiao_base -o xxxiao_data.jsonlines".split());
    # cmdline.execute("scrapy crawl xxxiao_base -o xxxiao_data.xml".split());
    # cmdline.execute("scrapy crawl xxxiao_base -o xxxiao_data.csv".split());
    