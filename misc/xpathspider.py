#coding: utf-8
import scrapy
import re

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider

# 模板1，使用最基本的Spider来完成
class BaseXpathSpider(scrapy.Spider):
    
    def extract_item(self, sels):
        contents = []
        for i in sels:
            content = re.sub(r'\s+', ' ', i.extract())
            if content != ' ':
                contents.append(content)
        return contents

    def extract_items(self, sel, rules, pagelink, item):
        for nk, nv in rules.items():
            if nk in ('__link'):
                item[nv] = pagelink
                continue          
            if nk in ('__use'):
                continue
            if nk not in item:
                item[nk] = []
            if sel.xpath(nv):
                item[nk] += self.extract_item(sel.xpath(nv))
            else:
                item[nk] = []    
    
    def traversal(self, sel, rules, pagelink, item_class, item, items):
        if item is None:
            item = item_class()
        if '__use' in rules:
            self.extract_items(sel, rules, pagelink, item)
            items.append(item)
        else:
            for nk, nv in rules.items():
                for i in sel.xpath(nk):
                    self.traversal(i, nv, pagelink, item_class, item, items)     
    
    
    def parse_with_rules(self, response, rules, item_class):
        sel = Selector(response)
        if sel is None:
            return []
        
        items = []
        self.traversal(sel, rules, response.url, item_class, None, items) 
        return items 
 
    
# 模板2，使用CrawlSpider来完成
class XpathSpider(BaseXpathSpider, CrawlSpider):         
    
    def traversal_dump(self, sel, rules, pagelink, item_class, item, items):
        item = {}
        for k, v in rules.items():
            if type(v) != dict:
                if k in ('__link'):
                    item[v] = pagelink
                    continue
                if k in ('__use'):
                    continue
                item[k] = self.extract_item(sel.xpath(v))
            else:
                item[k] = []
                for i in sel.xpath(k):
                    self.traversal_dump(i, v, pagelink, item_class, item, item[k])
        items.append(item)

    def dfs(self, sel, rules, pagelink, item_class, items):
        if item_class != dict:
            self.traversal(sel, rules, pagelink, item_class, None, items)
        else:
            self.traversal_dump(sel, rules, pagelink, item_class, None, items)

    def parse_with_rules(self, response, rules, item_class):
        sel = Selector(response)
        if sel is None:
            return []
        
        items = []
        self.dfs(sel, rules, response.url, item_class, items)
        return items
