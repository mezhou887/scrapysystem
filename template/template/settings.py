# -*- coding:utf-8 -*-


BOT_NAME = 'template'

SPIDER_MODULES = ['template.spiders']
NEWSPIDER_MODULE = 'template.spiders'

DOWNLOADER_MIDDLEWARES = {
   # 'misc.middleware.CustomHttpProxyMiddleware': 400,
   # 'misc.middleware.CustomHttpsProxyMiddleware': 400,
   # 'misc.middleware.CustomUserAgentMiddleware': 400,
}

ITEM_PIPELINES = {
   #'template.pipelines.DoNothingPipeline': 300,
  'template.pipelines.ImageDownloadPipeline': 200,
  'template.pipelines.JsonWithEncodingPipeline': 300,
   #'template.pipelines.CsvPipeline': 300,  
   #'template.pipelines.MongoDBPipeline': 300,   
   #'template.pipelines.MySQLPipeline': 300,    
   #'template.pipelines.RedisPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 400,   
}

#Log Info
LOG_FILE = 'template.log'
LOG_LEVEL = 'INFO'
#LOG_LEVEL = 'DEBUG'

#File Store 
IMAGES_STORE = '/Users/zhoumaoen/data/images'

#Redis Config 使用redis打开，不用redis请注释掉
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True

DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 10
