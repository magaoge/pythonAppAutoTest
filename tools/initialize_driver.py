import yaml
from appium import webdriver
from tools.path_maneger import appium_conf_path
from PageObject.common_page import Common

class Initialize_driver:
    @classmethod
    def initialize_driver(cls, sever_point=4723, noReset=None, automationName=None, **kwargs):
        # 这里可能由于python3的原因，将字符串识别为Unicode字符串，与正则存在冲突，所以加上r来格式化字符串
        r"""
        :param sever_point: 指定appium运行的服务端口
        :param noReset: True、False  是否删除app缓存， 默认False重置session
        :param automationName:  自动化测试的引擎，如果要抓取toast窗口，必须要重新设值为：UiAutomator2
        :param kwargs:用来修改appium其他参数值
        :return:
        """

        # 读取配置文件appium中的配置信息：
        strm = open(appium_conf_path, 'r', encoding="utf-8")
        desired_caps = yaml.safe_load(strm)

        # 可以自定义部分appium参数
        if noReset is not None:
            desired_caps['noReset'] = noReset
        if automationName is not None:
            desired_caps['automationName'] = automationName

        for kwarg in kwargs:
            desired_caps[kwarg] = kwargs[kwarg]
        appium_driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(sever_point), desired_caps)
        driver = Common(appium_driver)
        return driver