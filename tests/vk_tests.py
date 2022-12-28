import os.path

from pages.vk_page import VkHelper
from test_data import TestUrls, VkCredentials
import time


def test_vk_collect_cookies(browser):
    auth_page = VkHelper(browser)
    auth_page.go_to_site(TestUrls.vk)
    auth_page.sign_in(VkCredentials.user_data)
    auth_page.save_cookies()
    time.sleep(5)


def test_vk_login_with_cookies(browser):
    start_page = VkHelper(browser)
    cookiefile = os.path.join(os.path.dirname(__file__), 'cookies.txt')
    start_page.load_cookies(cookiefile=cookiefile, url=TestUrls.vk)
    time.sleep(5)

