import pytest
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from test_data import TestUrls


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome(executable_path="chromedriver")
    yield driver
    driver.quit()




# python -m pytest -v --driver Chrome --driver-path */chromedriver  test.py
