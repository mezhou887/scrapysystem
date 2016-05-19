"""
Scrapy ʹ���ź���֪ͨ���鷢��
"""

# ��Scrapy����������ȡʱ���͸��ź�
engine_started = object()

# ��Scrapy����ֹͣʱ���͸��ź�
engine_stopped = object()

# ��spider��ʼ��ȡʱ���͸��ź�
spider_opened = object()

# ��spider�������(idle)״̬ʱ���͸��ź�
spider_idle = object()

# ��ĳ��spider���ر�ʱ�����͸��ź�
spider_closed = object()

# ��spider�Ļص�������������ʱ(���磬�׳��쳣)�����͸��ź�
spider_error = object()

# ���������һ�� Request ������������ʱ�����͸��ź�
request_scheduled = object()

# ���������һ��Request���������ӳٱ��������ܾ�ʱ�����͸��ź�
request_dropped = object()

# �������downloader��ȡ��һ���µ� Response ʱ���͸��ź�
response_received = object()

# ��һ�� HTTPResponse ������ʱ����downloader���͸��ź�
response_downloaded = object()

# ��item����ȡ����ͨ������ Item Pipeline ��(û�б�����(dropped)�����͸��ź�
item_scraped = object()

# ��itemͨ�� Item Pipeline ����Щpipeline�׳� DropItem �쳣������itemʱ�����͸��ź�
item_dropped = object()

# for backwards compatibility
stats_spider_opened = spider_opened
stats_spider_closing = spider_closed
stats_spider_closed = spider_closed

item_passed = item_scraped

request_received = request_scheduled
