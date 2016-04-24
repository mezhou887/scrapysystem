from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from agents import AGENTS

import random

class CustomUserAgentMiddleware(object):

    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers.setdefault('User-Agent', agent)
                
