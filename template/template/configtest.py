# -*- coding: utf-8 -*-
'''
Created on 2016年4月23日

@author: 周茂恩
'''
import unittest
import urllib2
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from template.template.config import templateConfig

class Test(unittest.TestCase):

    def testDetailPage2(self):
        html = urllib2.urlopen(r'http://m.xxxiao.com/').read()
        soup = BeautifulSoup(html, "lxml")
        print(soup.prettify())
        sel = Selector(text=html);
        print '1', sel.xpath(templateConfig.list_page_rule2).extract()    

if __name__ == "__main__":
    unittest.main()