# -*- coding:utf-8 -*-
'''
Created on 2016年4月28日

@author: Administrator
'''
import pytesseract

from PIL import Image
image = Image.open('D:\\captcha.png')
vcode = pytesseract.image_to_string(image)
print (vcode)