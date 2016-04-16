# -*- coding: utf-8 -*-
import logging
import MySQLdb
from datetime import datetime
from twisted.internet.threads import deferToThread

# pip install MySQL-python       
class MySQLPipeline(object): 
    
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()
        self.process_query = "insert into TABLENAME(AAAA, BBBB, CCCC, DDDD, now) values(%s, %s, %s, %s);"
        self.test_query = "select count(1) from TABLENAME;"

    @classmethod
    def from_settings(cls, settings):
        host = settings.get('MYSQL_HOST',  'localhost')
        db = settings.get('MYSQL_DBNAME', 'scrapy')
        user = settings.get('MYSQL_USER', 'mezhou887')
        passwd = settings.get('MYSQL_PASSWD', 'mezhou887')
        
        conn = MySQLdb.connect(host, user, passwd, db, charset='utf8', use_unicode=False)
        return cls(conn);
    
    def process_item(self, item, spider):
        return deferToThread(self._process_item, item, spider)
        
    def _process_item(self, item, spider):  
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        logging.debug(self.process_query + now)  
        self.cur.execute(self.process_query, (item['AAAA'], item['BBB'], item['CCCC'], item['DDDD'], now))
        self.conn.commit()        
