# -*- coding: utf-8 -*-
'''
Created on 2016年4月21日

@author: 周茂恩
'''

class templateConfig():    
    list_page_rule1='//div[@class="tags"]/span/a/@href'
    list_page_rule2='//div[@class="navigation"]/div[@id="wp_page_numbers"]/ul/li/a[contains(text(), "下一页")]/@href'
    detail_page_rule1='//div[@class="inWrap"]/ul/li/div/div/a/@href'

