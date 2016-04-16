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
    'template.file_pipeline.DoNothingPipeline': 100,
    'scrapy.pipelines.images.ImagesPipeline': 200,
    'template.file_pipeline.JsonPipeline': 300,
    'template.file_pipeline.CsvPipeline': 400,
    'template.mysql_pipeline.MySQLPipeline': 500,    
    'template.redis_pipeline.RedisPipeline': 600,   
    'scrapy_mongodb.MongoDBPipeline': 700,
}

#Log Info
LOG_FILE = 'template.log'
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
MONGODB_COLLECTION = 'template_mongo'

#MySQL Config
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapy'
MYSQL_USER = 'mezhou887'
MYSQL_PASSWD = '123456'

DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 10
