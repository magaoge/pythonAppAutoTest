# 1.引入第三方库
# import time

from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# 这里引用的appium的By定位方法，继承于selenium，同时扩展了定位方式
# from appium.webdriver.common.mobileby import MobileBy


# # 2.封装基本参数的字典
# desired_caps = {}
#
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
# print(desired_caps)

desired_caps = {
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "appPackage": "au.com.lexisnexis.lexisred.preview",
  "appActivity": "crc642b024b3494c14a21.NativeTourActivity"
}

# 3.实例驱动器对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

print("---------------------------------------------------------")

Email = 'Gaoge.Ma@Lexisnexis.com'
password = '1234567as'


# WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((MobileBy.ID,'au.com.lexisnexis.lexisred.preview:id/tvSkipTour')))

# 获取到当前窗口的总大小
# 返回值类型是字典：return {k: size[k] for k in ('width', 'height')}
# windowSize = driver.get_window_size()
# print(windowSize)
# small_x = windowSize['width'] *0.1
# y = windowSize['height']*0.5
# big_x = windowSize['width']*0.9
#
# # 向右划
# # swipe(self: T, start_x: int, start_y: int, end_x: int, end_y: int, duration: int = 0)
# print('我执行了吗？')
# time.sleep(1)
# driver.swipe(big_x,y,small_x,y,1000)
# time.sleep(1)
# # 向左划
# driver.swipe(small_x,y,big_x,y,1000)


# class
# driver.find_element(MobileBy.ID,'au.com.lexisnexis.lexisred.preview:id/tvSkipTour').click()
# # id
# driver.find_element(MobileBy.ID,'au.com.lexisnexis.lexisred.preview:id/etEmail').send_keys(Email)
# driver.find_element(MobileBy.ID,'au.com.lexisnexis.lexisred.preview:id/etPassword').send_keys(password)
#
# # 无，有机会再演示
# # driver.find_element_by_accessibility_id()
#
# # UiSelector,可以多条件组合搜索
# driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").resourceId("au.com.lexisnexis.lexisred.preview:id/ivRememberPasswordCheckBox")').click()
#
# driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("LOGIN")').click()
#
# TouchAction(driver)


