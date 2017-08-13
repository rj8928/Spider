# coding=utf-8

import scrapy
from mySpider.items import ItcastItem

# 创建一个爬虫类

class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = 'itcast'
    # 允许爬虫的作用域
    allowd_domains = ["http://www.itcast.cn"]
    # 爬虫起始 url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#']


    def parse(self, response):
        # with open('teacher.html','w') as f:
        #     f.write(response.body)
        teacher_list = response.xpath('//div[@class="li_txt"]')
        list1 = []
        for each in teacher_list:
            # 实例化一个对象
            item = ItcastItem()
            # extract 将【匹配出的结果转换成Unicode字符串
            # 不加extract 结果为xpath对象
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()

            # print name[0],title[0],info[0]
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            yield item
            # list1.append(item)

        # return list1
