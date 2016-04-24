# -*- coding: utf-8 -*-
import logging
import mysql.connector
from datetime import datetime
from twisted.internet.threads import deferToThread
from hashlib import md5

# conn test: mysql -u root -p   或者 mysql -u mezhou887 -pmezhou887

# pip install mysql-connector-python       
class MySQLPipeline(object): 
    
    def __init__(self, conn):
        self.conn = conn
        self.process_query = "insert into TABLENAME(linkmd5id, AAAA, BBBB, CCCC, DDDD, now) values(%s, %s, %s, %s, %s, %s);"

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
        return deferToThread(self._process_item, item, spider)
        
    def _process_item(self, item, spider):  
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        linkmd5id = self._get_linkmd5id(item)
        self.conn.execute("select 1 from TABLENAME where linkmd5id = %s", (linkmd5id))
        ret = self.conn.fetchone()
        if ret:
            logging.debug(self.process_query + now)  
            self.conn.execute(self.process_query, (linkmd5id, item['AAAA'], item['BBB'], item['CCCC'], item['DDDD'], now))
        else:
            logging.debug("the item is already install." + now)  
            
    def _get_linkmd5id(self, item):         
        return md5(item['pagelink']).hexdigest()           

    def spider_closed(self, spider):
        self.conn.commit() 
        self.conn.close()