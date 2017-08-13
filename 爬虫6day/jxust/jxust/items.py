# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JxustItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    xuenian = scrapy.Field()
    xueqi = scrapy.Field()
    kechengdaima = scrapy.Field()
    kechengmingcheng = scrapy.Field()
    kechengxinzhi = scrapy.Field()
    xuefen = scrapy.Field()
    jidian = scrapy.Field()
    chengji = scrapy.Field()
    fuxiubiaoji = scrapy.Field()
    bukaochengji = scrapy.Field()
    chongxiuchengji = scrapy.Field()
    xueyuanmingcheng = scrapy.Field()

