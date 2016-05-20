# -*- coding: utf-8 -*-

import json
import codecs
import xlwt
from collections import OrderedDict
from manong.items import *
import datetime
    
class JsonPipeline(object):

    def __init__(self):
        self.file = codecs.open('manong.json', 'w', encoding='utf-8')

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
        self.workbook.save(u'码农周刊'+datetime.datetime.now().strftime('%Y%m%d')+'.xls')
        self.index += 1
        return item

