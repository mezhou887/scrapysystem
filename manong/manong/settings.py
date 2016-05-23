# -*- coding:utf-8 -*-
import os
import platform

PROJECT_DIR = "E:/Crawler/export/" if platform.system() == 'Windows' else "/Volumes/VMware Shared Folders/ScrapyData/"

BOT_NAME = 'manong'

SPIDER_MODULES = ['manong.spiders']
NEWSPIDER_MODULE = 'manong.spiders'


ITEM_PIPELINES = {
    'manong.file_pipeline.JsonPipeline': 300,
    'manong.file_pipeline.ExcelPipeline': 400,
}


# Log配置信息
LOG_FILE = 'manong.log'
LOG_LEVEL = 'INFO' #'DEBUG'


CONCURRENT_REQUESTS = 500
CONCURRENT_REQUESTS_PER_DOMAIN = 20

# 下载中间件相关信息
USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"
