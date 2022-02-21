import pytest
import yaml

from PageObject.base_page import Basic
from appium import webdriver

from PageObject.common_page import Common
from PageObject.login_page import *
from TestData.login_data import *
from tools.initialize_driver import Initialize_driver

from tools.path_maneger import *
# @pytest.mark.usefixtures("initialize_driver")
# class TestLogin():
#
#     @pytest.mark.parametrize("data", login_success_data )
#     def test_login_success(self,data,initialize_driver):
#         LoginPage(initialize_driver).login_test(data['Email'],data['password'])


class TestLogin():
    @pytest.mark.parametrize("data", login_success_data )
    @pytest.mark.usefixtures("pre_login_Reset")
    def test_login(self,data,pre_login_Reset):
        driver = pre_login_Reset
        driver.login_condition(data['Email'], data['password'])
