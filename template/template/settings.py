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
#    'scrapy.pipelines.files.FilesPipeline': 200,    
    'template.file_pipeline.JsonPipeline': 300,
    #'template.mysql_pipeline.MySQLPipeline': 400,    
    #'scrapy_redis.pipelines.RedisPipeline': 500,   
    #'scrapy_mongodb.MongoDBPipeline': 600,
}


# Log配置信息
LOG_FILE = 'template.log'
LOG_LEVEL = 'INFO' #'DEBUG'


# 图片存储信息
IMAGES_STORE = os.path.join(PROJECT_DIR,'data/images')
IMAGES_EXPIRES = 30
IMAGES_THUMBS = {
    'small': (50, 50),
    'middle': (160, 160),
    'big': (270, 270),
}
IMAGES_MIN_HEIGHT = 10
IMAGES_MIN_WIDTH = 10


# 文件存储信息 由于文件和图片都是存储到full路径下的，所以没必要保留多个
#FILES_STORE = os.path.join(PROJECT_DIR,'data/files')
#FILES_EXPIRES = 30


# Redis配置信息
# https://github.com/rolando/scrapy-redis
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'


# Mongodb配置信息
# http://sebdah.github.io/scrapy-mongodb/
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'template_mongo'
MONGODB_UNIQUE_KEY = 'pagelink'  # 将pageLink作为主键
MONGODB_ADD_TIMESTAMP = True     # 增加时间值


# MySQL配置信息
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapy'
MYSQL_USER = 'mezhou887'
MYSQL_PASSWD = 'mezhou887'


# Email配置信息
EXTENSIONS = {
    'scrapy.extensions.statsmailer.StatsMailer': 500,
}
# 收件人
STATSMAILER_RCPTS = ['mezhou887@foxmail.com']
# 发件人
MAIL_FROM = '1033738034@qq.com'
MAIL_HOST = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_TLS = True
MAIL_SSL = True
# 邮箱用户
MAIL_USER = '1033738034@qq.com'
# 邮箱密码
MAIL_PASS = 'ghyftlmoejsgbeai'


# 下载配置信息
DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 10
