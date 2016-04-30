# -*- coding:utf-8 -*-
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'

ITEM_PIPELINES = {
    'zhihu.file_pipeline.JsonPipeline': 300,
    'scrapy_mongodb.MongoDBPipeline': 600,
}


#Log Info
LOG_FILE = 'zhihu.log'
LOG_LEVEL = 'INFO'


# http://wiki.jikexueyuan.com/project/scrapy/settings.html
DEPTH_LIMIT=0
DEPTH_PRIORITY=0

CONCURRENT_ITEMS = 1000
CONCURRENT_REQUESTS = 100
CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 0
CONCURRENT_REQUESTS_PER_SPIDER=100

DNSCACHE_ENABLED = True


#Redis Config 使用redis打开，不用redis请注释掉
# https://github.com/rolando/scrapy-redis
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# Mongodb Config
# http://sebdah.github.io/scrapy-mongodb/
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'zhihu_mongo'


# #Email Config
# EXTENSIONS = {
#     'scrapy.extensions.statsmailer.StatsMailer': 500,
# }
# #收件人
# STATSMAILER_RCPTS = ['mezhou887@foxmail.com']
# 
# #发件人
# MAIL_FROM = '1033738034@qq.com'
# MAIL_HOST = 'smtp.qq.com'
# MAIL_PORT = 465
# MAIL_TLS = True
# MAIL_SSL = True
# #邮箱用户
# MAIL_USER = '1033738034@qq.com'
# #邮箱密码
# MAIL_PASS = 'ghyftlmoejsgbeai'


HEADER = {
    "Host": "www.zhihu.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
    "Referer": "https://www.zhihu.com/people/zhoumaoen",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",        
}

COOKIES = {
    'l_n_c': r'1',
    'q_c1': r'c8a06bdb55bb47f59d019039397fc8bc|1461945021000|1461945021000',
    '_xsrf': r'79aa81a264a82846b4ff50e15d41be8d',
    'cap_id': r'"NGIyMTRlOWI4OTQ3NGI0NTk1NTMzYTdkY2Q3NjgwYzk=|1461945021|9e3e33be67dd032b6471dd69dcd214d7bc06d8bf"',
    'l_cap_id': r'"ZmNkOWE5NjgwNDg3NDRhNWJmMDJhMTllYmM2NzAzYzI=|1461945021|d5add13497300c1cc3a3627da1f0d11494c61efb"',
    '__utmc': r'51854390',
    '__utmt': r'1',
    'd_c0': r'"AIAA-FnB2AmPTslifMFvf2Mjh8X9btcryJY=|1461945023"',
    '_zap': r'9a35614e-3815-40eb-9eaa-76757d436911',
    '_za': r'019b7205-d26f-4462-a032-daa57fcb4d74',
    'login': r'"MWMwNTk4NTJiZDMyNDlmMGE4ZDRlMDM0OWMxOTM3MzI=|1461945040|eabb72e69030eea87293d6c6b8c250c043d6f10b"',
    'z_c0': r'Mi4wQUFDQVBJd2JBQUFBZ0FENFdjSFlDUmNBQUFCaEFsVk4wUTlMVndEcGwxUkZyeW8tZ1FDTzFRX3NoaC16dGNxV2Jn|1461945041|925968e6850e335eba2e0f4956376ceeccf1573c',
    'unlock_ticket': r'"QUFDQVBJd2JBQUFYQUFBQVlRSlZUZG1KSTFmeDI2aEliR0xUT2NpdVFCQTduMzg4ODJ0WDdRPT0=|1461945041|8e771951f0f7b7192f1852f1822fffd49cbed413"',
    '__utma': r'51854390.1940704544.1461945023.1461945023.1461945023.1',
    '__utmz': r'51854390.1461945023.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utmv': r'51854390.100-1|2=registration_date=20130524=1^3=entry_date=20130524=1',
    '__utmb': r'51854390.4.10.1461945023',
}


