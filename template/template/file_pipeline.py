# -*- coding: utf-8 -*-

import json
import codecs
import csv
from collections import OrderedDict
from template.items import *
  
    
class DoNothingPipeline(object):
    def process_item(self, item, spider):
        return item
    

class CsvPipeline(object):
    
    def __init__(self):
        self.file = csv.writer(file('template.csv'), 'w', encoding='utf-8')
        
    def spider_opened(self, spider):
        self.file.writerow(spider.itemKyes)

    def process_item(self, item, spider):
        arr = []
        for key in spider.itemKeys:
            arr.append(item[key])
            
        self.writer.writerow(arr)
        return item
        
    def spider_closed(self,spider):
        self.file.close()
        

class JsonPipeline(object):

    def __init__(self):
        self.file = codecs.open('template.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()