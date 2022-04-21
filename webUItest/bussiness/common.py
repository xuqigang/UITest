from json.tool import main
from lib2to3.pgen2 import driver
from multiprocessing.sharedctypes import Value
from pydoc import locate
from sys import setdlopenflags
from unicodedata import name
from selenium import webdriver
import time

#浏览器操作封装到一个类中
class common_sum(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def open_url(self,url):
        self.driver.get(url)
        time.sleep(3)

    def locateElement(self,locate_type,value):
        el=None
        if locate_type=="id":
            el =self.driver.find_element_by_id(value)
        elif locate_type=="name":
            el =self.driver.find_element_by_name(value)
        elif locate_type=="class_name":
            el =self.driver.find_element_by_class_name(value)
        elif locate_type=="xpath":
            el=self.driver.find_element_by_xpath(value)
        elif locate_type=="css":
            el=self.driver.find_element_by_css_selector(value)
        elif locate_type=="tag_name":
            el=self.driver.find_element_by_tag_name(value)
        elif locate_type=="link_text":
            el=self.driver.find_element_by_link_text(value)
        if el is not None:
            return el

    def click(self,locate_type,value):
        el=self.locateElement(locate_type,value)
        el.click()
        time.sleep(3)

    def input_data(self,locate_type,value,data):
        el=self.locateElement(locate_type,value)
        el.send_keys(data)

    def get_text(self,locate_type,value):
        el=self.locateElement(locate_type,value)
        return el.text

    def __del__(self):
        time.sleep(3)
        self.driver.quit()

if __name__=='__main__':
    pass
