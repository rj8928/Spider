# coding=utf-8

from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get("http://www.baidu.com/")

# 截屏
# driver.save_screenshot("baidu.png")

from selenium.webdriver.common.keys import Keys

# 输入文本
driver.find_element_by_id("kw").send_keys(u"游戏")

driver.save_screenshot("3.png")
# 点击事件
driver.find_element_by_xpath('//*[@id="su"]').click()

driver.save_screenshot("2.png")
# html源码
# print driver.page_source

