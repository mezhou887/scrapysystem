# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import os
import requests
import logging
from twisted.enterprise import adbapi
from datetime import datetime
from template import settings  #这个错误是eclipse自己的编译器错误，不用管
from collections import OrderedDict
from template.items import *
import MySQLdb
import MySQLdb.cursors


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
        self.file = codecs.open('template.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


# sudo ln -s /usr/local/mysql/bin/* /usr/bin
# pip install MySQL-python    
# sudo ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib
# sudo ln -s /usr/local/mysql/lib /usr/local/mysql/lib/mysql    
class MySQLPipeline(object): 
    
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode= True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)  
        
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_insert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d   
        
    def _do_insert(self, conn, item, spider):
        sql = "insert into TABLENAME() values(%s, %s, %s, %s)"
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        ret = conn.fetchone()
        if ret:
            conn.execute(sql, (item['AAAA'], item['BBB'], item['CCCC'], item['DDDD'], now))
        print now
        
    def _handle_error(self, failure, item, spider):
        logging.error(failure)    
