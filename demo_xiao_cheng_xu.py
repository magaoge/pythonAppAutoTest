# 1.引入第三方库
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 这里引用的appium的By定位方法，继承于selenium，同时扩展了定位方式
from appium.webdriver.common.mobileby import MobileBy

# 注：
# 启动appium时，要指定chromedriver.exe的目录，使用appium默认目录下的会报错(后期可以在代码中指定路径)
# 在切换小程序webview时，会去匹配chrome内核的驱动。在切换完成之后，再打印所有的打开的句柄
# 所以在指定一个非默认的目录下面的chromedriver.exe(X5内核对应的版本)，此问题就不会出现。
# 在appium server上设置chromedriver的路径

# 2.封装基本参数的字典
desired_caps = {}
# 支持X5内核应用自动化配置,是指关闭非安卓原生webview对话的时候，同时关闭对话
# 默认值为false
desired_caps["recreateChromeDriverSessions"] = True
# 使用的手机操作系统
desired_caps['platformName'] = 'Android'
# 手机操作系统的版本
desired_caps['platformVersion'] = '10'
# 使用的手机或模拟器类型
desired_caps['deviceName'] = 'bf09e850'
# 包名
desired_caps['appPackage'] = 'com.tencent.mm'
# 需要打开的首页名
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
# 无需重置会话
desired_caps["noReset"] = True

# chromeOptions使用来定制启动选项，因为在appium中切换context识别webview的时候
# 把com.tencent.mm:toosmp的webview识别成com.tencent.mm的webview
# 所以为了避免这个问题，加上AndroidProcess:com.tencent.mm:toolsm
# options = wb.chromeOptions()
# androidProcess值从命令中的进程pid的进程名获取
# options.add_experimental_option("androidProcess","com.tencent.mm:appbrand3")
desired_caps["chromeOptions"] = {"androidProcess":"com.tencent.mm:appbrand3"}
# 做自动化时使用的浏览器名字。如果是一个应用则只需填写个空的字符串
desired_caps["browserName"] = ""

# 3.实例驱动器对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,"new UiSelector().text('发现')")))
driver.find_element_by_android_uiautomator("new UiSelector().text('发现')").click()
WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,"new UiSelector().text('小程序')")))
driver.find_element_by_android_uiautomator("new UiSelector().text('小程序')").click()
WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,"new UiSelector().text('柠檬班')")))
driver.find_element_by_android_uiautomator("new UiSelector().text('柠檬班')").click()


# 获取当前上下文
cons = driver.contexts
print("当前所有的上下文为:",cons)

# 切换到小程序webview
driver.switch_to.context("WEBVIEW_com.tencent.mm:appbrand3")
# 即使是打开的小程序,也可能有多个页面,所以先去获取当前所有的窗口
hs = driver.window_handles
print("当前所有的窗口为:",hs)

for handle in hs:
    driver.switch_to.window(handle)
    print("切换的窗口为:",handle)
    time.sleep(5)
    if driver.page_source.find("每天一更") != -1:
        break

WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((MobileBy.XPATH,"//span[@style and text()='免费送书！《送柠檬班出版的纸质教科书》']")))
driver.find_element(By.XPATH,"//span[@style and text()='免费送书！《送柠檬班出版的纸质教科书》']").click()

driver.quit()



