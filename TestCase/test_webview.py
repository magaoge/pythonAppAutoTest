import pytest
import yaml
from appium import webdriver
from PageObject.base_page import Basic
from TestData.login_data import login_success_data
from tools.initialize_driver import Initialize_driver
from appium.webdriver.common.mobileby import MobileBy
from PageObject.common_page import *
import time


from PageLocator.page_login import LoginPageElement as loc
from PageLocator.page_publiction import PublictionPageElement as poc
from PageLocator.page_webview import WebviewPageElement as weboc
from tools.path_maneger import appium_conf_path


class TestWebview:

    @pytest.mark.usefixtures("omit_login")
    def test_webview(self,omit_login):
        # data = {"Email": "Gaoge.Ma@Lexisnexis.com", "password": "1234567as",
        #         "expect": "可以是对 billing account 选择框是否出现的判断"}
        # 
        # driver = Initialize_driver.initialize_driver(noReset=True,)
        # driver.login_condition(data['Email'], data['password'])
        # *需要增加选择billing account的操作
        # driver.click_element(loc.billing_account, doc="选择billing account")
        # 2.等待welcome窗口的出现
        driver = omit_login
        time.sleep(10)

        # 这里的元素定位有问题，与代码无关，暂时不深究
        # driver.wait_element_Presence(poc.snooz_button, doc="等待welcome窗口的出现")
        # time.sleep(5)

        # 3.出现之后点击屏幕其他区域
        points = [(400,1100)]
        driver.tap_point(points)
        time.sleep(0.5)
        # # 4.点击···图标
        # # 导航栏的4个图标
        points2 = [(860,105)]
        driver.tap_point(points2)
        time.sleep(0.5)
        # 5.点击DL
        driver.click_element(poc.DL_button, doc="app内进入DL")
        # 5.1 等待APP内嵌浏览器页面加载
        # webview的className=android.webkit.WebView
        loater = (MobileBy.CLASS_NAME,"android.webkit.WebView")
        driver.wait_element_located(loater)
        # 5.2 进入webview内部
        # 注：后续写入公共方法的时候，需要获取全部的上下文句柄，然后遍历，再进入自己想要进入的句柄内

        driver.switch_context()
        print("开始继续往下运行")
        time.sleep(5)
        print("跳回默认的句柄")
        driver.switch_context(action="default")
        time.sleep(5)
        # 5.2 对APP内嵌浏览器页面进行还书操作（需要有chromedriver）
        driver.wait_element_located(weboc.return_button)
        driver.click_element(weboc.return_button, doc="点击第一个还书")
        pass

# if __name__ == '__main__':
#     TestWebview().test_webview()