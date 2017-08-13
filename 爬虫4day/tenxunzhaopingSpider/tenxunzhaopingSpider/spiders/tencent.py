# -*- coding: utf-8 -*-
import scrapy
from tenxunzhaopingSpider.items import TenxunzhaopingspiderItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    url = "http://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TenxunzhaopingspiderItem()

            # 职位名称
            item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情链接
            item['link'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            positionType = each.xpath("./td[2]/text()").extract()
            if positionType:
                item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            else:
                item['positionType'] = ''
            # 招聘人数
            item['popleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

        if self.offset <2190:
            self.offset +=10
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)








