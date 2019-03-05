# -*- coding: utf-8 -*-
import scrapy
from demo.items import FangItem
from scrapy_redis.spiders import RedisSpider

class FangSpider(RedisSpider):
    name = 'fang'
    #allowed_domains = ['fang.5i5j.com']
    #start_urls = ['https://fang.5i5j.com/bj/loupan/']
    redis_key = "fangspider:start_urls"

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(FangSpider, self).__init__(*args, **kwargs)
        
    def parse(self, response):
        #print(response.status)
        hlist = response.css("div.houseList_list")
        for vo in hlist:
            item = FangItem()
            item['title'] = vo.css("h3.fontS20 a::text").extract_first()
            item['address'] = vo.css("span.addressName::text").extract_first()
            item['time'] = vo.re("<span>(.*?)开盘</span>")[0]
            item['clicks'] = vo.re("<span><i>([0-9]+)</i>浏览</span>")[0]
            item['price'] = vo.css("i.fontS24::text").extract_first()
            #print(item)
            yield item
        #pass
