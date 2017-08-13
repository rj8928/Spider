# coding=utf-8

import urllib2
# 线程库
import threading
# 队列
from Queue import Queue
# 解析库
from lxml import etree
# 请求处理
import requests
# json处理
import json


class ThreadCrawl(threading.Thread):
    def __init__(self,threadname,pageQueue,dataQueue):
        # 初始化父类__init__方法
        # threading.Thtrad.__init__(self)
        super(ThreadCrawl,self).__init__()
        self.threadName = threadname
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.ua_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
        }

    def run(self):
        print "开始" + self.threadName

        while not CRAWL_EXIT:
            # 取出一个页码
            # 可选参数block，默认为True
            # 1.如果队列为空，block为True，进入阻塞状态，直到队列有新的数据
            # 2.如果队列为空，block为False，弹出empty（）异常
            try:
                page = self.pageQueue.get(False)
                url = "http://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                content = requests.get(url,headers = self.ua_headers).text
                self.dataQueue.put(content)


            except:
                pass

        print "结束" + self.threadName


class ThreadParse(threading.Thread):
    def __init__(self, threadname, dataQueue, filename,lock):
        super(ThreadParse,self).__init__()
        self.threadName = threadname
        self.dataQueue = dataQueue
        self.filename = filename
        self.lock = lock

    def run(self):
        print "开始" + self.threadName

        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                self.parse(html)
            except:
                pass

        print "结束" + self.threadName

    # 处理html内容并保存
    def parse(self,html):
        # print 111
        # print html
        html = etree.HTML(html)
        node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')
        # print 222
        items = {}
        for node in node_list:
            # print 33
            # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
            username = node.xpath('.//div/a/h2')[0].text
            # 图片连接
            image = node.xpath('.//div[@class="thumb"]//@src')  # [0]
            # 取出标签下的内容,段子内容
            content = node.xpath('.//div[@class="content"]/span')[0].text
            # 取出标签里包含的内容，点赞
            zan = node.xpath('.//i')[0].text
            # 评论
            comments = node.xpath('.//i')[1].text
            items = {
                "username": username,
                "image": image,
                "content": content,
                "zan": zan,
                "comments": comments
            }
            # print 22
            with self.lock:
                with open(self.filename + ".json", "a") as f:
                    print "正在写入"
                    f.write(json.dumps(items, ensure_ascii=False).encode("utf-8") + "\n")


# 退出控制
CRAWL_EXIT = False
# 采集控制
PARSE_EXIT = False

def main():
    # 页码队列，容量为10
    pageQueue = Queue(10)
    # 数字放入队列
    for i in range(1,11):
        pageQueue.put(i)
    # 采集结果队列  每一页的html源码
    dataQueue = Queue()
    # 采集线程与解析线程
    crawlList = ['采集线程1','采集线程2','采集线程3']
    parseList =['解析线程1','解析线程2','解析线程3']

    # 存储三个采集线程
    threadcrawl = []
    # 存储三个解析线程
    threadparse = []

    lock = threading.Lock()
    filename = "糗事百科"

    # 调用采集线程执行
    for threadname in crawlList:
        thread = ThreadCrawl(threadname,pageQueue,dataQueue)
        thread.start()
        threadcrawl.append(thread)


    # 调用解析线程执行
    for threadname in parseList:
        thread = ThreadParse(threadname,dataQueue,filename,lock)
        thread.start()
        threadparse.append(thread)
    # 队列空 阻塞
    while not pageQueue.empty():
        pass
    global CRAWL_EXIT
    CRAWL_EXIT = True
    print "队列空了"

    for thread in threadcrawl:
        thread.join()
        print 'over'

    while not dataQueue.empty():
        pass
    global PARSE_EXIT
    PARSE_EXIT = True
    print "正在处理"

    for thread in threadparse:
        thread.join()
        print "完成"
        







if __name__ == "__main__":
    main()