# -*- coding:utf-8 -*-
import os
import platform

PROJECT_DIR = "E:/Crawler/export/" if platform.system() == 'Windows' else "/Users/mezhou887/Downloads/ScrapyData/"

BOT_NAME = 'meizitu'

SPIDER_MODULES = ['meizitu.spiders']
NEWSPIDER_MODULE = 'meizitu.spiders'

DOWNLOADER_MIDDLEWARES = {
   # 'misc.middleware.CustomHttpProxyMiddleware': 100,
   # 'misc.middleware.CustomHttpsProxyMiddleware': 200,
   # 'misc.middleware.CustomUserAgentMiddleware': 300,
}

ITEM_PIPELINES = {
    'meizitu.file_pipeline.DoNothingPipeline': 100,
    'scrapy.pipelines.images.ImagesPipeline': 200,
    'meizitu.file_pipeline.JsonPipeline': 300,
    'meizitu.mysql_pipeline.MySQLPipeline': 400,    
    #'scrapy_redis.pipelines.RedisPipeline': 500,   
    #'scrapy_mongodb.MongoDBPipeline': 600,
}

#Log Info
LOG_FILE = 'meizitu.log'
LOG_LEVEL = 'INFO'
#LOG_LEVEL = 'DEBUG'

#Image Store 
IMAGES_STORE = os.path.join(PROJECT_DIR,'meizitu/data/images')
IMAGES_EXPIRES = 30
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}

#Redis Config 使用redis打开，不用redis请注释掉
# https://github.com/rolando/scrapy-redis
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# Mongodb Config
# http://sebdah.github.io/scrapy-mongodb/
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'meizitu_mongo'

#MySQL Config
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapy'
MYSQL_USER = 'mezhou887'
MYSQL_PASSWD = 'mezhou887'

#Email Config
EXTENSIONS = {
    'scrapy.extensions.statsmailer.StatsMailer': 500,
}
#收件人
STATSMAILER_RCPTS = ['mezhou887@foxmail.com']

#发件人
MAIL_FROM = '1033738034@qq.com'
MAIL_HOST = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_TLS = True
MAIL_SSL = True
#邮箱用户
MAIL_USER = '1033738034@qq.com'
#邮箱密码
MAIL_PASS = 'ghyftlmoejsgbeai'

DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 10
