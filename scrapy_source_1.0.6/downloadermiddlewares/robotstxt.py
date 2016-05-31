"""
robots封禁处理，默认不使用该中间件，使用时需启用
"""

import logging

from six.moves.urllib import robotparser

from scrapy.exceptions import NotConfigured, IgnoreRequest
from scrapy.http import Request
from scrapy.utils.httpobj import urlparse_cached
from scrapy.utils.log import failure_to_exc_info

logger = logging.getLogger(__name__)


class RobotsTxtMiddleware(object):
    DOWNLOAD_PRIORITY = 1000

    def __init__(self, crawler):
        if not crawler.settings.getbool('ROBOTSTXT_OBEY'):
            raise NotConfigured

        self.crawler = crawler
        self._useragent = crawler.settings.get('USER_AGENT')
        self._parsers = {}

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        if request.meta.get('dont_obey_robotstxt'):
            return
        rp = self.robot_parser(request, spider)
        if rp and not rp.can_fetch(self._useragent, request.url):
            logger.debug("Forbidden by robots.txt: %(request)s", {'request': request}, extra={'spider': spider})
            raise IgnoreRequest
    
    # 获取到网站下面的robots.txt文件并进行处理
    def robot_parser(self, request, spider):
        url = urlparse_cached(request)
        netloc = url.netloc
        if netloc not in self._parsers:
            self._parsers[netloc] = None
            robotsurl = "%s://%s/robots.txt" % (url.scheme, url.netloc)
            robotsreq = Request(
                robotsurl,
                priority=self.DOWNLOAD_PRIORITY,
                meta={'dont_obey_robotstxt': True}
            )
            dfd = self.crawler.engine.download(robotsreq, spider)
            dfd.addCallback(self._parse_robots)
            dfd.addErrback(self._logerror, robotsreq, spider)
        return self._parsers[netloc]

    def _logerror(self, failure, request, spider):
        if failure.type is not IgnoreRequest:
            logger.error("Error downloading %(request)s: %(f_exception)s",
                         {'request': request, 'f_exception': failure.value},
                         exc_info=failure_to_exc_info(failure),
                         extra={'spider': spider})

    # 这里面是具体的处理过程
    def _parse_robots(self, response):
        rp = robotparser.RobotFileParser(response.url)
        rp.parse(response.body.splitlines())
        self._parsers[urlparse_cached(response).netloc] = rp
