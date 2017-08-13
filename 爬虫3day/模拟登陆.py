# coding=utf-8
from bs4 import BeautifulSoup
import requests
import time

def zhihuLogin():
    # 构建一个session对象，可以保存Cookie
    sess = requests.Session()

    ua_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
    }

    # 获取登录页面，找到需要post的数据,同时会记录当前网页的Cookie值
    html = sess.get("https://www.zhihu.com/#signin",headers = ua_headers).text

    # 调用lxml解析库
    bs = BeautifulSoup(html,'lxml')
    # 获取页面_xsrf
    _xsrf = bs.find("input",attrs={"name":"_xsrf"}).get("value")
    print _xsrf
    codeurl = "http://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn" % (time.time() * 1000)
    print codeurl


if __name__ == "__main__":
    zhihuLogin()