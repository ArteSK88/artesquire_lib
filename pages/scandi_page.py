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
    PORTMEIRON_LOCATOR = (By.XPATH, '//figcaption[contains(text(), "Portmeirion")]')
    MUGS_N_CUPS_LOCATOR = (By.XPATH, '//a[contains(text(), "Mugs & Cups")]')
    WHITE_PORCELAIN_LOCATOR = (By.XPATH, '//a[contains(text(), "White Porcelain")]')
    GARDEN_SHOP_NOW_LOCATOR = (By.CSS_SELECTOR, "a.pagebuilder-button-primary")


class ScandiPlpLocators:
    SORT_BY_LOCATOR = (By.XPATH, '//label[contains(text(), "Sort By")]')
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
    def click_on_portmeirion(self):
        return self.find_element(ScandiHomePageLocators.PORTMEIRON_LOCATOR).click()

    def scroll_to_garden_shop_now(self):
        return self.scroll_to_element(locator=ScandiHomePageLocators.GARDEN_SHOP_NOW_LOCATOR, index=1)

    def hover_over_portmeirion(self):
        return self.hover_over_element(ScandiHomePageLocators.PORTMEIRON_LOCATOR)

    def hover_over_portmeirion_n_click_on_mugs_n_cups(self):
        return self.hover_n_click(ScandiHomePageLocators.PORTMEIRON_LOCATOR, ScandiHomePageLocators.MUGS_N_CUPS_LOCATOR)

    def click_on_mugs_n_cups(self):
        return self.click_inside_overlay_menu(ScandiHomePageLocators.MUGS_N_CUPS_LOCATOR)

    def click_on_white_porcelain(self):
        return self.click_inside_overlay_menu(ScandiHomePageLocators.WHITE_PORCELAIN_LOCATOR)


class ScandiPlpHelper(BasePage):
    def sort_by_price_ascending(self):
        self.find_element(ScandiPlpLocators.SORT_BY_LOCATOR).click()
        self.select_from_dropdown_by_text(ScandiPlpLocators.DROP_DOWN_LOCATOR, "Price: Low to High")

    def sort_by_price_descending(self):
        self.find_element(ScandiPlpLocators.SORT_BY_LOCATOR).click()
        self.select_from_dropdown_by_value(ScandiPlpLocators.DROP_DOWN_LOCATOR, "DESC price")



