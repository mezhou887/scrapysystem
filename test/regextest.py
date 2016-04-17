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
            
    def testSample3(self):
        text = '123pythontab123AAA2BBB'
        m = re.search(r"\d+", text)
        if m: 
            print m.group(0)
        else:
            print 'not match'
            
    def testSample4(self):
        text = '123pythontab1423AAA2BBB'
        p = re.compile("\d+")
        print p.findall(text)
        print re.findall(r'[a-zA-Z]+', text)

if __name__ == "__main__":
    unittest.main()