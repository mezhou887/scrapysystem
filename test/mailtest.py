# -*- coding: utf-8 -*-
'''
Created on 2016年4月17日

@author: 周茂恩
'''
import unittest
from scrapy.mail import MailSender


class Test(unittest.TestCase):


    def testMail(self):
        mailer = MailSender("smtp.qq.com", '1033738034@qq.com', '1033738034@qq.com', 'ghyftlmoejsgbeai', 465, True, False, False)
        mailer.send("mezhou887@foxmail.com", "scrapy title", "scrapy bodytF")
        print 'send mail success'

if __name__ == "__main__":
    unittest.main()