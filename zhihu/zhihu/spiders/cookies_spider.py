# -*- coding: utf-8 -*-
'''
Created on 2016年4月27日

@author: 周茂恩
'''

from selenium import webdriver
import time

def getcookies(url, next_url):
    
    driver = webdriver.Firefox()
    driver.get(url)
    
    time.sleep(3)
    driver.maximize_window() # 浏览器全屏显示
    
    #通过用户名密码登陆
    driver.find_element_by_name("account").send_keys("mezhou887@foxmail.com")
    driver.find_element_by_name("password").send_keys("")    
    
    time.sleep(10) # 休眠10s钟，等待用户输入验证码
    
    # 勾选保存密码， 点击登录按钮
    driver.find_element_by_name("remember_me").click()
    driver.find_element_by_xpath('//button[@class="sign-button submit"]').click()
    time.sleep(5)
    driver.get(next_url)

    print 'COOKIES = {'
    for item in driver.get_cookies():
        print "    '"+item["name"]+"': r'"+item["value"]+"',"  
    print '}'
    
    time.sleep(2)
    driver.close()
 
if __name__ == "__main__":
    getcookies("http://www.zhihu.com/#signin", "http://www.zhihu.com/people/raymond-wang/about")