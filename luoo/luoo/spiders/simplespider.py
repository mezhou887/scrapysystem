# -*- coding: utf-8 -*-
import scrapy
from luoo.items import luooItem
from scrapy.selector import Selector

class luooSpider(scrapy.Spider):
    name = "luoo"
    allowed_domains = ["luoo.net"]
    start_urls = ['http://www.luoo.net/music/'+str(i).rjust(3,'0') for i in range(1, 821)]
        
    # http://jandan.net/ooxx/page-1953#comments
    def parse(self, response):
        print response.url
        sel = Selector(response)
        items = []
        
        musics  = sel.xpath('//div[@id="luooPlayerPlaylist"]/ul/li').extract()
        
        for index, music in enumerate(musics):
            music_sel         = Selector(text=music)
            item              = luooItem()
            item['pagelink']  = response.url
            item['title']     = response.xpath('//title/text()').extract()[0].strip()
            item['musicname'] = music_sel.xpath('//div[@class="track-wrapper clearfix"]/a[1]/text()').extract()[0].strip()
            musiclink         = 'http://luoo-mp3.kssws.ks-cdn.com/low/luoo/radio' + str(int(response.url.split('/')[-1])) + '/' + str(index+1).rjust(2, '0') + '.mp3'
            item['musiclink'] = item['file_urls'] = musiclink
            item['autor']     = music_sel.xpath('//div[@class="track-wrapper clearfix"]/span[2]/text()').extract()[0].strip()
            items.append(item)
        return items        
