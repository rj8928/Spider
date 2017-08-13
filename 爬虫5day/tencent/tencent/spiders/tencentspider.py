# -*- coding: utf-8 -*-
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
#
#
# class TencentspiderSpider(CrawlSpider):
#     name = 'tencentspider'
#     allowed_domains = ['tencent.com']
#     start_urls = ['http://tencent.com/']
#
#     rules = (
#         Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
#     )
#
#     def parse_item(self, response):
#         i = {}
#         #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
#         #i['name'] = response.xpath('//div[@id="name"]').extract()
#         #i['description'] = response.xpath('//div[@id="description"]').extract()
#         return i


import scrapy
# 导入CrawlSpider类和Rule
from scrapy.spider import CrawlSpider,Rule
# 导入链接规则匹配类，用来提取符合规则的连接
from scrapy.linkextractors import LinkExtractor
from tencent.items import TencentItem

class TencentSpider(CrawlSpider):
    name = "tencentspider"
    allow_domains = ["hr.tencent.com"]
    start_urls = ["http://hr.tencent.com/position.php?&start=0#a"]

    pagelink = LinkExtractor(allow=("start=\d+"))

    rules = [
        Rule(pagelink,callback="parseTencent",follow=True),



    ]

    def parseTencent(self,response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
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


