import urllib
import urllib2

formdata = {
"type":"11",
"interval_id":"100:90",
"action":"",
"start":"0",
"limit":"20"
}

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="

ua_headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
}

data = urllib.urlencode(formdata)
request = urllib2.Request(url,data=data,headers=ua_headers)
print urllib2.urlopen(request).read()
