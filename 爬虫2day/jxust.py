# coding=utf-8
import urllib2
from lxml import etree
import urllib
import cookielib
from  PIL import Image
from bs4 import BeautifulSoup
import requests


class jxust():
    def __init__(self):
        self.header ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
                    }




    def getcode(self,codedata):
        url = "http://jw.jxust.edu.cn/"
        url2 = "http://jw.jxust.edu.cn/CheckCode.aspx/"

        # set_cookie = response.info()['Set-Cookie']
        # json_id = set_cookie.split(';')[0]
        # json_id = json_id.split('=')[-1]
        # print json_id

        with open('code.gif','wb') as f:
            f.write(codedata)
        image = Image.open("code.gif")
        image.show()
        code = raw_input("请输入验证码:")
        return code

        # value = content.xpath('//form/input/@value')
        # print value[0]
        #
        # return value[0],code


    def LoginSaveCookie(self,username,password):

        sess = requests.session()
        html = sess.get("http://jw.jxust.edu.cn/",headers = self.header).text
        bs = BeautifulSoup(html, 'lxml')
        # 获取页面_xsrf
        _viewstate = bs.find("input", attrs={"name": "__VIEWSTATE"}).get("value")
        codedata = sess.get("http://jw.jxust.edu.cn/CheckCode.aspx/",headers= self.header).content
        code = self.getcode(codedata)
        print _viewstate
        print code
        url = "http://jw.jxust.edu.cn/default2.aspx/"
        form = {
            "__VIEWSTATE": _viewstate,
                "txtUserName":username,
                "TextBox2":password,
            "txtSecretCode":code,
            "RadioButtonList1":"学生",
            "Button1":"",
            "lbLanguage":"",
            "hidPdrs":"",
            "hidsc":"",
        }
        response = sess.post(url,data = form , headers = self.header)
        print response.text
        # self.loadmarkPage(sessh)



    def loadmarkPage(self,sess):
        pass


    def delMarkPage(self):
        pass


    def saveMarkInfo(self):
        pass


    def StartWork(self,username,password):
        pass

if __name__ == "__main__":
    username = raw_input("请输入用户名：")
    password = raw_input("请输入密码:")
    login1 = jxust()
    login1.LoginSaveCookie(username,password)
