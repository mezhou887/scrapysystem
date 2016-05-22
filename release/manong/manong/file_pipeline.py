# -*- coding: utf-8 -*-

import json
import codecs
import xlwt
from collections import OrderedDict
from manong.items import *
import datetime
import platform
    
class JsonPipeline(object):

    def __init__(self):
        sysstr = platform.system()
        if(sysstr =="Windows"):
            self.file = codecs.open('E:\Crawler\export\manong_'+datetime.datetime.now().strftime('%Y%m%d')+'.json', 'w', encoding='utf-8')
        elif(sysstr == "Darwin"):
            self.file = codecs.open('/Volumes/"VMware Shared Folders"/ScrapyData/manong_'+datetime.datetime.now().strftime('%Y%m%d')+'.json', 'w', encoding='utf-8')
        else:
            self.file = codecs.open('manong_'+datetime.datetime.now().strftime('%Y%m%d')+'.json', 'w', encoding='utf-8')
        

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
        
        
class ExcelPipeline(object):

    def __init__(self):
        self.index = 0;
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.booksheet = self.workbook.add_sheet(u'码农周刊', cell_overwrite_ok=True)

    def process_item(self, item, spider):
        self.booksheet.write(self.index,0,item['name'])
        self.booksheet.write(self.index,1,item['link'])
        sysstr = platform.system()
        if(sysstr =="Windows"):
            self.workbook.save(u'E:\Crawler\export\码农周刊'+datetime.datetime.now().strftime('%Y%m%d')+'.xls')
        elif(sysstr == "Darwin"):
            self.workbook.save(u'/Volumes/"VMware Shared Folders"/ScrapyData/码农周刊'+datetime.datetime.now().strftime('%Y%m%d')+'.xls')
        else:
            self.workbook.save(u'码农周刊'+datetime.datetime.now().strftime('%Y%m%d')+'.xls')
        self.index += 1
        return item

