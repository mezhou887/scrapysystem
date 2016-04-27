1. http://lfstar.blog.163.com/blog/static/5637898720134365651965/
	如果在MacOSX (Mountain Lion),必须先执行两条export，否则在编译阶段会报错：'sed: RE error: illegal byte sequence'
	先执行这两句。
	export LC_COLLATE='C'
	export LC_CTYPE='C'
	
2. redis安装步骤
	参考 http://blog.csdn.net/zhaoqiubo/article/details/47445431 具体如下:
    cd /Users/zhoumaoen
	curl -O http://download.redis.io/releases/redis-3.0.7.tar.gz
	tar -zxvf redis-3.0.7.tar.gz
	cp -R -n redis-3.0.7/ /usr/local/redis
	cd /usr/local/redis
	sudo make test
	sudo make install
	mkdir -p /Users/zhoumaoen/redis/bin
	mkdir -p /Users/zhoumaoen/redis/etc
	mkdir -p /Users/zhoumaoen/data/redis/
	cp /usr/local/redis/src/mkreleasehdr.sh /Users/zhoumaoen/redis/bin
	cp /usr/local/redis/src/redis-benchmark /Users/zhoumaoen/redis/bin
	cp /usr/local/redis/src/redis-check-dump /Users/zhoumaoen/redis/bin
	cp /usr/local/redis/src/redis-cli /Users/zhoumaoen/redis/bin
	cp /usr/local/redis/src/redis-server /Users/zhoumaoen/redis/bin
	下载这个文件https://github.com/mezhou887/scrapysystem/blob/master/doc/redis.conf并保存到/Users/zhoumaoen/redis/etc中
	
	执行命令启动: /Users/zhoumaoen/redis/bin/redis-server /Users/zhoumaoen/redis/etc/redis.conf &
	
3. MongoDB安装步骤
    cd /Users/zhoumaoen
	mkdir -p /Users/zhoumaoen/MongoDB
	curl -O https://fastdl.mongodb.org/osx/mongodb-osx-x86_64-3.2.4.tgz
	tar -zxvf mongodb-osx-x86_64-3.2.4.tgz
	cp -R -n mongodb-osx-x86_64-3.2.4/ /Users/zhoumaoen/MongoDB
	mkdir -p /Users/zhoumaoen/data/mongodb
	chmod 777 /Users/zhoumaoen/data/mongodb
	执行命令启动: /Users/zhoumaoen/MongoDB/bin/mongod --dbpath /Users/zhoumaoen/data/mongodb &
	访问地址: http://localhost:27017/ 查看是否安装成功

4. MySQL安装步骤
	参考 http://www.cnblogs.com/macro-cheng/archive/2011/10/25/mysql-001.html
	账号密码 mezhou887/Admin1234#
	在系统偏好设置中启动MySQL 
	卸载 MySQL: http://www.cnblogs.com/TsengYuen/archive/2011/12/06/2278574.html
	
5. scrapy中文文档
	http://blog.csdn.net/iloveyin/article/details/41309679
	http://scrapy-chs.readthedocs.org/zh_CN/latest
	
6. 一行代码升级所有已安装的第三方包
	pip list --outdated | grep '^[a-z]* (' | cut -d " " -f 1 | xargs pip install -U

7. Xpath在FireFox下的插件
	Xpath Checker 0.4.4.1
	http://python.jobbole.com/84689/
	
8. 爬虫链接
	http://python.jobbole.com/84772/
	
9. 安装mysql-connector-python
	pip install mysql-connector-python	
	
10. python virtualenv沙盒环境的使用
	http://www.cnblogs.com/tk091/p/3700013.html
	
11. crontab的问题
	crontab: "/usr/bin/vi" exited with status 1
	执行以下命令: export EDITOR=vim
	
12. Beautiful Soup 4.2.0中文文档
	https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
	
13. phantomjs 2.1.1 下载地址
	http://pan.baidu.com/s/1bEnD5G  gqsy
	
14. 加入异常处理和md5
	http://www.w2bc.com/Article/44862
	
15. json转换成其他格式
	https://github.com/micha/jsawk (curl -L http://github.com/micha/jsawk/raw/master/jsawk > jsawk  chmod 777 jsawk && mv jsawk /bin/)
	https://stedolan.github.io/jq/ (apt-get install jq)
	
16. 参考链接
	http://www.cnblogs.com/Bright-Star/p/4163107.html?utm_source=tuicool&utm_medium=referral
	http://blog.chedushi.com/archives/6488
	http://www.xuebuyuan.com/1252477.html
	http://www.zhihu.com/question/19793879
	http://stackoverflow.com/questions/12553117/how-to-filter-duplicate-requests-based-on-url-in-scrapy
	https://github.com/mezhou887/scrapy-cluster
	https://github.com/mezhou887/scrapylib
	
	
		