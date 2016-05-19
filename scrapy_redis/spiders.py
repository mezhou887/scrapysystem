# -*- coding: utf-8 -*-
from scrapy import Spider, signals
from scrapy.exceptions import DontCloseSpider

from . import connection


class RedisMixin(object):
    
    # redis-cli lpush self.name:start_urls http://www.baidu.com
    redis_key = None

    # 初始化redis_key值为self.name:start_urls,然后初始化reids_server
    def setup_redis(self):
        if not self.redis_key:
            self.redis_key = '%s:start_urls' % self.name

        self.server = connection.from_settings(self.crawler.settings)
        # 将事件与回调函数关联起来，共12个信号
        self.crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)
        self.crawler.signals.connect(self.item_scraped, signal=signals.item_scraped)
        self.log("Reading URLs from redis list '%s'" % self.redis_key)

    def next_request(self):
        use_set = self.settings.getbool('REDIS_SET')

        if use_set:
            url = self.server.spop(self.redis_key)
        else:
            url = self.server.lpop(self.redis_key)

        if url:
            return self.make_requests_from_url(url)

    
    def schedule_next_request(self):
        req = self.next_request()
        if req:
            self.crawler.engine.crawl(req, spider=self)

    # 当spider进入空闲(idle)状态时, 发送该信号去抓取下一个request
    def spider_idle(self):
        self.schedule_next_request()
        raise DontCloseSpider

    # 当item被爬取，并完成全部ItemPipeline后, 发送该信号去抓取下一个request
    def item_scraped(self, *args, **kwargs):
        self.schedule_next_request()


class RedisSpider(RedisMixin, Spider):

    def _set_crawler(self, crawler):
        super(RedisSpider, self)._set_crawler(crawler)
        self.setup_redis()
