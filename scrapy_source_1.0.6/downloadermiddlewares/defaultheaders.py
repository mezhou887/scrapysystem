"""
给Headers添加默认参数的下载中间件
"""

class DefaultHeadersMiddleware(object):

    def __init__(self, headers):
        self._headers = headers

    # 从DEFAULT_REQUEST_HEADERS中读取到参数并设置到请求的headers中
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get('DEFAULT_REQUEST_HEADERS').items())

    def process_request(self, request, spider):
        for k, v in self._headers:
            request.headers.setdefault(k, v)
