# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    table = 'dang'  # 表名
    title = scrapy.Field()
    url = scrapy.Field()
    pic = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()


