"""
所有的与http相关的模块
"""

from scrapy.http.headers import Headers

from scrapy.http.request import Request
from scrapy.http.request.form import FormRequest
from scrapy.http.request.rpc import XmlRpcRequest

from scrapy.http.response import Response
from scrapy.http.response.html import HtmlResponse
from scrapy.http.response.xml import XmlResponse
from scrapy.http.response.text import TextResponse
