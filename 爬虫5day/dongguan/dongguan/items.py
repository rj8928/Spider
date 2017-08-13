# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # 标题
    title = scrapy.Field()
    # 编号
    num = scrapy.Field()
    # 内容
    info = scrapy.Field()
    # 状态
    # status = scrapy.Field()
    # url
    url = scrapy.Field()