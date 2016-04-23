# -*- coding:utf-8 -*-
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

BOT_NAME = 'xxxiao'

SPIDER_MODULES = ['xxxiao.spiders']
NEWSPIDER_MODULE = 'xxxiao.spiders'

ITEM_PIPELINES = {
    'xxxiao.file_pipeline.DoNothingPipeline': 100,
    'scrapy.pipelines.images.ImagesPipeline': 200,
    'xxxiao.file_pipeline.JsonPipeline': 300,
    'xxxiao.redis_pipeline.RedisPipeline': 500,   
}

# Log Info
LOG_FILE = 'xxxiao.log'
LOG_LEVEL = 'INFO'

#Image Store 
IMAGES_STORE = os.path.join(PROJECT_DIR,'data/images')
IMAGES_EXPIRES = 30
IMAGES_THUMBS = {
    'small': (50, 50),
    'mid': (160, 160),
    'big': (270, 270),
}

#Redis Config 使用redis打开，不用redis请注释掉
# https://github.com/rolando/scrapy-redis
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

#Email Config
EXTENSIONS = {
    'scrapy.extensions.statsmailer.StatsMailer': 500,
}

#Item Exporters
FEED_EXPORTERS_BASE = {
    'json': 'scrapy.exporters.JsonItemExporter',
    'jsonlines': 'scrapy.exporters.JsonLinesItemExporter',
    'csv': 'scrapy.exporters.CsvItemExporter',
    'xml': 'scrapy.exporters.XmlItemExporter',
    'marshal': 'scrapy.exporters.MarshalItemExporter',
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
