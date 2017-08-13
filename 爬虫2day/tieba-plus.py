# coding=utf-8

import  urllib
import urllib2
from lxml import etree


headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 60.0.3112.78Safari / 537.36"
    }
def loadpage(url):
    """根据url发送请求，获取服务器响应文件
        url:需要爬取的url地址
        filename: 文件名
    """
    # print "正在下载" +filename

    request = urllib2.Request(url, headers = headers)
    html = urllib2.urlopen(request).read()
    # 解析HTML文档
    content = etree.HTML(html)
    link_list = content.xpath('//div[@class="threadlist_lz clearfix"]//a[@class="j_th_tit "]/@href')
    for link in link_list:
        fulllink = "http://tieba.baidu.com"+link
        loadImage(fulllink)


def loadImage(link):
    request = urllib2.Request(link,headers=headers)
    response = urllib2.urlopen(request).read()


    content = etree.HTML(response)
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    for link in link_list:
        writeImage(link)




def writeImage(link):
    """
    作用： 将html内容写入到本地
     HTML： 服务器响应文件内容
     filename: 文件名
    """
    # print "正在保存"
    # 文件写入
    request = urllib2.Request(link,headers=headers)
    image = urllib2.urlopen(request).read()
    filename = link[-10:]
    with open("./meinv/"+filename,'wb')as f:
        f.write(image)
    print "-完成-"*30

def tiebaSpider(url,beginPage,endPage):
    """
    踢人吧爬虫调度器，负责组合处理每个页面的url
    url：贴吧url的前部分
    beginPage:起始页
    endpage:终止页
    :return:
    """

    for page in range(beginPage,endPage+1):
        pn = (page-1)*50
        fullurl = url + "&pn=" + str(pn)
        # print fullurl
        # filename = "第" + str(page)+"页.html"
        html = loadpage(url)
        # print html

    print "谢谢使用"


if __name__ == '__main__':
    kw = raw_input("请输入要爬取的贴吧名：")
    beginPage = int(raw_input("请输入起始页:"))
    endPage = int(raw_input("请输入结束页:"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw":kw})
    fullurl = url + key
    tiebaSpider(fullurl,beginPage,endPage)
