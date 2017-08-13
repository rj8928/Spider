# coding=utf-8

import urllib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Spider:
    def __init__(self):
        # 初始化起始页位置
        self.page = 1
        # 爬取开关
        self.switch = True
        self.list = []

    def loadPage(self):
        """下载页面"""
        print "--开始下载数据--"
        url = "http://www.neihan8.com/article/list_5_" + str(self.page) + ".html"
        ua_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
        }
        request = urllib2.Request(url,headers=ua_headers)
        response = urllib2.urlopen(request)
        # 获取html源码字符串
        html = response.read().decode('gbk')
        #匹配每页中的段子内容 re.S表示全文匹配
        patterm = re.compile('<div\sclass="f18 mb20">(.*?)</div>',re.S)
        # 进行匹配，返回所有段子列表
        content_list = patterm.findall(html)
        self.dealPage(content_list)
        # for content in content_list:
        #     print content



    def dealPage(self,content_list):
        """处理每页的段子"""
        print "--正在处理数据--"
        for item in content_list:
            item =item.replace("<p>","").replace("</p>","").replace("<br>","").replace("<br />","").replace("&ldquo;","").replace("&rdquo;","").replace("&hellip;","")
            self.writePage(item)
            # print item
        print "--本次爬取完成--\n"


    def writePage(self,content):
        """把段子逐个写入到文件里"""
        # print content
        print "--正在写入数据--"
        with open("duanzi.txt","a") as f:
                f.write(content)

    def startWork(self):
        """控制爬种运行"""

        while self.switch:
            # 用户控制循环
            command = raw_input("(爬取请按回车，退出请按q)--")
            if command == "q":
                self.switch = False
                return 0
            self.loadPage()
            self.page += 1


if __name__=='__main__':
    spider = Spider()
    spider.startWork()

