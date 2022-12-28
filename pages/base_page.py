from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.action_chains import ActionChains
import pickle


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'not find {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'not find {locator}')

    def select_from_dropdown_by_text(self, locator, visible_text, time=10):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                         message=f'not find {locator}')
        return Select(element).select_by_visible_text(visible_text)

    def select_from_dropdown_by_value(self, locator, value, time=10):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                         message=f'not find {locator}')
        return Select(element).select_by_value(value)

    def hover_over_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                         message=f'not find {locator}')
        hover = ActionChains(self.driver)
        return hover.move_to_element(element).perform()

    def hover_n_click(self, locator1, locator2, time=10):
        outer_element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator1),
                                                               message=f'not find {locator1}')
        inner_element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator2),
                                                               message=f'not find {locator2}')
        hover = ActionChains(self.driver)
        hover.move_to_element(outer_element).perform()
        return hover.move_to_element(inner_element).click().perform()

    def click_inside_overlay_menu(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                         message=f'not find {locator}')
        hover = ActionChains(self.driver)
        return hover.move_to_element(element).click().perform()

    def scroll_down(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up(self):
        return self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

    def scroll_to_element(self, locator, index, time=10):
        elements = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'not find {locator}')
        return elements[index].location_once_scrolled_into_view

    def save_cookies(self):
        return pickle.dump(self.driver.get_cookies(),
                           open("cookies.txt", 'wb'))

    def load_cookies(self, cookiefile, url):
        self.driver.get(url)
        cookies = pickle.load(open(cookiefile, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
