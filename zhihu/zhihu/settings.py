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


# 设置广度优先算法
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'


# # http://wiki.jikexueyuan.com/project/scrapy/settings.html
# DEPTH_LIMIT=0
# DEPTH_PRIORITY=0
# 
# CONCURRENT_ITEMS = 1000
# CONCURRENT_REQUESTS = 100
# CONCURRENT_REQUESTS_PER_DOMAIN = 100
# CONCURRENT_REQUESTS_PER_IP = 0
# CONCURRENT_REQUESTS_PER_SPIDER=100
# 
# DNSCACHE_ENABLED = True


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
    "Referer": "https://www.zhihu.com/people/raymond-wang",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",        
}

COOKIES = {
    'l_n_c': r'1',
    'q_c1': r'9b1dfbcc56c84b00897b1a2d717d82e6|1462089427000|1462089427000',
    '_xsrf': r'ebba027061cb11db54d768f2a83595ed',
    'cap_id': r'"MjBkNzM4MTlmMTU3NGNmYTkzZTFiODZmN2NiNjYyYmY=|1462089427|3f2b0808a97fbea84c8ead10c37ec2693911d0a5"',
    'l_cap_id': r'"Y2FiMTVlZDU2NTdkNDFjZDhlYWI4YzZkMmFlY2M3NDI=|1462089427|58c6c11493c212921773a3ae38843ad2fcdb5090"',
    'n_c': r'1',
    '__utmc': r'51854390',
    '__utmt': r'1',
    'd_c0': r'"AHDAXzbo2gmPTiSRNIOiP-5rgoL6aBotKPM=|1462089428"',
    '_za': r'86fa36c5-0d6d-4336-89c4-32782a65d45c',
    '_zap': r'542f17a8-d8af-44df-b2d8-272bbf516ff9',
    'login': r'"OGE2MDAwYmIxZTFlNDY3Y2FiYmI4Mjc4NWJkMmRjMzM=|1462089445|afbda51c8770203e851260de2f9e220aaefa6f0f"',
    'z_c0': r'Mi4wQUFDQVBJd2JBQUFBY01CZk51amFDUmNBQUFCaEFsVk41VU5OVndCZjRiOUJTZC1FRDlGNjZXWVFVSVpjOVI4Ylpn|1462089445|bc297707b949771bfc7a0c42de5bda49c41c0905',
    'unlock_ticket': r'"QUFDQVBJd2JBQUFYQUFBQVlRSlZUZTI5SlZkN3NSZlNQclVOc20tNjQ2bTJaUnUwUkRNNG1RPT0=|1462089445|d02b2e76dd6054bac983a6137005b4d2ad5c4664"',
    '__utma': r'51854390.647038316.1462089430.1462089430.1462089430.1',
    '__utmz': r'51854390.1462089430.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utmv': r'51854390.100-1|2=registration_date=20130524=1^3=entry_date=20130524=1',
    '__utmb': r'51854390.4.10.1462089430',
}



