#-*-coding:utf-8-*-

import types
from w3lib.html import remove_entities
from urlparse import urljoin

NULL = [None,'null']

list_first_item = lambda x:x[0] if x else None

def strip_null(arg,null=None):
    if null is None:
        null = NULL

    if type(arg) is types.ListType:
        return [i for i in arg if i not in null]
    elif type(arg) is types.TupleType:
        return tuple([i for i in arg if i not in null])
    elif type(arg) is type(set()):
        return arg.difference(set(null))
    elif type(arg) is types.DictType:
        return {key:value for key,value in arg.items() if value not in null}

    return arg

def deduplication(arg):
    if type(arg) is types.ListType:
        return list(set(arg))
    elif type(arg) is types.TupleType:
        return tuple(set(arg))

    return arg

def clean_link(link_text):
    return link_text.strip("\t\r\n '\"")

clean_url = lambda base_url,u,response_encoding: urljoin(base_url, remove_entities(clean_link(u.decode(response_encoding))))
