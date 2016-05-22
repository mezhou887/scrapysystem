# -*- coding: utf-8 -*-

import json
import codecs
from collections import OrderedDict
from jiandan.items import *
  
    
class DoNothingPipeline(object):
    def process_item(self, item, spider):
        return item
        

class JsonPipeline(object):

    def __init__(self):
        self.file = codecs.open('jiandan.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()