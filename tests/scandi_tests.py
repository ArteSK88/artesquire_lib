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


def test_product_cards_on_page_counter(browser, request):
    func_name = request.node.name
    scandipage = ScandiHomePageHelper(browser)
    plp_page = ScandiPlpHelper(browser)
    scandipage.go_to_site(TestUrls.scandiweb)
    scandipage.hover_over_portmeirion()
    scandipage.click_on_all_portmeirion()
    if plp_page.count_product_cards() != plp_page.items_on_page_counted_output():
        plp_page.highlight_counter()
        plp_page.zoom(95)
        plp_page.save_screenshot(func_name)
    else:
        pass
    assert plp_page.count_product_cards() == plp_page.items_on_page_counted_output()


def test_product_cards_total_counter(browser):
    scandipage = ScandiHomePageHelper(browser)
    plp_page = ScandiPlpHelper(browser)
    scandipage.go_to_site(TestUrls.scandiweb)
    scandipage.hover_over_portmeirion()
    scandipage.click_on_all_portmeirion()
    product_cards_total = []
    try:
        while True:
            cards_on_page = plp_page.count_product_cards()
            plp_page.count_product_cards()
            product_cards_total.append(cards_on_page)
            plp_page.click_on_next_page()
    except:
        pass
    assert sum(product_cards_total) == plp_page.items_total_counted_output()


def test_plp_images_displayed(browser, request):
    func_name = request.node.name
    scandipage = ScandiHomePageHelper(browser)
    plp_page = ScandiPlpHelper(browser)
    scandipage.go_to_site(TestUrls.scandiweb)
    scandipage.hover_over_portmeirion()
    scandipage.click_on_all_portmeirion()
    all_images_sizes = []
    for i in range(plp_page.count_product_cards()):
        all_images_sizes.append(plp_page.product_card_image_size(i))
        if plp_page.product_card_image_size(i) < 10:
            plp_page.highlight_product_image(i)
    if min(all_images_sizes) < 10:
        plp_page.zoom(30)
        plp_page.save_screenshot(func_name)
    assert min(all_images_sizes) >= 10


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


def test_sort_by_price_asc_on_page_two(browser, request):
    func_name = request.node.name
    homepage = ScandiHomePageHelper(browser)
    plp = ScandiPlpHelper(browser)
    homepage.go_to_site(TestUrls.scandiweb)
    homepage.click_on_new_in()
    plp.sort_by_price_ascending()
    plp.click_on_page_two()
    pricelist = plp.get_price_list()
    try:
        for i in range(1, len(pricelist)):
            if pricelist[i] < pricelist[i-1]:
                plp.highlight_price(i)
            assert pricelist[i] >= pricelist[i-1]
    except AssertionError:
        plp.zoom(80)
        plp.save_screenshot(func_name)
        raise AssertionError


def test_sort_by_price_desc(browser):
    homepage = ScandiHomePageHelper(browser)
    plp = ScandiPlpHelper(browser)
    homepage.go_to_site(TestUrls.scandiweb)
    homepage.click_on_new_in()
    plp.sort_by_price_descending()
    # time.sleep(3)
    pricelist = plp.get_price_list()
    for i in range(1, len(pricelist)):
        assert pricelist[i] <= pricelist[i-1]
