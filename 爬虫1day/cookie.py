import urllib
import urllib2
header = {
"Connection": "keep-alive",
# Cache-Control: max-age=0
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Referer": "http://jw.jxust.edu.cn/xscj_gc.aspx?xh=20141927&xm=%C8%D9%BF%A1&gnmkdm=N121605",
# Accept-Encoding: gzip, deflate
"Accept-Language": "zh-CN,zh;q=0.8",
"Cookie": "_gscu_1364509536=02006732j0ch2a68; _gscbrs_1364509536=1; ASP.NET_SessionId=y232h045yr5z0a45my1yrtz2"
}

formdata = {
# "__VIEWSTATE":"dDwxMjg4MjkxNjE4Ozs+xB5QtCIlbNdFE+iIWhBXgQ2KiOo=",
"__VIEWSTATE":"dDwxODI2NTc3MzMwO3Q8cDxsPHhoOz47bDwyMDE0MTkyNzs+PjtsPGk8MT47PjtsPHQ8O2w8aTwxPjtpPDM+O2k8NT47aTw3PjtpPDk+O2k8MTE+O2k8MTM+O2k8MTY+O2k8MjY+O2k8Mjc+O2k8Mjg+O2k8MzU+O2k8Mzc+O2k8Mzk+O2k8NDE+O2k8NDU+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOWtpuWPt++8mjIwMTQxOTI3Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlp5PlkI3vvJrojaPkv4o7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtpumZou+8muS/oeaBr+W3peeoi+WtpumZojs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85LiT5Lia77yaOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznvZHnu5zlt6XnqIs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOihjOaUv+ePre+8mjE0572R57ucMuePrTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MjAxNDA1MDM7Pj47Pjs7Pjt0PHQ8cDxwPGw8RGF0YVRleHRGaWVsZDtEYXRhVmFsdWVGaWVsZDs+O2w8WE47WE47Pj47Pjt0PGk8ND47QDxcZTsyMDE2LTIwMTc7MjAxNS0yMDE2OzIwMTQtMjAxNTs+O0A8XGU7MjAxNi0yMDE3OzIwMTUtMjAxNjsyMDE0LTIwMTU7Pj47Pjs7Pjt0PHA8O3A8bDxvbmNsaWNrOz47bDx3aW5kb3cucHJpbnQoKVw7Oz4+Pjs7Pjt0PHA8O3A8bDxvbmNsaWNrOz47bDx3aW5kb3cuY2xvc2UoKVw7Oz4+Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88dD47Pj47Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8ND47PjtsPHQ8O2w8aTwwPjtpPDE+Oz47bDx0PDtsPGk8MD47aTwxPjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+Oz47bDx0PEAwPDs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47Pj47dDw7bDxpPDA+Oz47bDx0PDtsPGk8MD47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47Pj47dDw7bDxpPDA+O2k8MT47PjtsPHQ8O2w8aTwwPjs+O2w8dDxAMDxwPHA8bDxWaXNpYmxlOz47bDxvPGY+Oz4+Oz47Ozs7Ozs7Ozs7Pjs7Pjs+Pjt0PDtsPGk8MD47PjtsPHQ8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs7Ozs7Ozs7Oz47Oz47Pj47Pj47dDw7bDxpPDA+Oz47bDx0PDtsPGk8MD47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8WkpVOz4+Oz47Oz47Pj47Pj47Pj47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjs+Pjs+jVLO2maoSf7hEF63hG5DUqWZn+Q=",
"ddlXN":"",
"ddlXQ":"",
"Button2":"(unable to decode value)"
}
data = urllib.urlencode(formdata)
url = "http://jw.jxust.edu.cn/xscj_gc.aspx?xh=20141927&xm=%C8%D9%BF%A1&gnmkdm=N121605"

request = urllib2.Request(url,data=data,headers=header)
response = urllib2.urlopen(request)

print response.read().decode('gbk')