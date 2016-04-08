1. http://lfstar.blog.163.com/blog/static/5637898720134365651965/
	如果在MacOSX (Mountain Lion),必须先执行两条export，否则在编译阶段会报错：'sed: RE error: illegal byte sequence'
	先执行这两句。
	export LC_COLLATE='C'
	export LC_CTYPE='C'
	
	
2. redis安装步骤
	参考 http://blog.csdn.net/zhaoqiubo/article/details/47445431
	redis.sh内容: /usr/local/bin/redis-server /usr/local/redis/etc/redis.conf &
	
3. MySQL安装步骤
	TODO

4. MongoDB安装步骤
	TODO
	
5. scrapy中文文档
	http://blog.csdn.net/iloveyin/article/details/41309679
	http://scrapy-chs.readthedocs.org/zh_CN/latest