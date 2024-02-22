import time
import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    @staticmethod
    def format_locator(locator, *values):
        return locator[0], locator[1].format(*values)

    @allure.step
    def get_element(self, locator, timeout=0):
        self.logger.info(f"{self.class_name}: Getting visible element by {str(locator)}")
        timeout = self.browser.tolerance if not timeout else timeout
        try:
            return WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException as exc:
            self.logger.error(f"{self.class_name}: WebElement {str(locator)} is not visible", exc_info=True)
            raise AssertionError(f"WebElement {str(locator)} is not visible") from exc

    @allure.step
    def get_element_from_element(self, parent_locator, child_locator):
        self.logger.info(f"{self.class_name}: Getting visible element {str(child_locator)} "
                         f"from element {str(parent_locator)}")
        return self.get_element(parent_locator).find_element(*child_locator)

    @allure.step
    def get_elements_from_element(self, parent_locator, child_locator):
        self.logger.info(f"{self.class_name}: Getting all visible elements {str(child_locator)} "
                         f"from element {str(parent_locator)}")
        return self.get_element(parent_locator).find_elements(*child_locator)

    @allure.step
    def hover_and_click(self, locator, delay=0.1):
        element = self.get_element(locator)
        self.logger.info(f"{self.class_name}: Hover and click on element {locator}")
        ActionChains(self.browser).move_to_element(element).pause(delay).click().perform()

    @allure.step
    def click(self, locator):
        self.logger.info(f"{self.class_name}: Do click on {locator}")
        element = self.get_element(locator)
        element.click()

    @allure.step
    def set_file(self, locator, abs_path_to_file):
        self.logger.info(f"{self.class_name}: set file path in {locator} to {abs_path_to_file}")
        self.get_element(locator).send_keys(abs_path_to_file)

    @allure.step
    def set_select_field_by_value(self, locator, value):
        self.logger.info(f"{self.class_name}: Select {value} from {locator} select web element")
        select = Select(self.get_element(locator))
        select.select_by_value(str(value))

    @allure.step
    def set_field(self, locator, text):
        self.logger.info(f"Set field {locator} to {text}")
        element = self.get_element(locator)
        element.click()
        element.clear()

        if text:
            self.__send_keys_by_chars(element, text)

    @allure.step
    def __send_keys_by_chars(self, element, text, delay=0.1):
        for char in text:
            time.sleep(delay)
            element.send_keys(char)

    @allure.step
    def press_enter(self, locator):
        self.logger.info(f"{self.class_name}: Pressing 'ENTER' key on element {str(locator)}")
        self.get_element(locator).send_keys(Keys.RETURN)
        return self
