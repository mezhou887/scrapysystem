# -*- coding:utf-8 -*-
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

BOT_NAME = 'cnbeta'

SPIDER_MODULES = ['cnbeta.spiders']
NEWSPIDER_MODULE = 'cnbeta.spiders'

DOWNLOADER_MIDDLEWARES = {
   # 'misc.middleware.CustomHttpProxyMiddleware': 100,
   # 'misc.middleware.CustomHttpsProxyMiddleware': 200,
   # 'misc.middleware.CustomUserAgentMiddleware': 300,
}

ITEM_PIPELINES = {
    'cnbeta.file_pipeline.DoNothingPipeline': 100,
    'scrapy.pipelines.images.ImagesPipeline': 200,
    'cnbeta.file_pipeline.JsonPipeline': 300,
    #'cnbeta.mysql_pipeline.MySQLPipeline': 400,    
    #'cnbeta.redis_pipeline.RedisPipeline': 500,   
    #'scrapy_mongodb.MongoDBPipeline': 600,
}

#Log Info
LOG_FILE = 'cnbeta.log'
LOG_LEVEL = 'INFO'
#LOG_LEVEL = 'DEBUG'

#Image Store 
IMAGES_STORE = os.path.join(PROJECT_DIR,'data/images')
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
MONGODB_COLLECTION = 'cnbeta_mongo'

#MySQL Config
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapy'
MYSQL_USER = 'mezhou887'
MYSQL_PASSWD = 'mezhou887'

DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 10
