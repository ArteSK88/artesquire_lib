import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="chromedriver", options=options)
    # driver = webdriver.Chrome(executable_path="chromedriver")
    yield driver
    driver.quit()




# python -m pytest -v --driver Chrome --driver-path */chromedriver  test.py
