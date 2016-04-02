from proxy import HTTPPROXIES, HTTPSPROXIES
from agents import AGENTS
import logging as log

import random


class CustomHttpProxyMiddleware(object):

    def process_request(self, request, spider):
        if self.use_proxy(request):
            p = random.choice(HTTPPROXIES)
            try:
                request.meta['updateproxy'] = "http://%s" % p['ip_port']
            except Exception, e:
                log.critical("Exception %s" % e)

    def use_proxy(self, request):
        return True

class CustomHttpsProxyMiddleware(object):

    def process_request(self, request, spider):
        if self.use_proxy(request):
            p = random.choice(HTTPSPROXIES)
            try:
                request.meta['updateproxy'] = "http://%s" % p['ip_port']
            except Exception, e:
                log.critical("Exception %s" % e)

    def use_proxy(self, request):
        return True


class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent
