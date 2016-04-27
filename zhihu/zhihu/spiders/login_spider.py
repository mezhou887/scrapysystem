# -*- coding: utf-8 -*-
'''
Created on 2016年4月27日
@author: 周茂恩
'''

import time
from scrapy.spiders.crawl import CrawlSpider
from scrapy.http.request.form import FormRequest
from selenium import webdriver

from zhihu.settings import HEADER, COOKIES

host = 'http://www.zhihu.com'
home = 'http://www.zhihu.com/people/raymond-wang/about'

class ZhihuLoginSpider(CrawlSpider):
    name = 'zhihu_login'
    allowed_domains = ['zhihu.com']
    start_urls = [home]
    
    def __init__(self):
        self.headers = HEADER
        self.cookies = COOKIES
    
    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield FormRequest(url, meta = {'cookiejar': i},
                headers = self.headers,
                cookies = self.cookies,
                callback = self.parse_item,
                errback = self.parse_error)
    
    def parse_item(self, response):
        print response.url
        if "Raymond Wang" in response.body:
            print 'successs'
        else:
            print 'fail'
    
    def parse_error(self):
        print 'error'
        
    def getcookies(self):
        driver = webdriver.Firefox()
        driver.get(host)
        
        time.sleep(10)
        driver.maximize_window() # 浏览器全屏显示
        
        #通过用户名密码登陆
        driver.find_element_by_name("account").send_keys("mezhou887@foxmail.com")
        driver.find_element_by_name("password").send_keys("")    
        
        time.sleep(10) # 休眠10s钟，等待用户输入验证码
        
        # 勾选保存密码， 点击登录按钮
        driver.find_element_by_name("remember_me").click()
        driver.find_element_by_xpath('//button[@class="sign-button submit"]').click()
        time.sleep(10)
        driver.get(home)
        
        cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
        cookiestr = ';'.join(item for item in cookie)
        driver.close()
        
        # print cookiestr
        return cookiestr