# coding=utf-8

import urllib
import urllib2

url = "http://www.baidu.com/s"
headers = {"User-Agent":"Mozilla...."}

keyword = raw_input("请输入要查询的关键字：")

wd = {"wd":keyword}

wd = urllib.urlencode(wd)

fullurl = url + "?" + wd

print fullurl

request = urllib2.Request(fullurl,headers= headers)

response = urllib2.urlopen(request)

print response.read()