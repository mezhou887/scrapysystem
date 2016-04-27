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
    '__utma':r'51854390.1313781830.1461749937.1461749937.1461749937.1',
    '__utmb':r'51854390.2.10.1461749937',
    '__utmc':r'518543900',
    '__utmt':r'1',
    '__utmv':r'51854390.000--|3=entry_date=20160427=1',
    '__utmz':r'51854390.1461749937.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '_xsrf':r'fadcba2d30a45cf5c90ca721225839d0',
    '_za':r'5c361762-0281-4137-b798-d102760f8406',
    '_zap':r'9ef0ce3b-330b-4ca4-99d6-7117a15926fb',
    'cap_id': r'"ZTkwMDJlMDExZjU0NDAwN2EyYWE1MGRlNjA3YmZiNzE=|1461749930|863e09b2d188cf031b95622891ac21cb77f5cf0c"',
    'd_c0': r'"ADDAJMb31AmPTr7DTvsqvXaXrshcPFCBpNo=|1461690854"',
    'l_cap_id': r'"ODhjYzBmMDQ1MWU3NGM5Yzg2Yzg0NzQzMWJhZjAxNTU=|1461749930|663fca96f65c57a282009bb3432da8b0e3c6ae91"',
    'l_n_c':r'1',
    'login': r'"ZDkyMWM5YmE3NTZkNDJiZmE5MzhjODRmMGZiZjIyOGE=|1461749951|49f18270fcc1ce87d8b8e877d79110e7c258d338"',
    'q_c1':r'873fb5a6eee5428793458e6f0b9513bb|1461749930000|1461749930000',
    'unlock_ticket':r'"QUFDQVBJd2JBQUFYQUFBQVlRSlZUY2VQSUZkbk5LUlZHbHJFZ2JWQTdkelB2Y0JIaVQwVmJRPT0=|1461749951|77d0f0c281edd26869d93d4abae20d6f788c6abe"',
    'z_c0':r'Mi4wQUFDQVBJd2JBQUFBTU1Ba3h2ZlVDUmNBQUFCaEFsVk52eFZJVndCTDZhSWNfTVYyZDZSWFR5MHdXN2hGa29JQl9B|1461749951|903aa0edabeb0940cbbd591fcdaa9041fdeea12e',
}
