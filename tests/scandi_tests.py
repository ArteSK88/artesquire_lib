from pages.scandi_page import ScandiAuthHelper, ScandiHomePageHelper, ScandiPlpHelper
from test_data import ScandiLogin, TestUrls
import time


def test_scroll_to_element(browser):
    scandipage = ScandiHomePageHelper(browser)
    scandipage.go_to_site(TestUrls.scandiweb)
    time.sleep(1)
    scandipage.scroll_to_garden_shop_now()
    time.sleep(2)
    scandipage.scroll_down()
    time.sleep(2)
    scandipage.scroll_up()
    time.sleep(1)


def test_first_scandi_hover_n_click(browser):
    scandipage = ScandiHomePageHelper(browser)
    scandipage.go_to_site(TestUrls.scandiweb)
    scandipage.hover_over_portmeirion_n_click_on_mugs_n_cups()
    time.sleep(5)


def test_second_scandi_hover_n_click(browser):
    scandipage = ScandiHomePageHelper(browser)
    scandipage.go_to_site(TestUrls.scandiweb)
    scandipage.hover_over_portmeirion()
    # time.sleep(2)
    scandipage.click_on_mugs_n_cups()
    time.sleep(5)


def test_create_new_account(browser):
    auth_page = ScandiAuthHelper(browser)
    auth_page.go_to_site(TestUrls.scandiweb)
    auth_page.create_an_account(ScandiLogin.user_data)
    time.sleep(5)


def test_sign_in_and_log_out(browser):
    auth_page = ScandiAuthHelper(browser)
    auth_page.go_to_site(TestUrls.scandiweb)
    auth_page.sign_in(ScandiLogin.user_data)
    auth_page.click_on_logout()
    time.sleep(5)


def test_sort_by_price_asc(browser):
    homepage = ScandiHomePageHelper(browser)
    plp = ScandiPlpHelper(browser)
    homepage.go_to_site(TestUrls.scandiweb)
    homepage.hover_over_portmeirion()
    homepage.click_on_white_porcelain()
    plp.sort_by_price_ascending()
    time.sleep(2)
    plp.scroll_down()
    time.sleep(2)
    plp.scroll_up()
    time.sleep(2)


def test_sort_by_price_desc(browser):
    homepage = ScandiHomePageHelper(browser)
    plp = ScandiPlpHelper(browser)
    homepage.go_to_site(TestUrls.scandiweb)
    homepage.hover_over_portmeirion()
    homepage.click_on_white_porcelain()
    plp.sort_by_price_descending()
    time.sleep(10)


def test_asos(browser):
    homepage = ScandiHomePageHelper(browser)
    plp = ScandiPlpHelper(browser)
    homepage.go_to_site("https://www.asos.com/adidas-originals/adidas-originals-oznova-trainers-in-off-white-and-grey/prd/202527704?colourWayId=202527705&cid=1935")
    plp.asos_select("UK 8.5")
    time.sleep(10)
