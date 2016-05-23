# -*- coding: utf-8 -*-

import json
import codecs
from collections import OrderedDict
from xxxiao.items import *
import datetime
import platform
  
    
class JsonPipeline(object):

    def __init__(self):
        sysstr = platform.system()
        if(sysstr =="Windows"):
            self.file = codecs.open('E:/Crawler/export/xxxiao_'+datetime.datetime.now().strftime('%Y%m%d')+'.json', 'w', encoding='utf-8')
        elif(sysstr == "Darwin"):
            self.file = codecs.open('/Users/mezhou887/Downloads/ScrapyData/xxxiao_'+datetime.datetime.now().strftime('%Y%m%d')+'.json', 'w', encoding='utf-8')
        else:
            self.file = codecs.open('xxxiao_'+datetime.datetime.now().strftime('%Y%m%d')+'.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()