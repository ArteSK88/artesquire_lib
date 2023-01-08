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


class ScandiHomePageLocators:
    HEADER_LOCATOR = (By.CSS_SELECTOR, "div.Header-ContactUs")
    PORTMEIRON_LOCATOR = (By.XPATH, '//figcaption[contains(text(), "Portmeirion")]')
    ALL_PORTMEIRION_LOCATOR = (By.XPATH, '//a[contains(text(), "All Portmeirion")]')
    NEW_IN_LOCATOR = (By.XPATH, '//figcaption[contains(text(), "New In")]')
    MUGS_N_CUPS_LOCATOR = (By.XPATH, '//a[contains(text(), "Mugs & Cups")]')
    WHITE_PORCELAIN_LOCATOR = (By.XPATH, '//a[contains(text(), "White Porcelain")]')
    GARDEN_SHOP_NOW_LOCATOR = (By.CSS_SELECTOR, "a.pagebuilder-button-primary")


class ScandiPlpLocators:
    PRODUCT_CARD_LOCATOR = (By.XPATH, '//a[@block="ProductCard"]')
    PRODUCT_IMAGE_LOCATOR = (By.CSS_SELECTOR, 'img.Image-Image')
    PRICE_LOCATOR = (By.XPATH, '//span[@itemprop="lowPrice"]')
    ITEMS_COUNTER_LOCATOR = (By.CSS_SELECTOR, 'div.ItemsCount')
    PAGE_TWO_LOCATOR = (By.XPATH, '//a[@aria-label="Page 2"]')
    NEXT_PAGE_LOCATOR = (By.XPATH, '//a[@aria-label="Next Page"]')
    SORT_BY_LOCATOR = (By.XPATH, '//label[contains(text(), "Sort By")]')
    SORT_BY_PRICE_ASC_LOCATOR = (By.ID, "oASC price")
    SORT_BY_PRICE_DESC_LOCATOR = (By.ID, "oDESC price")
    DROP_DOWN_LOCATOR = (By.XPATH, "//select[@id='category-sort']")


class ScandiAuthHelper(BasePage):
    def click_on_sign_in(self):
        return self.find_element(ScandiAuthLocators.SIGN_IN_LINK_LOCATOR).click()

    def create_an_account(self, user_data):
        self.find_element(ScandiAuthLocators.SIGN_IN_LINK_LOCATOR).click()
        self.find_element(ScandiAuthLocators.CREATE_AN_ACCOUNT_BUTTON).click()
        self.find_element(ScandiAuthLocators.FIRST_NAME_LOCATOR).send_keys(user_data['firstname'])
        self.find_element(ScandiAuthLocators.LAST_NAME_LOCATOR).send_keys(user_data['lastname'])
        self.find_element(ScandiAuthLocators.EMAIL_LOCATOR).send_keys(user_data['email'])
        password = user_data['password']
        self.find_element(ScandiAuthLocators.PASSWORD_LOCATOR).send_keys(password)
        self.find_element(ScandiAuthLocators.CONFIRM_PASSWORD_LOCATOR).send_keys(password)
        self.find_element(ScandiAuthLocators.SIGN_UP_BUTTON).click()

    def sign_in(self, user_data):
        self.find_element(ScandiAuthLocators.SIGN_IN_LINK_LOCATOR).click()
        self.find_element(ScandiAuthLocators.EMAIL_LOCATOR).send_keys(user_data['email'])
        self.find_element(ScandiAuthLocators.PASSWORD_LOCATOR).send_keys(user_data['password'])
        self.find_element(ScandiAuthLocators.SIGN_IN_BUTTON).click()

    def click_on_logout(self):
        return self.find_element(ScandiAuthLocators.LOG_OUT_BUTTON).click()


class ScandiHomePageHelper(BasePage):
    def click_on_new_in(self):
        return self.find_element(ScandiHomePageLocators.NEW_IN_LOCATOR).click()

    def click_on_portmeirion(self):
        return self.find_element(ScandiHomePageLocators.PORTMEIRON_LOCATOR).click()

    def scroll_to_garden_shop_now(self):
        return self.scroll_to_element(locator=ScandiHomePageLocators.GARDEN_SHOP_NOW_LOCATOR, index=1)

    def hover_over_portmeirion(self):
        return self.hover_over_element(ScandiHomePageLocators.PORTMEIRON_LOCATOR)

    def click_on_all_portmeirion(self):
        return self.find_element(ScandiHomePageLocators.ALL_PORTMEIRION_LOCATOR).click()

    def hover_over_portmeirion_n_click_on_mugs_n_cups(self):
        return self.hover_n_click(ScandiHomePageLocators.PORTMEIRON_LOCATOR, ScandiHomePageLocators.MUGS_N_CUPS_LOCATOR)

    def click_on_mugs_n_cups(self):
        return self.click_inside_overlay_menu(ScandiHomePageLocators.MUGS_N_CUPS_LOCATOR)

    def click_on_white_porcelain(self):
        return self.click_inside_overlay_menu(ScandiHomePageLocators.WHITE_PORCELAIN_LOCATOR)


class ScandiPlpHelper(BasePage):
    def click_on_next_page(self):
        return self.find_element(ScandiPlpLocators.NEXT_PAGE_LOCATOR).click()

    def click_on_page_two(self):
        return self.find_element(ScandiPlpLocators.PAGE_TWO_LOCATOR).click()

    def count_product_cards(self):
        return len(self.find_elements(ScandiPlpLocators.PRODUCT_CARD_LOCATOR))

    def items_on_page_counted_output(self):
        return int(self.find_element(ScandiPlpLocators.ITEMS_COUNTER_LOCATOR).text.split(' ')[3]) + 1 \
               - int(self.find_element(ScandiPlpLocators.ITEMS_COUNTER_LOCATOR).text.split(' ')[1])

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



