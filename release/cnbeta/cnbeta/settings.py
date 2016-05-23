# -*- coding:utf-8 -*-
import platform

PROJECT_DIR = "E:/Crawler/export/" if platform.system() == 'Windows' else "/Users/mezhou887/Downloads/ScrapyData/"

BOT_NAME = 'cnbeta'

SPIDER_MODULES = ['cnbeta.spiders']
NEWSPIDER_MODULE = 'cnbeta.spiders'

ITEM_PIPELINES = {
    'cnbeta.file_pipeline.DoNothingPipeline': 100,
    'cnbeta.file_pipeline.JsonPipeline': 300,
    'cnbeta.mysql_pipeline.MySQLPipeline': 400,    
}

#Log Info
LOG_FILE = 'cnbeta.log'
LOG_LEVEL = 'INFO'

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

CONCURRENT_REQUESTS = 500
CONCURRENT_REQUESTS_PER_DOMAIN = 20
