# -*- coding:utf-8 -*-
# cat xxxiao.json | jq '.[] | {message: .title, name: .pagelink}'
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

BOT_NAME = 'xxxiao'

SPIDER_MODULES = ['xxxiao.spiders']
NEWSPIDER_MODULE = 'xxxiao.spiders'


ITEM_PIPELINES = {
    'xxxiao.file_pipeline.DoNothingPipeline': 100,
    'scrapy.pipelines.images.ImagesPipeline': 200,
#    'scrapy.pipelines.files.FilesPipeline': 200,
    'xxxiao.file_pipeline.JsonPipeline': 300,
    'scrapy_mongodb.MongoDBPipeline': 600,
}


# Log配置信息
LOG_FILE = 'xxxiao.log'
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


# Mongodb配置信息
# http://sebdah.github.io/scrapy-mongodb/
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'xxxiao_mongo'
MONGODB_UNIQUE_KEY = 'pagelink'  # 将pageLink作为主键
MONGODB_ADD_TIMESTAMP = True     # 增加时间值

#Email配置信息
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


# 下载配置信息
DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 10
