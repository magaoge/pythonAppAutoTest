from PageObject.base_page import Basic
from appium import webdriver
from PageLocator.page_login import LoginPageElement as loc

# # 2.封装基本参数的字典
# desired_caps = {}
# # 使用的手机操作系统
# desired_caps['platformName'] = 'Android'
# # 手机操作系统的版本
# desired_caps['platformVersion'] = '7.1'
# # 使用的手机或模拟器类型
# desired_caps['deviceName'] = 'Android Emulator'
# # 包名
# desired_caps['appPackage'] = 'au.com.lexisnexis.lexisred.preview'
# # 需要打开的首页名
# desired_caps['appActivity'] = 'crc642b024b3494c14a21.NativeTourActivity'
#
# # 3.实例驱动器对象
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)



class LoginPage(Basic):

    # 保留，因为毕竟登录是登陆页面的功能，目前是与Common中的方法重复，
    # 而且在执行测试的时候，也没有用到，看后续是否有必要保留
    def login_test(self,Email,password):
        self.click_element(loc.skip_guide_button,doc="首次登录点击跳过指南")
        self.input_text(loc.email_input,Email,doc="输入登录邮箱")
        self.input_text(loc.password_input, password, doc="输入登录密码")
        self.click_element(loc.remember_pwd, doc="点击记住密码")
        self.click_element(loc.login_button, doc="点击确认登录")
        # 要根据页面的activity来判断用户是否登录成功了
        self.click_element(loc.billing_account,doc="选择billing account")

# if __name__ == '__main__':
#     LoginPage().login_test()