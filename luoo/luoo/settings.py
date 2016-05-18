# -*- coding:utf-8 -*-
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

BOT_NAME = 'luoo'

SPIDER_MODULES = ['luoo.spiders']
NEWSPIDER_MODULE = 'luoo.spiders'


ITEM_PIPELINES = {
    'luoo.file_pipeline.JsonPipeline': 300,
}


# Log配置信息
LOG_FILE = 'luoo.log'
LOG_LEVEL = 'INFO' #'DEBUG'


CONCURRENT_REQUESTS = 500
CONCURRENT_REQUESTS_PER_DOMAIN = 20

# 下载中间件相关信息
COOKIES_ENABLED = False
USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"
