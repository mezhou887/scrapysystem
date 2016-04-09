# -*- coding: utf-8 -*-
'''
Created on 2016年4月7日

@author: 周茂恩
'''
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import unittest
import requests

class TestCssFunctions(unittest.TestCase):

    def testSample1(self):
        pass
    
    def testSample2(self):
        str = 'http://doc.scrapy.org/en/latest/_static/selectors-sample1.html'
        r = requests.get(str)
        response = HtmlResponse(url=str, body=r.content)
        print '1.', Selector(response=response).css('title::text').extract()   
        
    def testSample3(self):
        str = 'http://www.cnbeta.com/'        
        r = requests.get(str)
        response = HtmlResponse(url=str, body=r.content)
        print '2.', Selector(response=response).css('title::text').extract()[0]   
        print '3.', Selector(response=response).css('title::text').extract()[0].encode('utf-8')     

if __name__ == "__main__":
    unittest.main()