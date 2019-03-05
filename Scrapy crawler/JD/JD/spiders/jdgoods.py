# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from JD.items import JdItem
from bs4 import BeautifulSoup
class JdgoodsSpider(scrapy.Spider):
    name = 'jdgoods'
    allowed_domains = ['jd.com']
    base_urls = 'https://list.jd.com/list.html?cat=670,671,672&page='

    def start_requests(self):
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            url = self.base_urls + str(page)
            yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        products = response.xpath('//*[@id="plist"]/ul/li[@class="gl-item"]')
        # soup = BeautifulSoup(response.body, "lxml")
        for p in products:
            item = JdItem()
            # imlist = soup.find_all(name="img",attrs={"width":"220","height":"220"})
            # for im in imlist:
                # if 'src' in im.attrs:
                #     imurl = "https:" + im.attrs['src']
                # else:
                #     imurl = "https:" + im.attrs['data-lazy-img']
            # 首先判断有无src属性来决定如何获取
            if p.xpath(".//div[@class='p-img']/a/img/@src").extract():
                item['image'] = ''.join(["https:"] + p.xpath(".//div[@class='p-img']/a/img/@src").extract())
            else:
                item['image'] = ''.join(["https:"] + p.xpath(".//div[@class='p-img']/a/img/@data-lazy-img").extract())
            item['price'] = ''.join(p.xpath(".//div[@class='p-price']/strong[@class='J_price']//text()").extract()).strip()
            item['title'] = ''.join(p.xpath(".//div[@class='p-name']/a/em/text()").extract()).strip()
            yield item
