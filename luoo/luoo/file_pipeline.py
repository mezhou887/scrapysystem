# -*- coding: utf-8 -*-

import json
import os
import codecs
from collections import OrderedDict
from luoo.items import *
from scrapy.http import Request
from scrapy.pipelines.files import FilesPipeline
import datetime
import platform
  
    
class JsonPipeline(object):

    def __init__(self):
        sysstr = platform.system()
        if(sysstr =="Windows"):
            self.file = codecs.open('E:/Crawler/export/luoo_'+datetime.datetime.now().strftime('%Y%m%d')+'.json', 'w', encoding='utf-8')
        elif(sysstr == "Darwin"):
            self.file = codecs.open('/Volumes/"VMware Shared Folders"/ScrapyData/luoo_'+datetime.datetime.now().strftime('%Y%m%d')+'.json', 'w', encoding='utf-8')
        else:
            self.file = codecs.open('luoo_'+datetime.datetime.now().strftime('%Y%m%d')+'.json', 'w', encoding='utf-8')        
        

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
        
class CustomerFilesPipeline(FilesPipeline):
    
    def __init__(self, store_uri, download_func=None):
        super(CustomerFilesPipeline, self).__init__(store_uri, download_func)    
        
    def get_media_requests(self, item, info):
        self.title = item['title']
        self.name = item['musicname']
        return [Request(item.get(self.FILES_URLS_FIELD))] 
    
    def file_path(self, request, response=None, info=None):
        if not isinstance(request, Request):
            url = request
        else:
            url = request.url
 
        if not hasattr(self.file_key, '_base'):
            return self.file_key(url)
         
        folder = self.title
        if not os.path.exists(folder):
            os.mkdir(folder)        
         
        media_guid = self.name
        media_ext = os.path.splitext(url)[1]
        return '%s/%s%s' % (folder, media_guid, media_ext)   
    
        