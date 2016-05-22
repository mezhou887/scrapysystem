# -*- coding: utf-8 -*-
import logging
import mysql.connector
from datetime import datetime
from twisted.internet.threads import deferToThread

# conn test: mysql -u root -p   或者 mysql -u mezhou887 -pmezhou887
# CREATE TABLE `meizitu` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `pagelink` varchar(200) DEFAULT NULL,
#   `title` varchar(200) DEFAULT NULL,
#   `name` varchar(200) DEFAULT NULL,
#   `dealdate` datetime DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# pip install mysql-connector-python       
class MySQLPipeline(object): 
    
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()
        self.process_query = "insert into meizitu(pagelink, title, name, dealdate) values(%s, %s, %s, %s);"

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
        logging.debug(self.process_query + now)  
        self.cur.execute(self.process_query, (item['pagelink'], item['title'], item['name'], now))
        self.conn.commit()        

    def spider_closed(self, spider):
        self.cur.close()
        self.conn.close()