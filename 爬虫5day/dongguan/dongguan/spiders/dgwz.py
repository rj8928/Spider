# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem


class DgwzSpider(CrawlSpider):
    name = 'dgwz'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://d.wz.sun0769.com/index.php/question/huiyin?page=0']

    pagelink = LinkExtractor(allow=('huiyin\?page=\\d+'))
    infolink = LinkExtractor(allow=(r'question/\d+/\d+'))


    rules = (
        Rule(pagelink),
        Rule(infolink,callback="parse_dongguan",follow=False),
    )


    def parse_item(self, response):
        i = {}
        # print response.url + "这里"
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # yield i

    def parse_dongguan(self, response):
        item = DongguanItem()

        title = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]


        # 标题
        item['title'] = title

        # 编号
        item['num'] =  title.split(' ')[-1].split(':')[-1]
        # 内容
        item['info'] = response.xpath('//div[@class="c1 text14_2"]/text()').extract()[0]
        # 状态
        # item['status'] = response.xpath('//span[@class="qblue"]/text()').extract()[0]
        # url

        item['url'] = response.url




        # num = title.split('')[-1].split(':')[-1]
        #
        # info = response.xpath('//div[@class="c1 text14_2"]/text()')
        # status = response.xpath('//span[@class="qblue"]/text()')

        return item
