# coding=utf-8
import urllib2

# 构建一个HTTPHandler处理器对象，支持处理HTTP的请求
http_handler = urllib2.HTTPHandler(debuglevel=1)


# build——opener方法构建一个自定义的opener对象，参数是构建的处理器对象
opener = urllib2.build_opener(http_handler)

request = urllib2.Request("http://www.baidu.com/")
response = opener.open(request)

print response.read()
