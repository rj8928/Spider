# -*- coding: utf-8 -*-
import scrapy
import json
from shijijiayuan.items import ShijijiayuanItem
from scrapy_redis.spiders import RedisSpider


class JianyuanSpider(RedisSpider):
    name = 'jiayuan'
    # allowed_domains = ['jiayuan.com']
    page = 1
    redis_key = 'myspider:start_urls'
    # start_urls = ['http://jiayuan.com/']
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(JianyuanSpider, self).__init__(*args, **kwargs)

    def parse(self,response):
        url = 'https://passport.jiayuan.com/dologin.php?host=www.jiayuan.com&new_header=1&channel=index/'

        yield scrapy.FormRequest(
            url = url,
            formdata= {
                "channel": "200",
                "position": "201",
                "name": "15570080949",
                "password": "892806304",
                "remem_pass": "on"},
            callback= self.parse_page
        )


    def parse_page(self, response):
        print response.status
        url = 'http://search.jiayuan.com/v2/search_v2.php' + "?" + str(self.page) + "/"
        while self.page <= 5:
            yield scrapy.FormRequest(
                url = 'http://search.jiayuan.com/v2/search_v2.php' + "?" + str(self.page) + "/",
                formdata={
                "sex":"f",
                "key":"",
                "stc":"1:36, 2:20.28, 23:1",
                "sn":"default",
                "sv":"1",
                "p":str(self.page),
                "f":"",
                "listStyle":"bigPhoto",
                "pri_uid":"167374339",
                "jsversion":"v5"
                    },
                callback=self.delpage
                )

            if self.page < 200:
                self.page += 1
            # print self.page


    def delpage(self,response):
        print response.status
        content = response.body[11:-13]
        # print 9999999
        # print content
        # print 9999999999999999999999999999999999999999999999
        content =json.loads(content)
        userinfo =content["userInfo"]

        for user in userinfo:
            item = ShijijiayuanItem()
            item['userid'] = user['realUid']
            item['nickname'] = user['nickname']
            item['sex'] = user['sex']
            item['marriage'] = user['marriage']
            item['height'] = user['height']
            item['education'] = user['education']
            item['work_location'] = user['work_location']
            item['age'] = user['age']
            item['shortnote'] = user['shortnote']
            item['matchCondition'] = user['matchCondition']
            url = "http://www.jiayuan.com/" + str(user['realUid'])
            item['source'] = url
            # print 8888
            # print url
            # print 9999
            yield scrapy.Request(url= url, meta={"meta_1": item}, callback=self.second_parse)



    def second_parse(self,response):
        meta_1 = response.meta['meta_1']
        income = response.xpath('string(//ul[@class="member_info_list fn-clear"]//li[4])').extract()[0]
        house = response.xpath('string(//ul[@class="member_info_list fn-clear"]//li[5])').extract()[0]
        weight = response.xpath('string(//ul[@class="member_info_list fn-clear"]//li[6])').extract()[0]

        income = ''.join(income.split())
        house = ''.join(house.split())
        weight = ''.join(weight.split())


        meta_1['income'] = income
        meta_1['house'] = house
        meta_1['weight'] = weight

        # 相册地址
        images_urls = response.xpath('//div[@class="small_pic fn-clear"]//a/@href').extract()[0]
        # print images_urls

        yield scrapy.Request(url=images_urls,meta={"meta_2":meta_1},callback=self.thirdly_parse)

    def thirdly_parse(self,response):
        meta_2 = response.meta['meta_2']
        images_urls = response.xpath('//td[@align="center"]/img/@src').extract()
        meta_2['images_urls'] = images_urls

        yield meta_2








        """
        相册地址
       //div[@class="small_pic fn-clear"]//a/@href 
        相册每张图片地址
        //td[@align="center"]/img/@src
         
         //ul[@class="member_info_list fn-clear"]//li 456 月薪住房体重
         
         //img[@class="img_absolute"]/@src  图片
         
         
         
         
         "uid": 164649321,
            "realUid": 165649321,
            "nickname": "盛玉青",
            "sex": "女",
            "sexValue": "f",
            "randAttr": "formal",
            "marriage": "离异",
            "height": "164",
            "education": "大专",
            "income": null,
            "work_location": "景德镇",
            "work_sublocation": "景德镇",
            "age": 27,
            "image": "http://at2.jyimg.com/d1/96/c17385db5d60da9b2d1724e4049f/c17385db5_3_avatar_p.jpg",
            "count": "7502",
            "online": 0,
            "randTag": "<span>164cm</span>",
            "randListTag": "<span>164cm</span>",
            "userIcon": "<i title=手机认证 class=tel></i><i title=看信包月 class=kxby></i>",
            "helloUrl": "http://www.jiayuan.com/msg/hello.php?type=20&randomfrom=4&uhash=d1c17385db5d60da9b2d1724e4049f96",
            "sendMsgUrl": "http://www.jiayuan.com/msg/send.php?uhash=d1c17385db5d60da9b2d1724e4049f96",
            "shortnote": "我是一个简单,开朗,独立,大大咧咧,孝顺的人 ，关于外貌，简单形容就是大眼睛,微胖。我自己拥有2家手机店和一套自己的房子，我不管在经济还是在生活上都有独立能力，而且烧菜也不错哦！如…",
            "matchCondition": "28-35岁,172-189cm,本科,有照片"
            """



