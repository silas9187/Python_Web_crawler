# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy import Selector
class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&page_index=1']
    p = 1
    def parse(self, response):
        # print('aaaaa')

        # 获取所有图书信息
        dlist = response.selector.xpath("//div[@id='search_nature_rg']//li")
        # 遍历图书，解析信息然后封装到item容器中
        for dd in dlist:
            # 构造图书信息的Item容器对象
            item = DangdangItem()
            # 标题
            item['title'] = dd.css("a::attr(title)").extract_first()
            # 判断是有data-original属性或者src属性，从而得到所有的图书的图片信息
            if dd.xpath("./a[@name='itemlist-picture']/img/@data-original").extract_first():
                item['pic'] = dd.xpath("./a[@name='itemlist-picture']/img/@data-original").extract_first()
            else:
                item['pic'] = dd.xpath("./a[@name='itemlist-picture']/img/@src").extract_first()
            # 图书详情链接
            item['url'] = dd.css("a::attr(href)").extract_first()
            # 图书作者
            item['author'] = dd.xpath(".//p[@class='search_book_author']/span[1]/a[1]/@title").extract_first()
            # 图书价格
            item['price'] = dd.css("span.search_now_price::text").extract_first()
            # 交给管道文件
            yield (item)

            self.p += 1
            if self.p <= 55:
                next_url = 'http://search.dangdang.com/?key=python&page_index=' + str(self.p)
                url = response.urljoin(next_url)  # 构建绝对url地址
                yield scrapy.Request(url=url, callback=self.parse)
