"""
用于HTTP auth处的下载中间件
"""

from w3lib.http import basic_auth_header

from scrapy import signals


class HttpAuthMiddleware(object):
    """
        给HTTP Authorization header中增加http_user和http_pass属性的
    """

    @classmethod
    def from_crawler(cls, crawler):
        o = cls()
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o
    
    # 需要在爬虫中添加http_user和http_pass这两个属性
    def spider_opened(self, spider):
        usr = getattr(spider, 'http_user', '') 
        pwd = getattr(spider, 'http_pass', '')
        if usr or pwd:
            self.auth = basic_auth_header(usr, pwd)

    def process_request(self, request, spider):
        auth = getattr(self, 'auth', None)
        if auth and 'Authorization' not in request.headers:
            request.headers['Authorization'] = auth
