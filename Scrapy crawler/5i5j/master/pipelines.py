# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis,re

class MasterPipeline(object):  
    def __init__(self,host,port):
        #连接redis数据库
        self.r = redis.Redis(host=host, port=port, decode_responses=True)
        #self.redis_url = 'redis://password:@localhost:6379/'  
        #self.r = redis.Redis.from_url(self.redis_url,decode_responses=True)  

    @classmethod
    def from_crawler(cls,crawler):
        '''注入实例化对象（传入参数）'''
        return cls(
            host = crawler.settings.get("REDIS_HOST"),
            port = crawler.settings.get("REDIS_PORT"),
        )

    def process_item(self, item, spider):  
        #使用正则判断url地址是否有效，并写入redis。
        if re.search('/bj/loupan/',item['url']):
            self.r.lpush('fangspider:start_urls', item['url'])
        else:
            self.r.lpush('fangspider:no_urls', item['url'])
