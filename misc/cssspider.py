#coding: utf-8

import re

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider

class CommonSpider(CrawlSpider):

    keywords = set(['__use', '__list'])
    def extract_item(self, sels):
        contents = []
        for i in sels:
            content = re.sub(r'\s+', ' ', i.extract())
            if content != ' ':
                contents.append(content)
        return contents

    def extract_items(self, sel, rules, item):
        for nk, nv in rules.items():
            if nk in ('__use', '__list'):
                continue
            if nk not in item:
                item[nk] = []
            if sel.css(nv):
                item[nk] += self.extract_item(sel.css(nv))
            else:
                item[nk] = []

    def traversal(self, sel, rules, item_class, item, items):
        if item is None:
            item = item_class()
        if '__use' in rules:
            if '__list' in rules:
                unique_item = item_class()
                self.extract_items(sel, rules, unique_item)
                items.append(unique_item)
            else:
                self.extract_items(sel, rules, item)
        else:
            for nk, nv in rules.items():
                for i in sel.css(nk):
                    self.traversal(i, nv, item_class, item, items)

    def deal_text(self, sel, item, force_1_item, k, v):
        if v.endswith('::text'):
            item[k] = ' '.join(self.extract_item(sel.css(v)))
        else:
            _items = self.extract_item(sel.css(v))
            if force_1_item:
                if len(_items) >= 1:
                    item[k] = _items[0]
                else:
                    item[k] = ''
            else:
                item[k] = _items

    def traversal_dict(self, sel, rules, item_class, item, items, force_1_item):
        item = {}
        for k, v in rules.items():
            if type(v) != dict:
                if k in self.keywords:
                    continue
                if type(v) == list:
                    continue
                self.deal_text(sel, item, force_1_item, k, v)
            else:
                item[k] = []
                for i in sel.css(k):
                    self.traversal_dict(i, v, item_class, item, item[k], force_1_item)
        items.append(item)

    def dfs(self, sel, rules, item_class, force_1_item):
        if sel is None:
            return []

        items = []
        if item_class != dict:
            self.traversal(sel, rules, item_class, None, items)
        else:
            self.traversal_dict(sel, rules, item_class, None, items, force_1_item)
        return items

    def parse_with_rules(self, response, rules, item_class, force_1_item=False):
        return self.dfs(Selector(response), rules, item_class, force_1_item)
