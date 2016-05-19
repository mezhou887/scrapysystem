# -*- coding: utf-8 -*-
from scrapy.utils.reqser import request_to_dict, request_from_dict

try:
    import cPickle as pickle
except ImportError:
    import pickle

# 基类
class Base(object):

    def __init__(self, server, spider, key):
        self.server = server
        self.spider = spider
        self.key = key % {'spider': spider.name}

    def _encode_request(self, request):
        return pickle.dumps(request_to_dict(request, self.spider), protocol=-1)

    def _decode_request(self, encoded_request):
        return request_from_dict(pickle.loads(encoded_request), self.spider)

    def __len__(self):
        raise NotImplementedError

    def push(self, request):
        raise NotImplementedError

    def pop(self, timeout=0):
        raise NotImplementedError

    def clear(self):
        self.server.delete(self.key)

# 队列 FIFO
class SpiderQueue(Base):

    def __len__(self):
        return self.server.llen(self.key)

    def push(self, request):
        self.server.lpush(self.key, self._encode_request(request))

    def pop(self, timeout=0):
        if timeout > 0:
            data = self.server.brpop(self.key, timeout)
            if isinstance(data, tuple):
                data = data[1]
        else:
            data = self.server.rpop(self.key)
        if data:
            return self._decode_request(data)


# 默认的Queue
class SpiderPriorityQueue(Base):

    def __len__(self):
        return self.server.zcard(self.key)

    def push(self, request):
        data = self._encode_request(request)
        pairs = {data: -request.priority}
        self.server.zadd(self.key, **pairs)

    def pop(self, timeout=0):
        pipe = self.server.pipeline()
        pipe.multi()
        pipe.zrange(self.key, 0, 0).zremrangebyrank(self.key, 0, 0)
        results, count = pipe.execute()
        if results:
            return self._decode_request(results[0])

# 栈 LIFO
class SpiderStack(Base):

    def __len__(self):
        return self.server.llen(self.key)

    def push(self, request):
        self.server.lpush(self.key, self._encode_request(request))

    def pop(self, timeout=0):
        if timeout > 0:
            data = self.server.blpop(self.key, timeout)
            if isinstance(data, tuple):
                data = data[1]
        else:
            data = self.server.lpop(self.key)

        if data:
            return self._decode_request(data)


__all__ = ['SpiderQueue', 'SpiderPriorityQueue', 'SpiderStack']
