# -*- coding: utf-8 -*-

import json
import codecs
from collections import OrderedDict
from luoo.items import *
from scrapy.http import Request
from scrapy.pipelines.files import FilesPipeline
  
    
class JsonPipeline(object):

    def __init__(self):
        self.file = codecs.open('luoo.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
        
class CustomerFilesPipeline(FilesPipeline):
    
    def get_media_requests(self, item, info):
        return [Request(item.get(self.FILES_URLS_FIELD))]    
    
        