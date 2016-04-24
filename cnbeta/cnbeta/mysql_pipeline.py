# -*- coding: utf-8 -*-
import logging
import mysql.connector
from datetime import datetime
from hashlib import md5

# conn test: mysql -u root -p   或者 mysql -u mezhou887 -pmezhou887

# pip install mysql-connector-python       
class MySQLPipeline(object): 
    
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()
        self.process_query = "insert into cnbeta(linkmd5id, pagelink, title, now) values(%s, %s, %s, %s);"

    @classmethod
    def from_settings(cls, settings):
        config={'host':settings.get('MYSQL_HOST',  'localhost'),  
                'user':settings.get('MYSQL_USER', 'mezhou887'),  
                'password':settings.get('MYSQL_PASSWD', 'mezhou887'),  
                'port':3306,
                'database':settings.get('MYSQL_DBNAME', 'scrapy'),  
                'charset':'utf8' 
        }
        conn = mysql.connector.connect(**config)
        return cls(conn);
    
    def process_item(self, item, spider):
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        linkmd5id = self._get_linkmd5id(item)
        logging.debug(self.process_query + now)  
        self.cur.execute(self.process_query, (linkmd5id, item['pagelink'], item['title'][0], now))
        self.conn.commit()
            
    def _get_linkmd5id(self, item):         
        return md5(item['pagelink']).hexdigest()           

    def spider_closed(self, spider):
        self.cur.close()
        self.conn.close()