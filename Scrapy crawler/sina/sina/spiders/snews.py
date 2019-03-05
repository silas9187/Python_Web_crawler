# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

class SnewsSpider(scrapy.Spider):
    name = 'snews'
    allowed_domains = ['news.sina.com']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        dlist = response.selector.xpath("//div[@class='section']")
        for v in dlist:
            # 获取橙色1号标题并遍历输出
            hlist = v.xpath("./h2/text()").extract()
            for h in hlist:
                print(h, end="·")
            print()
            clist = v.xpath(".//div[@class='clearfix']")
            for c in clist:
                # 进行判断，从而打印出所有2号标题
                if c.xpath("./h3/a/@href").extract_first():
                    print(c.xpath("./h3/a/@href").extract_first(), end=':')
                    print(c.xpath("./h3/a/text()").extract_first())
                elif c.xpath("./h3/span/text()").extract_first():  # 显示出 产品 ,地方站
                    print(c.xpath("./h3/span/text()").extract_first())
                else:
                    print(c.xpath("./h3/text()").extract_first())  # 显示出 客户端

                print('>'*50)
                # 获取所有分类信息并遍历输出
                alist = c.xpath("./ul//li/a")
                for a in alist:
                    print(a.xpath("./@href").extract_first(), end=':')
                    print(a.xpath("./text()").extract_first())
                print("<" * 50)
