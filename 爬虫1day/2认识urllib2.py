# coding=utf-8

import urllib2


# 向指定的url发送请求，并返回服务器响应的类文件
# open不支持构造头请求
response = urllib2.urlopen("http://www.baidu.com/")

html = response.read()

print html