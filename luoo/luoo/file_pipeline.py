# -*- coding: utf-8 -*-

import json
import os
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
    
    def __init__(self, store_uri, download_func=None):
        self.base = store_uri
        super(CustomerFilesPipeline, self).__init__(store_uri, download_func)    
        
    def get_media_requests(self, item, info):
        self.title = self.base + '/' + item['title']
        self.name = item['musicname']
        return [Request(item.get(self.FILES_URLS_FIELD))] 
    
    def file_path(self, request, response=None, info=None):
        folder = self.title
        if not os.path.exists(folder):
            os.mkdir(folder)        
        
        media_ext = os.path.splitext(request.url)[1]
        return '%s/%s%s' % (folder, self.name, media_ext)   
    
        