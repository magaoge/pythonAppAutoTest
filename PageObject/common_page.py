# 这个页面负责封装的页面，是一些通用的功能，
# 比如一些软件的导航栏，并不属于任何页面，
# 或者是比如登录这种，许多行为的前置动作的行为，可以提取到这个页面进行管理
# 但是任何页面都会用到，所以将他们的功能封装在这里
import time

import yaml

from PageObject.base_page import Basic
from tools.path_maneger import *
from appium import webdriver
from PageLocator.page_login import LoginPageElement as loc
from PageLocator.page_publiction import PublictionPageElement as poc



class Common(Basic):

    def login_condition(self,Email,password):

        currentPage = self.driver.current_activity

        if currentPage.find('crc642b024b3494c14a21.NativeTourActivity') != -1:
            self.click_element(loc.skip_guide_button,doc="首次登录点击跳过指南")
            self.input_text(loc.email_input,Email,doc="输入登录邮箱")
            self.input_text(loc.password_input, password, doc="输入登录密码")
            self.click_element(loc.remember_pwd, doc="点击记住密码")
            self.click_element(loc.login_button, doc="点击确认登录")

            # 一定要等待，不然即使是time.sleep也无法有效的等待加载
            self.wait_element_located(loc.billing_account, doc="等待billing account窗口的出现")
            self.click_element(loc.billing_account, doc="选择billing account")
            self.click_element(loc.open_billing_account, doc="打开选中的billing account")


        elif currentPage.find('crc64ae60dead79d0657c.LoginActivity') != -1:
            self.input_text(loc.email_input, Email, doc="输入登录邮箱")
            self.input_text(loc.password_input, password, doc="输入登录密码")
            self.click_element(loc.remember_pwd, doc="点击记住密码")
            self.click_element(loc.login_button, doc="点击确认登录")
            time.sleep(1)
            # self.click_element(loc.billing_account, doc="选择billing account")
            self.wait_element_located(loc.open_billing_account, doc="等待billing account窗口的出现")
            self.click_element(loc.open_billing_account, doc="打开选中的billing account")

        elif currentPage.find('crc64d4d7368348c9cdda.MyPublicationsActivity') != -1:
            print("已经是登录状态")


