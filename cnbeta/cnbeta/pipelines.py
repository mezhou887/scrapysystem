# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import os
import requests
from cnbeta import settings
from collections import OrderedDict
from cnbeta.items import *


class ImageDownloadPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' in item:
            images = []
            dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            for image_url in item['image_urls']:
                us = image_url.split('/')[3:]
                image_file_name = '_'.join(us)
                file_path = '%s/%s' % (dir_path, image_file_name)
                images.append(file_path)
                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True)
                    for block in response.iter_content(1024):
                        if not block:
                            break

                        handle.write(block)

            item['images'] = images
        return item
    
    
class DoNothingPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('cnbeta.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class MongoDBPipeline(object):
    def process_item(self, item, spider):
        return item


class CsvPipeline(object):
    def process_item(self, item, spider):
        return item  

    
class MySQLPipeline(object): 
    def process_item(self, item, spider):
        return item     
    

class RedisPipeline(object):
    def process_item(self, item, spider):
        return item

