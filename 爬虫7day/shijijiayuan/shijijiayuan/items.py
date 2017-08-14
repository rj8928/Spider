# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShijijiayuanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # 用户名
    nickname = scrapy.Field()
    # 性别
    sex = scrapy.Field()
    # uid
    userid = scrapy.Field()
    # 状态
    marriage = scrapy.Field()
    # 年龄
    age = scrapy.Field()
    # 图片链接
    images_urls = scrapy.Field()
    imagepath = scrapy.Field()
    # 简介
    shortnote = scrapy.Field()
    # 籍贯
    work_location = scrapy.Field()
    # 学历
    education = scrapy.Field()
    # 身高
    height = scrapy.Field()
    # 月薪
    income = scrapy.Field()
    # 体重
    weight = scrapy.Field()
    # 住房
    house = scrapy.Field()

    # 个人主页
    source_url = scrapy.Field()

    # spider来源
    source = scrapy.Field()

    #择偶条件
    matchCondition = scrapy.Field()

    crawled = scrapy.Field()
    spider = scrapy.Field()

    """ 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
