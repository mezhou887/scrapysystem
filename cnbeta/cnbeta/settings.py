# -*- coding:utf-8 -*-


BOT_NAME = 'cnbeta'

SPIDER_MODULES = ['cnbeta.spiders']
NEWSPIDER_MODULE = 'cnbeta.spiders'

DOWNLOADER_MIDDLEWARES = {
   # 'misc.middleware.CustomHttpProxyMiddleware': 400,
   # 'misc.middleware.CustomHttpsProxyMiddleware': 400,
   # 'misc.middleware.CustomUserAgentMiddleware': 400,
}

ITEM_PIPELINES = {
   #'cnbeta.pipelines.DoNothingPipeline': 300,
  'cnbeta.pipelines.ImageDownloadPipeline': 200,
  'cnbeta.pipelines.JsonWithEncodingPipeline': 300,
   #'cnbeta.pipelines.CsvPipeline': 300,  
   #'cnbeta.pipelines.MongoDBPipeline': 300,   
   #'cnbeta.pipelines.MySQLPipeline': 300,    
   #'cnbeta.pipelines.RedisPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 400,   
}

#Log Info
LOG_FILE = 'cnbeta.log'
LOG_LEVEL = 'INFO'
#LOG_LEVEL = 'DEBUG'

#File Store 
IMAGES_STORE = '/Users/zhoumaoen/data/images'

#Redis Config 使用redis打开，不用redis请注释掉
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True

DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 10
