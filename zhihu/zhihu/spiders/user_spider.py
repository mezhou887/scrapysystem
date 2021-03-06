# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from datetime import datetime

from zhihu.settings import HEADER, COOKIES
from zhihu.items import *

host = 'http://www.zhihu.com'

class ZhihuUserSpider(scrapy.Spider):
   
    name = "zhihu_user"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        'https://www.zhihu.com/people/raymond-wang',
    ]
    
    def __init__(self,  *a,  **kwargs):
        super(ZhihuUserSpider, self).__init__(*a, **kwargs)
        self.user_names = []
        self.headers    = HEADER
        self.cookies    = COOKIES
        
    def make_requests_from_url(self, url):
        return Request(url, headers = self.headers, cookies = self.cookies, dont_filter=True)    

    def parse(self, response):
        sel = Selector(response)
        
        self.parse_detail(response)
        
        headers = self.headers;
        headers['Referer'] = response.url
       
        followees_link = host+sel.xpath('//div[@class="zu-main-sidebar"]/div/a/@href').extract()[0]
        followers_link = host+sel.xpath('//div[@class="zu-main-sidebar"]/div/a/@href').extract()[1]

        yield scrapy.Request(followees_link, headers = headers, cookies=self.cookies, callback=self.parse_followees)
        yield scrapy.Request(followers_link, headers = headers, cookies=self.cookies, callback=self.parse_followers)    

    # 处理的是个人主页
    def parse_detail(self, response):
        print 'parse_detail', response.url
        sel = Selector(response)
        
        try:
            user = ZhihuUserItem()
             
            ## 通用参数
            user['_id'] = user['username']=response.url.split('/')[-2]
            user['url'] = response.url
             
            ## 基本信息
            user['nickname']    = ''.join(sel.xpath('//div[@class="title-section ellipsis"]/a[@class="name"]/text()').extract())                   # 姓名
            user['location']    = ''.join(sel.xpath('//span[@class="location item"]/a/text()').extract())                                          # 地址
            user['industry']    = ''.join(sel.xpath('//span[@class="business item"]/a/text()').extract())                                          # 产业
            user['sex']         = ''.join(sel.xpath('//span[@class="item gender"]/i/@class').extract())                                            # 性别
            user['description'] = ''.join(sel.xpath('//span[@class="description unfold-item"]/span/text()').extract()).strip().replace("\n",'')    # 描述信息
            user['view_num']    = ''.join(sel.xpath('//span[@class="zg-gray-normal"]/strong/text()').extract())                                    # 浏览次数
            user['update_time'] = str(datetime.now())
             
            statistics = sel.xpath('//div[@class="profile-navbar clearfix"]/a/span/text()').extract()
            if len(statistics) == 6:
                user['ask_num']        = statistics[1]      # 提问
                user['answer_num']     = statistics[2]      # 回答
                user['post_num']       = statistics[3]      # 文章
                user['collection_num'] = statistics[4]      # 收藏
                user['log_num']        = statistics[5]      # 公共编辑

            ## 详细资料
            # 个人成就
            statistics = sel.xpath('//div[@class="zm-profile-module-desc"]/span/strong/text()').extract()
            if len(statistics) == 4:
                user['agree_num'] = statistics[0]           # 赞同
                user['thank_num'] = statistics[1]           # 感谢
                user['fav_num']   = statistics[2]           # 收藏
                user['share_num'] = statistics[3]           # 分享
             
            # 职业经历
            user['jobs'] = []
            job_nodes = sel.xpath('//div[@class="zm-profile-module zg-clear"][1]/div')
            for node in job_nodes:
                company = '/'.join(node.xpath('//div[@class="ProfileItem-text ProfileItem-text--bold"]/a/text()').extract())
                title   = ''.join(node.xpath('//div[@class="ProfileItem-text ProfileItem-text--bold"]/span[2]/text()').extract())
                user['jobs'].append({'company': company, 'title':title})
                 
            # 居住信息    
            user['locations'] = []
            location_nodes = sel.xpath('//div[@class="zm-profile-module zg-clear"][2]/div')
            for node in location_nodes:
                local = '/'.join(node.xpath('//div[@class="ProfileItem-text ProfileItem-text--bold"]/a/text()').extract())
                user['locations'].append({'local': local})
 
            # 教育经历
            user['educations'] = []
            edu_nodes = sel.xpath('//div[@class="zm-profile-module zg-clear"][3]/div')
            for node in edu_nodes:
                school = ''.join(node.xpath('@data-title').extract())
                major  = ''.join(node.xpath('@data-sub-title').extract())
                user['educations'].append({'school':school, 'major':major})
 
            ## 关注了和关注者
            statistics = sel.xpath('//a[@class="item"]/strong/text()').extract()
            user['followee_num'] = statistics[0]        # 关注了的数量
            user['follower_num'] = statistics[1]        # 关注者的数量
 
            self.user_names.append(user['username'])    # 这个以后要保存到数据库中
            return user
 
        except Exception, e:
            open('error_pages/about_' + response.url.split('/')[-2]+'.html', 'w').write(response.body)
            print '='*10 + str(e)         


    def parse_followees(self, response):
        print 'parse_followees', response.url
        sel = Selector(response)
        links = sel.xpath('//div[@class="zm-list-content-medium"]/h2/a/@href').extract()

        headers = self.headers;
        headers['Referer'] = response.url

        for link in links:
            username_tmp = link.split('/')[-1]
            if username_tmp in self.user_names:
                print 'Already Get:' + '%s' % username_tmp
                continue
            
            yield Request(link+'/about', headers = headers, cookies=self.cookies, callback=self.parse_detail)
                 
                            
    def parse_followers(self, response):
        print 'parse_followers', response.url
        sel = Selector(response)
        links = sel.xpath('//div[@class="zm-list-content-medium"]/h2/a/@href').extract()
        
        headers = self.headers;
        headers['Referer'] = response.url

        for link in links:
            username_tmp = link.split('/')[-1]
            if username_tmp in self.user_names:
                print 'Already Get:' + '%s' % username_tmp
                continue

            yield Request(link+'/about', headers = headers, cookies=self.cookies, callback=self.parse_detail)
            