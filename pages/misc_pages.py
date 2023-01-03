from selenium.webdriver.common.by import By
import time

from pages.base_page import BasePage


class JqeryLocators:
    FRAME_LOCATOR = (By.CSS_SELECTOR, "iframe.demo-frame")
    DROPPABLE_LOCATOR = (By.ID, "draggable")
    DROP_AREA_LOCATOR = (By.ID, "droppable")

class JqueryPageHelper(BasePage):
    def drag_element(self, x, y):
        return self.drag_n_drop_by_offset(locator=JqeryLocators.DROPPABLE_LOCATOR,
                                          frame_locator=JqeryLocators.FRAME_LOCATOR, x_offset=x, y_offset=y)

    def drop_element(self):
        return self.drag_n_drop(locator=JqeryLocators.DROPPABLE_LOCATOR,
                                target_locator=JqeryLocators.DROP_AREA_LOCATOR,
                                frame_locator=JqeryLocators.FRAME_LOCATOR)


class FlipKartLocators:
    SLIDER_LOCATOR = (By.CSS_SELECTOR, "div._3FdLqY")

class FlipKartPageHelper(BasePage):
    def move_left_slider(self, x):
        return self.drag_n_drop_by_offset(FlipKartLocators.SLIDER_LOCATOR, index=0, x_offset=x)

    def move_right_slider(self, x):
        return self.drag_n_drop_by_offset(FlipKartLocators.SLIDER_LOCATOR, index=1, x_offset=x)


class AsosLocators:
    ASOS_SELECT = (By.ID, 'main-size-select-0')

class AsosPageHelper(BasePage):
    def asos_select(self, visible_text):
        self.find_element(AsosLocators.ASOS_SELECT).click()
        self.select_from_dropdown_by_text(AsosLocators.ASOS_SELECT, visible_text)
        self.find_element(AsosLocators.ASOS_SELECT).click()


class RediffLocators:
    REDIFF_SUBMIT = (By.NAME, 'proceed')

class RediffPageHelper(BasePage):
    def rediff_submit(self):
        return self.find_element(RediffLocators.REDIFF_SUBMIT).click()


class VkLocators:
    EMAIL_FIELD = (By.ID, "index_email")
    ENTER_BUTTON = (By.XPATH, '//span[contains(text(), "Войти")]')
    PSWD_FIELD = (By.NAME, 'password')
    CONTINUE_BUTTON = (By.XPATH, '//span[contains(text(), "Продолжить")]')

class VkPageHelper(BasePage):
    def sign_in(self, user_data):
        time.sleep(2)
        self.find_element(VkLocators.EMAIL_FIELD).send_keys(user_data['username'])
        time.sleep(2)
        self.find_element(VkLocators.ENTER_BUTTON).click()
        time.sleep(2)
        self.find_element(VkLocators.PSWD_FIELD).send_keys(user_data['password'])
        time.sleep(2)
        self.find_element(VkLocators.CONTINUE_BUTTON).click()
        time.sleep(2)