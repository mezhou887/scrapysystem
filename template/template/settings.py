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
   #'meizitu.pipelines.DoNothingPipeline': 300,
  'meizitu.pipelines.ImageDownloadPipeline': 200,
    'meizitu.pipelines.JsonWithEncodingPipeline': 300,
   #'meizitu.pipelines.CsvPipeline': 300,  
   #'meizitu.pipelines.MongoDBPipeline': 300,   
   #'meizitu.pipelines.MySQLPipeline': 300,    
   #'meizitu.pipelines.RedisPipeline': 300,
}

LOG_FILE = 'template.log'
LOG_LEVEL = 'INFO'
#LOG_LEVEL = 'DEBUG'

IMAGES_STORE = '/Users/zhoumaoen/data/images'
DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 10
