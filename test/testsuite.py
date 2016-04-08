# -*- coding: utf-8 -*-
'''
Created on 2016年4月8日

@author: 周茂恩
'''
import unittest
from test.xpathtest import TestXpathFunctions
from test.csstest import TestCssFunctions
from test.regextest import TestRegexFunctions

def suite_use_test_loader():
    test_cases = (TestXpathFunctions, TestCssFunctions, TestRegexFunctions)
    suite = unittest.TestSuite()
    for test_case in test_cases:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest='suite_use_test_loader')