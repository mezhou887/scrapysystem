#-*- coding: UTF-8 -*-
import json
import codecs

data = []
with open('proxylist.json') as f:
    for line in f:
        data.append(json.loads(line))

str = "\r\n"
for item in data:
    str = str + "insert into proxylist(name,catalog,workLocation,recruitNumber,detailLink,publishTime) values "
    str = str + "('%s','%s','%s','%s','%s','%s');\r\n" % (item['name'],item['catalog'],item['workLocation'],item['recruitNumber'],item['detailLink'],item['publishTime'])

file_object = codecs.open('proxylist.sql', 'w' ,"utf-8")
file_object.write(str)
file_object.close()
print "success"
