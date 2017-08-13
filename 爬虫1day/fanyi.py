# coding=utf-8
import  urllib
import urllib2



url = "http://fanyi.baidu.com/v2transapi"

ua_headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
}
key = raw_input('请输入要翻译的文字:')
formdata = {
"from":"zh",
"to":"en",
"query":key,
"transtype":"realtime",
"simple_means_flag":"3"
 }
# data=urllib.urlencode(data).encode("utf-8")
data = urllib.urlencode(formdata)
# fullurl = url+key
# print data
request = urllib2.Request(url,data=data,headers=ua_headers)

response = urllib2.urlopen(request)

print response.read()