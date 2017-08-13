# coding=utf-8

import urllib2


# 向指定的url发送请求，并返回服务器响应的类文件
# response = urllib2.urlopen("http://www.baidu.com/")

#  User-agent  爬虫与反爬虫的第一步  构造请求头
ua_headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
}

request = urllib2.Request("http://www.baidu.com/",headers= ua_headers)
response = urllib2.urlopen(request)

# 服务器返回的类文件支持Python文件对象的操作方法
html = response.read()

# 返回http响应码
print response.getcode()

# 返回实际url  防止重定向
print response.geturl()

# 返回服务器响应的http报头
print response.info()
