# -*- coding:utf-8 -*-
import os
import platform

PROJECT_DIR = "E:/Crawler/export/" if platform.system() == 'Windows' else "/Volumes/VMware Shared Folders/ScrapyData/"

BOT_NAME = 'woaidu'

SPIDER_MODULES = ['woaidu.spiders']
NEWSPIDER_MODULE = 'woaidu.spiders'


ITEM_PIPELINES = {
    'woaidu.file_pipeline.DoNothingPipeline': 100,
    'scrapy.pipelines.images.ImagesPipeline': 200,
    'woaidu.file_pipeline.JsonPipeline': 300,
}


# Log配置信息
LOG_FILE = 'woaidu.log'
LOG_LEVEL = 'INFO' #'DEBUG'


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

CONCURRENT_REQUESTS = 500
CONCURRENT_REQUESTS_PER_DOMAIN = 20