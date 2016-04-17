# -*- coding: utf-8 -*-
'''
Created on 2016年4月8日

@author: 周茂恩
'''
import unittest
from test.xpathtest import TestXpathFunctions
from test.regextest import TestRegexFunctions
from test.loggertest import TestLoggerFunctions
from test.loggertest import TestMailFunctions

def suite_use_test_loader():
    test_cases = (TestXpathFunctions, TestLoggerFunctions, TestMailFunctions, TestRegexFunctions)
    suite = unittest.TestSuite()
    for test_case in test_cases:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest='suite_use_test_loader')