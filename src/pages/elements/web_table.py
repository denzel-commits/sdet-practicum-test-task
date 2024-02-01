import allure
from selenium.webdriver.common.by import By

from src.base_classes.base_page import BasePage


class WebTableElement(BasePage):
    ROWS = (By.CSS_SELECTOR, "tr")
    COLS = (By.CSS_SELECTOR, "tr:first-child>td")

    def __init__(self, browser, locator):
        super().__init__(browser)
        self._webtable = locator

    @allure.step
    def get_rows_count(self):
        return len(self.get_elements_from_element(self._webtable, self.ROWS))

    @allure.step
    def get_cols_count(self):
        return len(self.get_elements_from_element(self._webtable, self.COLS))

    @allure.step
    def get_dict(self):
        rows_count = self.get_rows_count()
        result_dict = {}

        for row in range(1, rows_count):
            title = self.get_element_from_element(self._webtable, (By.XPATH, f"//tbody//tr[{row}]/td[1]")).text
            value = self.get_element_from_element(self._webtable, (By.XPATH, f"//tbody//tr[{row}]/td[2]")).text
            result_dict[title] = value

        return result_dict
