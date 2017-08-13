ua_headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
}

# //div[@class="threadlist_lz clearfix"]//a[@class="j_th_tit "]/@href

# //img[@class="BDE_Image"]/@src


# //div[@class="btn"]//input[1]/@value  jxust登录值

form ={
"useValidateCode":"0",
"isremenberme":"0",
"ip":"",
"username":"20141927",
"password":"589588aa11",
"losetime":"240",
"lt":"_cEFE60101-0A84-FFB7-9076-70486CBDCB4D_k65C4A858-C9B0-7BB3-89BC-5A06D931E76D",
"_eventId":"submit",
"submit1":"",
}


url = "http://ca.jxust.edu.cn/zfca/login?service=http%3A%2F%2Fportal.jxust.edu.cn%2Fportal.do"

# header ={
#
#
# "Origin": "http://ca.jxust.edu.cn"
#
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
#
# "Referer": "http://ca.jxust.edu.cn/zfca/login"
#
# "Cookie": "JSESSIONID=D5DF5CA676DB184EBC78CFDD9AFA1B54"
# }


# title2 = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extarct()
    #num = title.split('')[-1].split(':')[-1]
    #title = title.split('')[0]
    # info = response.xpath('//div[@class="c1 text14_2"]/text()')
    # status = response.xpath('//span[@class="qblue"]/text()')
    #start_urls = ["http://d.wz.sun0769.com/index.php/question/huiyin?page=0"]


    # 世纪佳缘
    """
    
    照片
    //img[@class="img_absolute"]/@src
    
    请求post地址
    http://search.jiayuan.com/v2/search_v2.php   p为页数
    
    for user in response["userinfo"]:
    uid = user[""realUid""]
    
    url = "http://www.jiayuan.com/" + uid + "/"
    
    
    
    
    http://www.jiayuan.com/164771295?fxly=search_v2
    
          formdata{  
        sex:f
        key:
        stc:1:36,2:20.28,23:1
        sn:default
        sv:1
        p:3 
        f:
        listStyle:bigPhoto
        pri_uid:167374339
        jsversion:v5
            }
            
    //img[@class="img_absolute"]/@src
    
    frominfo //h6[@class="member_name"]
    list  = frominfo.split("，")
    age = list[0]
    status = list[1]
    address = list[2][6:]
    
    info //ul[@class="member_info_list fn-clear"]//li 12456 学历 身高 月薪 住房 体重
    
    jianjie //div[@class="js_text"]
      
    zeouyaoqiu //div[@class="bg_white mt15"][2]//li 124 年龄 身高 学历
    
    
    登录
    https://passport.jiayuan.com/dologin.php?host=www.jiayuan.com&new_header=1&channel=index
    
    formdata{
    channel:200
position:201
name:15570080949
password:892806304
remem_pass:on
    }
    
    
    """