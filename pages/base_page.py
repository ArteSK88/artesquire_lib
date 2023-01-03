from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.action_chains import ActionChains
import pickle


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.alert = Alert(self.driver)

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
        return self.actions.move_to_element(element).perform()

    def hover_n_click(self, locator1, locator2, time=10):
        outer_element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator1),
                                                               message=f'not find {locator1}')
        inner_element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator2),
                                                               message=f'not find {locator2}')
        self.actions.move_to_element(outer_element).perform()
        return self.actions.move_to_element(inner_element).click().perform()

    def drag_n_drop(self, locator, target_locator, frame_locator=None, locator_index=0, target_index=0,
                    frame_index=0, time=10):
        if frame_locator is not None:
            new_frame = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(frame_locator),
                                                               message=f'not find {frame_locator}')
            self.driver.switch_to.frame(new_frame[frame_index])
        else:
            pass
        draggable = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                               message=f'not find {locator}')
        drop_area = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(target_locator),
                                                               message=f'not find {target_locator}')
        return self.actions.drag_and_drop(draggable[locator_index], drop_area[target_index]).perform()

    def drag_n_drop_by_offset(self, locator, frame_locator=None, index=0, frame_index=0, time=10,
                              x_offset=0, y_offset=0):
        if frame_locator is not None:
            new_frame = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(frame_locator),
                                                               message=f'not find {frame_locator}')
            self.driver.switch_to.frame(new_frame[frame_index])
        else:
            pass
        draggable = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                               message=f'not find {locator}')
        return self.actions.drag_and_drop_by_offset(draggable[index], x_offset, y_offset).perform()

    def click_inside_overlay_menu(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                         message=f'not find {locator}')
        return self.actions.move_to_element(element).click().perform()

    def scroll_down(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up(self):
        return self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

    def scroll_to_element(self, locator, index=0, time=10):
        elements = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'not find {locator}')
        return elements[index].location_once_scrolled_into_view

    def catch_alert(self):
        return self.alert.text

    def accept_alert(self):
        return self.alert.accept()

    def dismiss_alert(self):
        return self.alert.dismiss()

    def save_cookies(self):
        return pickle.dump(self.driver.get_cookies(),
                           open("collected_data/cookies.txt", 'wb'))

    def load_cookies(self, cookiefile, url):
        self.driver.get(url)
        cookies = pickle.load(open(cookiefile, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
