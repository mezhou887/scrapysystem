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

    sample1 = '''
    <html>
        <head>
            <base href='http://example.com/' />
            <title>Example website</title>
        </head>
        <body>
            <div id='images'>
                <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
                <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
                <a href='imageA.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
                <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
                <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
            </div>
        </body>
    </html>
    '''    

    def testSample1(self):
        sel = Selector(text=self.sample1);
        print '1.', sel.css('img').xpath('@src').extract()
        print '2.', sel.css('base::attr(href)').extract()
        print '3.', sel.css('a[href*=image]::attr(href)').extract()
        print '4.', sel.css('a[href*=image] img::attr(src)').extract()
    
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