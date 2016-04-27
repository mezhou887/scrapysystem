#-*-coding:utf-8-*-

from urllib import quote
from w3lib.html import remove_entities
from w3lib.url import _safe_chars
from urlparse import urljoin

list_first_item = lambda x:x[0] if x else None

def clean_link(link_text):
    return link_text.strip("\t\r\n '\"")

clean_url = lambda base_url,u,response_encoding: urljoin(base_url, remove_entities(clean_link(u.decode(response_encoding))))

def parse_query_string(query):
    params = query.split("&")
    keyvals = []
    for param in params:
        kv = param.split("=") + [None]
        keyvals.append((kv[0], kv[1]))
    return keyvals


def filter_query(query, remove_re=None, keep_re=None):
    keyvals = parse_query_string(query)
    qargs = []
    for k, v in keyvals:
        if remove_re is not None and remove_re.search(k):
            continue
        if keep_re is None or keep_re.search(k):
            qarg = quote(k, _safe_chars)
            if isinstance(v, basestring):
                qarg = qarg + '=' + quote(v, _safe_chars)
            qargs.append(qarg.replace("%20", "+"))
    return '&'.join(qargs)