import pytest
from selenium.common import TimeoutException

from pages.scandi_page import ScandiAuthHelper, ScandiHomePageHelper, ScandiPlpHelper
from test_data import ScandiLogin, TestUrls
import time

"""demonstrates that logo size exceeds 35 kB"""
def test_blog_logo_size(browser):
    homepage = ScandiHomePageHelper(browser)
    homepage.go_to_site(TestUrls.scandiweb)
    homepage.scroll_to_footer_menu()
    homepage.click_on_blog()
    assert 10 <= homepage.blog_logo_image_size() <= 35

"""demonstrates the actual number of product cards does not match with the indicated with the counter 
and saves a screenshot with the counter border marked solid red"""
def test_product_cards_on_page_counter(browser, request):
    func_name = request.node.name
    homepage = ScandiHomePageHelper(browser)
    plp = ScandiPlpHelper(browser)
    homepage.go_to_site(TestUrls.scandiweb)
    homepage.hover_over_portmeirion()
    homepage.click_on_all_portmeirion()
    actual_number_of_products, displayed_number_of_products = plp.count_product_cards()
    if actual_number_of_products != displayed_number_of_products:
        plp.highlight_counter()
        plp.zoom(95)
        plp.save_screenshot(func_name)
    else:
        pass
    assert actual_number_of_products == displayed_number_of_products

"""demonstrates that the counter calculates the total number or product cards on all pages in category correctly"""
def test_product_cards_total_counter(browser):
    homepage = ScandiHomePageHelper(browser)
    plp = ScandiPlpHelper(browser)
    homepage.go_to_site(TestUrls.scandiweb)
    homepage.hover_over_portmeirion()
    homepage.click_on_all_portmeirion()
    product_cards_total = []
    try:
        while True:
            plp.count_product_cards()
            actual_number_of_products, _ = plp.count_product_cards()
            product_cards_total.append(actual_number_of_products)
            plp.click_on_next_page()
    except:
        pass
    assert sum(product_cards_total) == plp.items_total_counted_output()

"""detects all product cards with unuploaded or too small low quality images, 
marks them with red solid edge and saves screenshot"""
def test_plp_images_displayed(browser, request):
    func_name = request.node.name
    homepage = ScandiHomePageHelper(browser)
    plp = ScandiPlpHelper(browser)
    homepage.go_to_site(TestUrls.scandiweb)
    homepage.hover_over_portmeirion()
    homepage.click_on_all_portmeirion()
    actual_number_of_products, _ = plp.count_product_cards()
    all_images_sizes = []
    for i in range(actual_number_of_products):
        all_images_sizes.append(plp.product_card_image_size(i))
        if plp.product_card_image_size(i) < 10:
            plp.highlight_product_image(i)
    if min(all_images_sizes) < 10:
        plp.zoom(30)
        plp.save_screenshot(func_name)
    assert min(all_images_sizes) >= 10

"""trying various negative sign up scenarios, demonstrates the bugs when a user is successfully registered 
with special characters for firstname or lastname, whereas passwords do not match"""
@pytest.mark.parametrize("scenario", list(range(len(ScandiLogin.user_data))),
                         ids=[i['ids'] for i in ScandiLogin.user_data])
def test_create_new_account_with_invalid_data(browser, scenario):
    auth_page = ScandiAuthHelper(browser)
    auth_page.go_to_site(TestUrls.scandiweb)
    user_data = ScandiLogin.user_data[scenario]
    auth_page.create_an_account_with_invalid_data(user_data)
    try:
        if auth_page.dashboard_title() == "Dashboard":
            auth_page.click_on_logout()
    except:
        pass
    assert user_data['ER'] in auth_page.warning_message()

"""demonstrates that an applied filter does not work after switching to next page in category"""
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

"""demonstrates that sorting filter works correctly on the page where it is applied"""
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

"""demonstrates a bug when overlay menu does not disappear as expected when it is not hovered over"""
def test_overlay_menu(browser, request):
    homepage = ScandiHomePageHelper(browser)
    homepage.go_to_site(TestUrls.scandiweb)
    homepage.click_on_portmeirion()
    homepage.hover_over_new_in()
    try:
        assert homepage.overlay_menu_is_not_visible()
    except TimeoutException:
        homepage.highlight_overlay_menu()
        homepage.save_screenshot(request.node.name)
        raise AssertionError

"""demonstrates that SALE ROOM category is not populated with products.
Error message is not user friendly"""
def test_empty_page(browser):
    homepage = ScandiHomePageHelper(browser)
    plp = ScandiPlpHelper(browser)
    homepage.go_to_site(TestUrls.scandiweb)
    homepage.click_on_sale_room()
    time.sleep(3)
    assert (plp.category_page_is_present()) \
           or ('Sorry, currently we are not holding a sale' in homepage.empty_page_message())

"""demonstrates a bug when a hint under search field does not disappear as expected 
after clicking on blank area to the right of the search field"""
def test_search_hint(browser):
    homepage = ScandiHomePageHelper(browser)
    homepage.go_to_site(TestUrls.scandiweb)
    homepage.click_on_search()
    homepage.click_on_search_header()
    assert homepage.search_hint_is_not_dispayed()
