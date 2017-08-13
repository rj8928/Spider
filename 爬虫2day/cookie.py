# coding=utf-8
import urllib
import urllib2
import cookielib

#通过CookieJar类创建一个cookieJar对象，用来保存cookie的值
cookie = cookielib.CookieJar()

# 通过HTTPCookieProcessor处理器类构建一个处理器对象，用来处理cookie
#参数就是CookieJar类
cookie_handler = urllib2.HTTPCookieProcessor(cookie)


opener = urllib2.build_opener(cookie_handler)

# 登录接口
url = "http://ca.jxust.edu.cn/zfca/login?service=http%3A%2F%2Fportal.jxust.edu.cn%2Fportal.do"
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"),("Origin","http://ca.jxust.edu.cn"),("Referer","http://ca.jxust.edu.cn/zfca/login"),("Cookie",cookie1)]

data = {"username":"1320141927","password":"589588a"}

data =urllib.urlencode(data)

request = urllib2.Request(url,data=data)

response = opener.open(request)

print response.read().decode("gbk")