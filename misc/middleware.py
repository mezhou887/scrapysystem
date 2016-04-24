from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from agents import AGENTS

import random

class CustomUserAgentMiddleware(UserAgentMiddleware):

    def process_request(self, request, spider):
        if self.user_agent:
            request.headers.setdefault('User-Agent', self.user_agent)
        else:
            agent = random.choice(AGENTS)
            request.headers.setdefault('User-Agent', agent)
                
