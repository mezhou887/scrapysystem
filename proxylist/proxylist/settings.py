# -*- coding:utf-8 -*-
import platform

PROJECT_DIR = "E:/Crawler/export/" if platform.system() == 'Windows' else "/Volumes/VMware Shared Folders/ScrapyData/"

BOT_NAME = 'proxylist'

SPIDER_MODULES = ['proxylist.spiders']
NEWSPIDER_MODULE = 'proxylist.spiders'


ITEM_PIPELINES = {
    'proxylist.file_pipeline.DoNothingPipeline': 100,
    'proxylist.file_pipeline.JsonPipeline': 300,
    'proxylist.file_pipeline.ProxyPipeline': 400,
}

#Log Info
LOG_FILE = 'proxylist.log'
LOG_LEVEL = 'INFO'

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
