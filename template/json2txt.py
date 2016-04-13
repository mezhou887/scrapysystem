#-*- coding: UTF-8 -*-
import json

data = []
with open('template.json') as f:
    for line in f:
        data.append(json.loads(line))

import codecs
file_object = codecs.open('template.sql', 'w' ,"utf-8")
for item in data:
    str = "%s#_#%s#_#%s#_#%s\r\n" % (item['title'],item['link'],item['desc'],item['listUrl'])
    file_object.write(str)

file_object.write(str)
file_object.close()
print "success"

