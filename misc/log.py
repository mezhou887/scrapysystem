# -*- coding: utf-8 -*-
import pprint
class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        if isinstance(object, unicode):
            return (object.encode('utf8'), True, False)
        return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)

# pu是经过修改的版本，支持UTF-8模式
pu = MyPrettyPrinter() 

# pp是默认的版本
pp = pprint.PrettyPrinter()


