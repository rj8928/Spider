# coding=utf-8
import time
# 导入webdriver API对象  可以调用浏览器和操作页面
from selenium import webdriver
# 导入Keys 可模拟操控鼠标键盘
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()

driver.get("http://jw.jxust.edu.cn/")

# driver.save_screenshot("douban.png")

driver.find_element_by_name("txtUserName").send_keys("20141927")
driver.find_element_by_name("TextBox2").send_keys("589588aa")

driver.save_screenshot("jw.png")

icode = raw_input("请输入验证码：")
driver.find_element_by_name("txtSecretCode").send_keys(icode)

driver.save_screenshot("1.png")
# time.sleep(2)
# driver.find_element_by_id("Button1").send_keys(Keys.RETURN)
# time.sleep(2)
# 点击父元素 无效
# driver.find_element_by_xpath('//*[@id="form1"]/div/div[3]/dl[5]/dd').click()



# 模拟点击事件失效 尚未解决
# 点击元素
# driver.find_element_by_name('txtUserName').send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="Button1"]').click()
print 1
#
# 执行js点击
# js = "document.getElementsByClassName('btn_dl')[0].clickAndWait();"
# driver.execute_script(js)
driver.save_screenshot("denglu.png")
