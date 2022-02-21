from appium import webdriver
# 1.引入pytest
import pytest

from TestData.login_data import login_success_data
from tools.initialize_driver import Initialize_driver
from tools.path_maneger import *
import os
import yaml

driver = None

# 做一个所有方法的前置动作，noReset=True，判断登录状况，并且返回appium driver对象
@pytest.fixture(scope="function")
def pre_login_noReset():
    driver = Initialize_driver.initialize_driver(noReset=True)
    yield driver


# 做一个所有方法的前置动作，noReset=False
@pytest.fixture(scope="function")
def pre_login_Reset():
    driver = Initialize_driver.initialize_driver()
    yield driver

# 省略登录


@pytest.fixture(scope="function")
def omit_login():
    driver = Initialize_driver.initialize_driver()
    driver.login_condition(login_success_data[0]['Email'], login_success_data[0]['password'])
    yield driver


# 3.声明一个函数级别的fixture
@pytest.fixture(scope="function")
def refresh():
    pass


def pytest_configure(config):
    marker_list = ["smoke"]  # 标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
