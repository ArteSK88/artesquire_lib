import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ScandiAuthLocators:
    SIGN_IN_LINK_LOCATOR = (By.XPATH, '//span[contains(text(), "Sign in")]')
    CREATE_AN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button.Button_isHollow')
    SIGN_UP_BUTTON = (By.XPATH, '//button[contains(text(), "Sign up")]')
    SIGN_IN_BUTTON = (By.XPATH, '//button[contains(text(), "Sign in")]')
    LOG_OUT_BUTTON = (By.XPATH, '//button[contains(text(), "Logout")]')

    FIRST_NAME_LOCATOR = (By.ID, 'firstname')
    LAST_NAME_LOCATOR = (By.ID, 'lastname')
    EMAIL_LOCATOR = (By.ID, 'email')
    PASSWORD_LOCATOR = (By.ID, 'password')
    CONFIRM_PASSWORD_LOCATOR = (By.ID, 'confirm_password')
    WARNING_MESSAGE_LOCATOR = (By.CLASS_NAME, 'Field-Message')

    ACCOUNT_HEADING_LOCATOR = (By.CLASS_NAME, "MyAccount-Heading")

class ScandiHomePageLocators:
    HEADER_LOCATOR = (By.CSS_SELECTOR, "div.Header-ContactUs")
    SEARCH_FIELD_LOCATOR = (By.ID, 'search-field')
    SEARCH_FIELD_HINT_LOCATOR = (By.XPATH, '//article[@aria-label="Search results"]')
    SEARCH_HEADER_WRAPPER_LOCATOR = (By.CLASS_NAME, 'Header-SearchWrapper')
    OVERLAY_MENU_LOCATOR = (By.CSS_SELECTOR, "div.MenuOverlay-ItemList")
    PORTMEIRON_LOCATOR = (By.XPATH, '//figcaption[contains(text(), "Portmeirion")]')
    ALL_PORTMEIRION_LOCATOR = (By.XPATH, '//a[contains(text(), "All Portmeirion")]')
    NEW_IN_LOCATOR = (By.XPATH, '//figcaption[contains(text(), "New In")]')
    SALE_ROOM_LOCATOR = (By.XPATH, '//figcaption[contains(text(), "Sale Room")]')
    EMPTY_PAGE_LOCATOR = (By.CSS_SELECTOR, 'div.CmsBlock-Wrapper')
    MUGS_N_CUPS_LOCATOR = (By.XPATH, '//a[contains(text(), "Mugs & Cups")]')
    WHITE_PORCELAIN_LOCATOR = (By.XPATH, '//a[contains(text(), "White Porcelain")]')
    GARDEN_SHOP_NOW_LOCATOR = (By.CSS_SELECTOR, "a.pagebuilder-button-primary")
    FOOTER_MENU_LOCATOR = (By.CLASS_NAME, 'Footer-Menu')
    BLOG_LINK_LOCATOR = (By.XPATH, '//a[@href="/blog"]')
    BLOG_LOGO_LOCATOR = (By.XPATH, '//img[@alt="The Sophie Conran Blog"]')

class ScandiPlpLocators:
    PRODUCT_CARD_LOCATOR = (By.XPATH, '//a[@block="ProductCard"]')
    PRODUCT_IMAGE_LOCATOR = (By.CSS_SELECTOR, 'img.Image-Image')
    PRICE_LOCATOR = (By.XPATH, '//span[@itemprop="lowPrice"]')
    ITEMS_COUNTER_LOCATOR = (By.CSS_SELECTOR, 'div.ItemsCount')
    CATEGORY_PAGE_LOCATOR = (By.CSS_SELECTOR, 'main.CategoryPage')
    PAGE_TWO_LOCATOR = (By.XPATH, '//a[@aria-label="Page 2"]')
    NEXT_PAGE_LOCATOR = (By.XPATH, '//a[@aria-label="Next Page"]')
    SORT_BY_LOCATOR = (By.XPATH, '//label[contains(text(), "Sort By")]')
    SORT_BY_PRICE_ASC_LOCATOR = (By.ID, "oASC price")
    SORT_BY_PRICE_DESC_LOCATOR = (By.ID, "oDESC price")
    DROP_DOWN_LOCATOR = (By.XPATH, "//select[@id='category-sort']")


class ScandiAuthHelper(BasePage):
    def click_on_sign_in(self):
        return self.find_element(ScandiAuthLocators.SIGN_IN_LINK_LOCATOR).click()

    def create_an_account_with_invalid_data(self, user_data):
        self.find_element(ScandiAuthLocators.SIGN_IN_LINK_LOCATOR).click()
        self.find_element(ScandiAuthLocators.CREATE_AN_ACCOUNT_BUTTON).click()
        self.find_element(ScandiAuthLocators.FIRST_NAME_LOCATOR).send_keys(user_data['firstname'])
        self.find_element(ScandiAuthLocators.LAST_NAME_LOCATOR).send_keys(user_data['lastname'])
        self.find_element(ScandiAuthLocators.EMAIL_LOCATOR).send_keys(user_data['email'])
        self.find_element(ScandiAuthLocators.PASSWORD_LOCATOR).send_keys(user_data['password'])
        self.find_element(ScandiAuthLocators.CONFIRM_PASSWORD_LOCATOR).send_keys(user_data['confirming_password'])
        self.find_element(ScandiAuthLocators.SIGN_UP_BUTTON).click()


    def dashboard_title(self):
        return self.find_element(ScandiAuthLocators.ACCOUNT_HEADING_LOCATOR).text

    def sign_in(self, user_data):
        self.find_element(ScandiAuthLocators.SIGN_IN_LINK_LOCATOR).click()
        self.find_element(ScandiAuthLocators.EMAIL_LOCATOR).send_keys(user_data['email'])
        self.find_element(ScandiAuthLocators.PASSWORD_LOCATOR).send_keys(user_data['password'])
        self.find_element(ScandiAuthLocators.SIGN_IN_BUTTON).click()

    def click_on_logout(self):
        return self.find_element(ScandiAuthLocators.LOG_OUT_BUTTON).click()

    def warning_message(self):
        return self.find_element(ScandiAuthLocators.WARNING_MESSAGE_LOCATOR).text


class ScandiHomePageHelper(BasePage):
    def click_on_search(self):
        return self.find_element(ScandiHomePageLocators.SEARCH_FIELD_LOCATOR).click()

    def click_on_search_header(self):
        return self.find_element(ScandiHomePageLocators.SEARCH_HEADER_WRAPPER_LOCATOR).click()

    def click_on_header(self):
        return self.find_element(ScandiHomePageLocators.HEADER_LOCATOR).click()

    def search_hint_is_not_dispayed(self):
        return self.invisible_element(ScandiHomePageLocators.SEARCH_FIELD_HINT_LOCATOR)

    def click_on_new_in(self):
        return self.find_element(ScandiHomePageLocators.NEW_IN_LOCATOR).click()

    def hover_over_new_in(self):
        return self.hover_over_element(ScandiHomePageLocators.NEW_IN_LOCATOR)

    def click_on_sale_room(self):
        return self.find_element(ScandiHomePageLocators.SALE_ROOM_LOCATOR).click()

    def empty_page_message(self):
        return self.find_element([ScandiHomePageLocators.EMPTY_PAGE_LOCATOR][0]).text

    def all_portmeirion_is_not_visible(self):
        return self.invisible_element(ScandiHomePageLocators.ALL_PORTMEIRION_LOCATOR)

    def overlay_menu_is_not_visible(self):
        return self.invisible_element([ScandiHomePageLocators.OVERLAY_MENU_LOCATOR][0])

    def highlight_overlay_menu(self):
        return self.highlight_single_element([ScandiHomePageLocators.OVERLAY_MENU_LOCATOR][0])

    def click_on_portmeirion(self):
        return self.find_element(ScandiHomePageLocators.PORTMEIRON_LOCATOR).click()

    def hover_over_portmeirion(self):
        return self.hover_over_element(ScandiHomePageLocators.PORTMEIRON_LOCATOR)

    def click_on_all_portmeirion(self):
        return self.find_element(ScandiHomePageLocators.ALL_PORTMEIRION_LOCATOR).click()

    def hover_over_portmeirion_n_click_on_mugs_n_cups(self):
        return self.hover_n_click(ScandiHomePageLocators.PORTMEIRON_LOCATOR, ScandiHomePageLocators.MUGS_N_CUPS_LOCATOR)

    def scroll_to_garden_shop_now(self):
        return self.scroll_to_element(locator=ScandiHomePageLocators.GARDEN_SHOP_NOW_LOCATOR, index=1)

    def click_on_mugs_n_cups(self):
        return self.click_inside_overlay_menu(ScandiHomePageLocators.MUGS_N_CUPS_LOCATOR)

    def click_on_white_porcelain(self):
        return self.click_inside_overlay_menu(ScandiHomePageLocators.WHITE_PORCELAIN_LOCATOR)

    def scroll_to_footer_menu(self):
        self.scroll_to_element(ScandiHomePageLocators.FOOTER_MENU_LOCATOR)

    def click_on_blog(self):
        self.find_element(ScandiHomePageLocators.BLOG_LINK_LOCATOR).click()

    def blog_logo_image_size(self):
        return self.get_image_size(ScandiHomePageLocators.BLOG_LOGO_LOCATOR)


class ScandiPlpHelper(BasePage):
    def category_page_is_present(self):
        return self.find_element(ScandiPlpLocators.CATEGORY_PAGE_LOCATOR)

    def click_on_next_page(self):
        return self.find_element(ScandiPlpLocators.NEXT_PAGE_LOCATOR).click()

    def click_on_page_two(self):
        return self.find_element(ScandiPlpLocators.PAGE_TWO_LOCATOR).click()

    def count_product_cards(self):
        actual_number_of_products = len(self.find_elements(ScandiPlpLocators.PRODUCT_CARD_LOCATOR))
        displayed_number_of_products = \
            int(self.find_element(ScandiPlpLocators.ITEMS_COUNTER_LOCATOR).text.split(' ')[3]) + 1 \
               - int(self.find_element(ScandiPlpLocators.ITEMS_COUNTER_LOCATOR).text.split(' ')[1])
        return actual_number_of_products, displayed_number_of_products

    def items_total_counted_output(self):
        return int(self.find_element(ScandiPlpLocators.ITEMS_COUNTER_LOCATOR).text.split(' ')[5])

    def product_card_image_size(self, index):
        return self.get_image_size(ScandiPlpLocators.PRODUCT_IMAGE_LOCATOR, index=index)

    def presence_of_image(self, index):
        return self.check_presence_of_image(ScandiPlpLocators.PRODUCT_IMAGE_LOCATOR, index=index)

    def highlight_counter(self):
        self.move_to_element(ScandiPlpLocators.ITEMS_COUNTER_LOCATOR)
        time.sleep(1)
        return self.highlight_element(ScandiPlpLocators.ITEMS_COUNTER_LOCATOR)

    def highlight_product_image(self, index):
        self.move_to_element(ScandiPlpLocators.PRODUCT_IMAGE_LOCATOR)
        time.sleep(1)
        return self.highlight_element(ScandiPlpLocators.PRODUCT_IMAGE_LOCATOR, index=index)

    def highlight_price(self, index):
        self.move_to_element(ScandiPlpLocators.PRICE_LOCATOR)
        time.sleep(1)
        return self.highlight_element(ScandiPlpLocators.PRICE_LOCATOR, index=index)

    def sort_by_price_ascending(self):
        self.find_element(ScandiPlpLocators.SORT_BY_LOCATOR).click()
        self.find_element(ScandiPlpLocators.SORT_BY_PRICE_ASC_LOCATOR).click()

    def sort_by_price_descending(self):
        self.find_element(ScandiPlpLocators.SORT_BY_LOCATOR).click()
        self.find_element(ScandiPlpLocators.SORT_BY_PRICE_DESC_LOCATOR).click()

    def get_price_list(self):
        self.find_elements(ScandiPlpLocators.PRICE_LOCATOR)
        return [float(x.text) for x in self.find_elements(ScandiPlpLocators.PRICE_LOCATOR)]



