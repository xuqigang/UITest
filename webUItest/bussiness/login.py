from cmath import log
import imp
from pytest import main
from selenium import webdriver
import sys
from common import common_sum
# sys.path.append("../commonshare")
# from bussiness.common import common_sum
# sys.path.append("Users/apple/Documents/Python/commonshare/common.py")
# from commonshare.common import common_sum
class login(common_sum):
    def login(self,user,pwd):
        self.open_url("http://vip.doumi.com/")
        self.click("class_name","login-btn")
        # if self.locateElement("class","userName") is None:
        self.input_data("id","phone_id",user)
        self.input_data("id","password_id",pwd)
        text=self.get_text("class_name","header_send_img")
        self.input_data("id","register_code",text)
        self.click("id","jz_submit_login")
if __name__=="__main__":
    log=login()
    log.login("14444445544","123456")

