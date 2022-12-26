from selenium.webdriver.common.by import By
from pages.base_page import BasePage

import time



class VkLocators:
    EMAIL_FIELD = (By.ID, "index_email")
    ENTER_BUTTON = (By.XPATH, '//span[contains(text(), "Войти")]')
    PSWD_FIELD = (By.NAME, 'password')
    CONTINUE_BUTTON = (By.XPATH, '//span[contains(text(), "Продолжить")]')


class VkHelper(BasePage):
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