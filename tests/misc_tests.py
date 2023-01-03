from test_data import TestUrls, VkCredentials
from pages.misc_pages import JqueryPageHelper, FlipKartPageHelper, AsosPageHelper, RediffPageHelper, VkPageHelper
import os
import time



def test_jquery_offset_drag(browser):
    jquery_page = JqueryPageHelper(browser)
    jquery_page.go_to_site(TestUrls.jquery)
    jquery_page.drag_element(150, 40)
    time.sleep(5)

def test_jquery_target_drop(browser):
    jquery_page = JqueryPageHelper(browser)
    jquery_page.go_to_site(TestUrls.jquery)
    jquery_page.drop_element()
    time.sleep(5)

def test_flipkart_slider(browser):
    flipkart_page = FlipKartPageHelper(browser)
    flipkart_page.go_to_site(TestUrls.flipkart)
    flipkart_page.move_left_slider(30)
    time.sleep(7)
    flipkart_page.move_right_slider(-90)
    time.sleep(5)

def test_asos(browser):
    asos_page = AsosPageHelper(browser)
    asos_page.go_to_site(TestUrls.asos)
    asos_page.asos_select("UK 8.5")
    time.sleep(10)

def test_rediff_alert(browser):
    rediff_page = RediffPageHelper(browser)
    rediff_page.go_to_site(TestUrls.rediff)
    rediff_page.rediff_submit()
    assert "Please enter a valid user name" in rediff_page.catch_alert()
    time.sleep(1)
    rediff_page.accept_alert()
    time.sleep(1)

def test_vk_collect_cookies(browser):
    vk_page = VkPageHelper(browser)
    vk_page.go_to_site(TestUrls.vk)
    vk_page.sign_in(VkCredentials.user_data)
    vk_page.save_cookies()
    time.sleep(5)

def test_vk_login_with_cookies(browser):
    vk_page = VkPageHelper(browser)
    cookiefile = os.path.join(os.path.dirname(__file__), 'collected_data/cookies.txt')
    vk_page.load_cookies(cookiefile=cookiefile, url=TestUrls.vk)
    time.sleep(5)