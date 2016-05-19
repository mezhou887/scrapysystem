"""
Scrapy 使用信号来通知事情发生
"""

# 当Scrapy引擎启动爬取时发送该信号
engine_started = object()

# 当Scrapy引擎停止时发送该信号
engine_stopped = object()

# 当spider开始爬取时发送该信号
spider_opened = object()

# 当spider进入空闲(idle)状态时发送该信号
spider_idle = object()

# 当某个spider被关闭时，发送该信号
spider_closed = object()

# 当spider的回调函数产生错误时(例如，抛出异常)，发送该信号
spider_error = object()

# 当引擎调度一个 Request 对象用于下载时，发送该信号
request_scheduled = object()

# 当引擎调度一个Request对象下载延迟被调度器拒绝时，发送该信号
request_dropped = object()

# 当引擎从downloader获取到一个新的 Response 时发送该信号
response_received = object()

# 当一个 HTTPResponse 被下载时，由downloader发送该信号
response_downloaded = object()

# 当item被爬取，并通过所有 Item Pipeline 后(没有被丢弃(dropped)，发送该信号
item_scraped = object()

# 当item通过 Item Pipeline ，有些pipeline抛出 DropItem 异常，丢弃item时，发送该信号
item_dropped = object()

# for backwards compatibility
stats_spider_opened = spider_opened
stats_spider_closing = spider_closed
stats_spider_closed = spider_closed

item_passed = item_scraped

request_received = request_scheduled
