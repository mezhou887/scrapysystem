# -*- coding:utf-8 -*-
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

BOT_NAME = 'template'

SPIDER_MODULES = ['template.spiders']
NEWSPIDER_MODULE = 'template.spiders'

DOWNLOADER_MIDDLEWARES = {
   # 'misc.middleware.CustomHttpProxyMiddleware': 100,
   # 'misc.middleware.CustomHttpsProxyMiddleware': 200,
   # 'misc.middleware.CustomUserAgentMiddleware': 300,
}

ITEM_PIPELINES = {
    'template.pipelines.DoNothingPipeline': 100,
    'template.pipelines.ImageDownloadPipeline': 200,
    'template.pipelines.JsonWithEncodingPipeline': 300,
    'template.pipelines.MySQLPipeline': 400,    
    'scrapy_redis.pipelines.RedisPipeline': 500,   
    'scrapy_mongodb.MongoDBPipeline': 600,
}

#Log Info
LOG_FILE = 'template.log'
LOG_LEVEL = 'INFO'
#LOG_LEVEL = 'DEBUG'

#Image Store 
IMAGES_STORE = os.path.join(PROJECT_DIR,'data/images')

#Redis Config 使用redis打开，不用redis请注释掉
# https://github.com/rolando/scrapy-redis
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# Mongodb Config
# https://github.com/sebdah/scrapy-mongodb
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'template_mongo'

#MySQL Config
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapy'
MYSQL_USER = 'mezhou887'
MYSQL_PASSWD = '123456'

DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 10
