# -*- coding:utf-8 -*-


BOT_NAME = 'template'

SPIDER_MODULES = ['template.spiders']
NEWSPIDER_MODULE = 'template.spiders'

DOWNLOADER_MIDDLEWARES = {
   # 'misc.middleware.CustomHttpProxyMiddleware': 400,
   # 'misc.middleware.CustomHttpsProxyMiddleware': 400,
    'misc.middleware.CustomUserAgentMiddleware': 400,
}

ITEM_PIPELINES = {
   #'template.pipelines.DoNothingPipeline': 300,
    'template.pipelines.JsonWithEncodingPipeline': 300,
   #'template.pipelines.MongoDBPipeline': 300,    
   #'template.pipelines.RedisPipeline': 300,
}

LOG_FILE = 'template.log'
LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 10
