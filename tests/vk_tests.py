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
    start_page.load_cookies(cookiefile=r'C:\Users\Artesk\PycharmProjects\art_esque_lib\tests\cookies.txt',
                            url=TestUrls.vk)
    time.sleep(5)
