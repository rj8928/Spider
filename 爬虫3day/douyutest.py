# coding=utf-8
from selenium import webdriver
import unittest
from bs4 import BeautifulSoup

class douyu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.num = 0
        self.count = 0
    def testdouyu(self):
        self.driver.get("https://www.douyu.com/directory/all")

        while True:
            elment = BeautifulSoup(self.driver.page_source,'lxml')

            elment = elment.select('#live-list-content')[0]
            # print elment
            # elment = BeautifulSoup(elment,'lxml')
            titles = elment.find_all('h3',{"class":"ellipsis"})
            names = elment.find_all('span',{"class":"dy-name ellipsis fl"})
            nums = elment.find_all('span',{"class":"dy-num fr"})

            for title,name,num in zip(titles,names,nums):
                print u"主播\t" + name.get_text().strip() + u"\t标题\t" + title.get_text().strip() + u"\t观看人数\t" + num.get_text().strip()

                self.num +=1
                num = num.get_text().strip()
                if num.find(u"万") != -1:
                    num = num.replace(u'万','')
                    # print num
                    num = float(num) * 10000

                num = int(num)
                self.count += num


            if self.driver.page_source.find("shark-pager-disable-next") != -1:
                break

            self.driver.find_element_by_xpath('//*[@id="J-pager"]/a[11]').click()

    def tearDown(self):
        print "总主播数" + str(self.num)
        print "总观众数" + str(self.count)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()