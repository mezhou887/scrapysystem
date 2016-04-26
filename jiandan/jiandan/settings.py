# -*- coding:utf-8 -*-
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

BOT_NAME = 'jiandan'

SPIDER_MODULES = ['jiandan.spiders']
NEWSPIDER_MODULE = 'jiandan.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None, # 禁用cookies
}


ITEM_PIPELINES = {
    'jiandan.file_pipeline.DoNothingPipeline': 100,
    'scrapy.pipelines.images.ImagesPipeline': 200,
    'jiandan.file_pipeline.JsonPipeline': 300,
}


# Log配置信息
LOG_FILE = 'jiandan.log'
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


# Redis配置信息
# https://github.com/rolando/scrapy-redis
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'


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

CONCURRENT_REQUESTS = 500
CONCURRENT_REQUESTS_PER_DOMAIN = 20

# 下载中间件相关信息
COOKIES_ENABLED = False
USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"
