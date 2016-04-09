# -*- coding: utf-8 -*-

# overview http://scrapyd.readthedocs.org/en/latest/overview.html

#1. server ipaddress  http://localhost:6800/

#2. Install scrapyd pip install scrapyd

#3. 运行爬虫
curl http://localhost:6800/schedule.json -d project=template -d spider=template

#4. 取消爬虫
curl http://localhost:6800/cancel.json -d project=template -d job=6487ec79947edab326d6db28a2d86511e8247444

#5. 显示所有爬虫
curl http://localhost:6800/listprojects.json

#6. 显示爬虫版本
curl http://localhost:6800/listversions.json?project=template

#7. 显示所有job
curl http://localhost:6800/listjobs.json?project=template

#8.删除爬虫项目
curl http://localhost:6800/delproject.json -d project=template

