# -*- coding: utf-8 -*-

import json
import codecs
from collections import OrderedDict
from proxylist.items import *
  
    
class DoNothingPipeline(object):
    def process_item(self, item, spider):
        return item
        

class JsonPipeline(object):

    def __init__(self):
        self.file = codecs.open('proxylist.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class ProxyPipeline(object):

    def __init__(self):
        self.file = codecs.open('proxy.py', 'w', encoding='utf-8')
        self.file.write('HTTPPROXIES = [ \n')

    def process_item(self, item, spider):
        line = '{"ip_port": "'+item['ip'][0]+':' + item['port'][0]+ '"}, \n'
        self.file.write(line)
        return item
    
    def spider_closed(self, spider):
        self.file.write(']')
        self.file.close()    