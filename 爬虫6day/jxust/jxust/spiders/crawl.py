# -*- coding: utf-8 -*-
import scrapy
from jxust.jxust_cookie import jxust_c

class CrawlSpider(scrapy.Spider):
    name = 'chengji'
    # allowed_domains = ['']
    start_urls = ['http://jw.jxust.edu.cn/']

    def showcode(self,codedata):
        pass


    def parse(self, response):
        username = raw_input("用户名：")
        self.filename = username
        password = raw_input("密码：")
        c = jxust_c()
        self.cookie = c.LoginSaveCookie(username,password)

        # _VIEWSTATE = response.xpath("//form/input/@value")
        # print _VIEWSTATE
        url = "http://jw.jxust.edu.cn/xscj_gc.aspx?xh=20141927&xm=%C8%D9%BF%A1&gnmkdm=N121605"
        yield  scrapy.FormRequest(
            url = url,
            cookies = self.cookie,
            callback= self.parse_page,
        )

    def parse_page(self,response):
        # print response.body.decode("gbk")
        _VIEWSTATE = response.xpath("//form/input/@value").extract()[0]
        # for temp in _VIEWSTATE:
        #     print 111
        #     print temp
        #     print 222
        #     _VIEWSTATE = temp
        # print _VIEWSTATE
        url = "http://jw.jxust.edu.cn/xscj_gc.aspx?xh=20141927&xm=%C8%D9%BF%A1&gnmkdm=N121605"
        form ={
        "__VIEWSTATE": _VIEWSTATE,
        "ddlXN":"",
        "ddlXQ":"",
        "Button2":"在校学习成绩查询"
        }
        yield scrapy.FormRequest(
            url=url,
            cookies=self.cookie,
            formdata= form,
            callback=self.parse_page2,
        )
    def parse_page2(self,response):
        item = response.xpath('//table[@id="Datagrid1"]').extract()[0]

        with open(self.filename + ".html","w") as f:
            f.write(item.encode("utf-8"))



