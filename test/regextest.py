# -*- coding: utf-8 -*-
'''
Created on 2016年4月7日

@author: 周茂恩
'''
import unittest
import re

class TestRegexFunctions(unittest.TestCase):

    def testSample1(self):
        print re.match("c", "abcdef")

if __name__ == "__main__":
    unittest.main()