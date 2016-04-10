# -*- coding: utf-8 -*-
'''
Created on 2016年4月7日

@author: 周茂恩
'''
import unittest
import re

# link1: http://blog.jobbole.com/74844/

class TestRegexFunctions(unittest.TestCase):

    def testSample1(self):
        print re.match("c", "abcdef")
        
    def testSample2(self):
        pattern = re.compile(r'world')
        match = pattern.search('hello world!')
        if match:
            print match.group()

if __name__ == "__main__":
    unittest.main()