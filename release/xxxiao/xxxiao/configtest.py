# -*- coding: utf-8 -*-
'''
Created on 2016年4月23日

@author: 周茂恩
'''
import unittest
import urllib2
# from bs4 import BeautifulSoup
from scrapy.selector import Selector
from xxxiao.xxxiao.config import xxxiaoConfig

class Test(unittest.TestCase):

    def testListPage1(self):
        html = urllib2.urlopen(r'http://m.xxxiao.com/').read()
        sel = Selector(text=html);
        print '1', sel.xpath(xxxiaoConfig.list_page_rule1).extract()
        
    def testListPage2(self):
        html = urllib2.urlopen(r'http://m.xxxiao.com/').read()
        sel = Selector(text=html);
        print '2', sel.xpath(xxxiaoConfig.list_page_rule2).extract()

    def testDetailPage1(self):
        html = urllib2.urlopen(r'http://m.xxxiao.com/').read()
        sel = Selector(text=html);
        print '3', sel.xpath(xxxiaoConfig.detail_page_rule1).extract()
        
    def testDetailPage2(self):
        html = urllib2.urlopen(r'http://m.xxxiao.com/39056').read()
        # soup = BeautifulSoup(html, "lxml")
        # print(soup.prettify())
        sel = Selector(text=html);
        print '4', sel.xpath(xxxiaoConfig.detail_page_rule2).extract()    

if __name__ == "__main__":
    unittest.main()