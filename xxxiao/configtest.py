# -*- coding: utf-8 -*-
'''
Created on 2016年4月23日

@author: 周茂恩
'''
import unittest
import urllib2
from bs4 import BeautifulSoup
from scrapy.selector import Selector

class Test(unittest.TestCase):
    
    list_page_rule1='//div[@class="nav-previous"]/a/@href'
    list_page_rule2='//ul[@id="menu-nav"]/li/a/@href'
    detail_page_rule1='//a[@class="thumb-link"]/@href'
    detail_page_rule2='//div[@class="post-thumb"]/a/@href'


    def testListPage1(self):
        html = urllib2.urlopen(r'http://m.xxxiao.com/').read()
        sel = Selector(text=html);
        print '1', sel.xpath(self.list_page_rule1).extract()
        
    def testListPage2(self):
        html = urllib2.urlopen(r'http://m.xxxiao.com/').read()
        sel = Selector(text=html);
        print '2', sel.xpath(self.list_page_rule2).extract()

    def testDetailPage1(self):
        html = urllib2.urlopen(r'http://m.xxxiao.com/').read()
        sel = Selector(text=html);
        print '3', sel.xpath(self.detail_page_rule1).extract()
        
    def testDetailPage2(self):
        html = urllib2.urlopen(r'http://m.xxxiao.com/39056').read()
        soup = BeautifulSoup(html, "lxml")
        print(soup.prettify())
        sel = Selector(text=html);
        print '4', sel.xpath(self.detail_page_rule2).extract()    

if __name__ == "__main__":
    unittest.main()