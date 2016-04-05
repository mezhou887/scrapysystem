# -*- coding:utf-8 -*-


BOT_NAME = 'cnbeta'

SPIDER_MODULES = ['cnbeta.spiders']
NEWSPIDER_MODULE = 'cnbeta.spiders'

DOWNLOADER_MIDDLEWARES = {
   # 'misc.middleware.CustomHttpProxyMiddleware': 400,
   # 'misc.middleware.CustomHttpsProxyMiddleware': 400,
    'misc.middleware.CustomUserAgentMiddleware': 400,
}

ITEM_PIPELINES = {
   #'cnbeta.pipelines.DoNothingPipeline': 300,
    'cnbeta.pipelines.JsonWithEncodingPipeline': 300,
   #'cnbeta.pipelines.MongoDBPipeline': 300,    
   #'cnbeta.pipelines.RedisPipeline': 300,
}

LOG_FILE = 'cnbeta.log'
LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 10
