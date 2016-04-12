# -*- coding:utf-8 -*-


BOT_NAME = 'meizitu'

SPIDER_MODULES = ['meizitu.spiders']
NEWSPIDER_MODULE = 'meizitu.spiders'

DOWNLOADER_MIDDLEWARES = {
   # 'misc.middleware.CustomHttpProxyMiddleware': 400,
   # 'misc.middleware.CustomHttpsProxyMiddleware': 400,
   # 'misc.middleware.CustomUserAgentMiddleware': 400,
}

ITEM_PIPELINES = {
   #'meizitu.pipelines.DoNothingPipeline': 300,
  'meizitu.pipelines.ImageDownloadPipeline': 200,
  'meizitu.pipelines.JsonWithEncodingPipeline': 300,
   #'meizitu.pipelines.CsvPipeline': 300,  
   #'meizitu.pipelines.MongoDBPipeline': 300,   
   #'meizitu.pipelines.MySQLPipeline': 300,    
   #'meizitu.pipelines.RedisPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 400,
}

#Log Info
LOG_FILE = 'meizitu.log'
LOG_LEVEL = 'INFO'
#LOG_LEVEL = 'DEBUG'

#File Store 
IMAGES_STORE = '/Users/zhoumaoen/data/images'

#Redis Config 使用redis打开，不用redis请注释掉
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True

DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 10
