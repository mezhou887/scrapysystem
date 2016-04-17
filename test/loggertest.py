# -*- coding: utf-8 -*-
'''
Created on 2016年4月17日

@author: 周茂恩
'''
import unittest
import logging
import pprint
import urllib2
import json
from bs4 import BeautifulSoup
from misc.log import pp, pu
from jsonpipe import jsonpipe
from jsonpipe import jsonunpipe
import simplejson

class TestLoggerFunctions(unittest.TestCase):
    
    html1 = '''
    <html><head><base href='http://example.com/' /><title>Example website</title></head>
        <body><div id='images'>
                <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
                <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
                <a href='imageA.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
                <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
                <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
            </div></body></html>
    '''  
    json1 = '''
    {
      "@fields": {
          "account": "pyr",
          "args": [],
          "created": 1367480388.013037,
          "filename": "test.py",
          "funcName": "<module>",
          "levelname": "WARNING",
          "levelno": 30,
          "lineno": 18,
          "module": "test",
          "msecs": 13.036966323852539,
          "name": "root",
          "pathname": "test.py",
          "process": 1819,
          "processName": "MainProcess",
          "relativeCreated": 18.002986907958984,
          "thread": 140060726359808,
          "threadName": "MainThread"
      },
      "@message": "TEST",
      "@source_host": "phoenix.spootnik.org",
      "@timestamp": "2013-05-02T09:39:48.013158"
    }
    '''  
    
    def testHtmlSamplele1(self):
        soup = BeautifulSoup(self.html1, "lxml")
        print(soup.prettify())

    def testJsonSample1(self):
        data = [{'a':"A",'b':(2,4),'c':3.0}]  #list对象
        pp.pprint(data)
        pu.pprint(data)
        pprint.pprint(data)
        logging.info(data)
        
    def testJsonSample2(self):   
        html = urllib2.urlopen(r'http://api.douban.com/v2/book/isbn/9787218087351')
        hjson = json.loads(html.read())     
        print hjson
        for line in simplejson.loads(self.json1, object_pairs_hook=simplejson.OrderedDict):
            print line
        
    # pip install jsonpipe    
    def testJsonSample3(self):
        print simplejson.loads('{"a": 1, "b": 2, "c": 3}', object_pairs_hook=simplejson.OrderedDict)
        
        print jsonunpipe(['/\t{}', '/a\t123', '/b\t456'], decoder=simplejson.JSONDecoder(object_pairs_hook=simplejson.OrderedDict))
        for line in jsonpipe({"a": 1, "b": 2}):
            print line    
    
    
if __name__ == "__main__":
    unittest.main() 
