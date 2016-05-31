##1. commands包 ##

+ __init__.py: 基类，提供了基本的框架，给commands包下的其他类继承，默认设置为不需要项目才能运行，通过运行run方法来运行命令
+ bench.py: 性能测试类，执行的命令为scrapy bench
+ check.py: 设置为需要项目才能运行，执行命令为scrapy check
+ crawl.py: 设置为需要项目才能运行，爬虫运行就是从这里开始的，使用spider进行爬取

##2. http包 ##

##3. downloadermiddlewares中间件 ##
+ robotstxt: RobotsTxtMiddleware,优先级是最高的，作用是

##4. pipelines包 ##



##N.综合 ##