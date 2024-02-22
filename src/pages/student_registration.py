import allure
from selenium.webdriver.common.by import By
from src.base_classes.base_page import BasePage
from src.helpers.utilities import map_user_data
from src.pages.elements.web_table import WebTableElement


class StudentRegistrationForm(BasePage):
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#userEmail")

    GENDER_RADIO = (By.XPATH, "//input[@name='gender' and @value='{}']//following-sibling::label")

    MOBILE_INPUT = (By.CSS_SELECTOR, "#userNumber")

    DOB_DATE_PICKER_INPUT = (By.CSS_SELECTOR, "#dateOfBirthInput")

    DOB_MONTH_SELECT = (By.XPATH, "//div[@class='react-datepicker']//select[@class='react-datepicker__month-select']")
    DOB_YEAR_SELECT = (By.XPATH, "//div[@class='react-datepicker']//select[@class='react-datepicker__year-select']")
    DOB_DATE_ITEM = (By.XPATH, "//div[contains(@class, 'react-datepicker__day')][text()='{}']")

    SUBJECTS_INPUT = (By.CSS_SELECTOR, "#subjectsInput")

    HOBBIES_CHECKBOX = (By.XPATH, "//input[contains(@id, 'hobbies-checkbox')]//following-sibling::label[text() = '{}']")

    PICTURE_FILE_INPUT = (By.XPATH, "//input[@type='file' and @id='uploadPicture']")

    ADDRESS_INPUT = (By.CSS_SELECTOR, "#currentAddress")

    STATE_SELECT = (By.CSS_SELECTOR, "#stateCity-wrapper div#state")
    STATE_SELECT_ITEM = (By.XPATH, "//div[@class=' css-26l3qy-menu']//div[text()='{}']")

    CITY_SELECT = (By.CSS_SELECTOR, "#stateCity-wrapper div#city")
    CITY_SELECT_ITEM = (By.XPATH, "//div[@class=' css-26l3qy-menu']//div[text()='{}']")

    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button#submit")

    MODAL_WINDOW_TITLE = (By.XPATH, "//div[contains(@class, 'modal-title')]")
    MODAL_WINDOW_TABLE = (By.XPATH, "//div[@class='modal-body']//table[contains(@class, 'table')]")

    @allure.step
    def click_submit_button(self):
        self.hover_and_click(self.SUBMIT_BUTTON)

        return self

    @allure.step("Set state field to {state}")
    def set_state(self, state):
        self.get_element(self.STATE_SELECT).click()
        self.hover_and_click(self.format_locator(self.STATE_SELECT_ITEM, state))

        return self

    @allure.step("Set city field to {city}")
    def set_city(self, city):
        self.get_element(self.CITY_SELECT).click()
        self.hover_and_click(self.format_locator(self.CITY_SELECT_ITEM, city))

        return self

    @allure.step("Set birthdate field to {date} {month} {year}")
    def set_date_of_birth(self, date, month, year):
        self.hover_and_click(self.DOB_DATE_PICKER_INPUT)

        self.set_select_field_by_value(self.DOB_MONTH_SELECT, (month-1))
        self.set_select_field_by_value(self.DOB_YEAR_SELECT, year)
        self.hover_and_click(self.format_locator(self.DOB_DATE_ITEM, date))

        return self

    @allure.step("Set first name field to {firstname}")
    def set_first_name(self, firstname):
        self.set_field(self.FIRST_NAME_INPUT, firstname)

        return self

    @allure.step("Set last name field to {lastname}")
    def set_last_name(self, lastname):
        self.set_field(self.LAST_NAME_INPUT, lastname)

        return self

    @allure.step("Set email field to {email}")
    def set_email(self, email):
        self.set_field(self.EMAIL_INPUT, email)

        return self

    @allure.step("Set gender radio to {gender}")
    def set_gender(self, gender):
        self.hover_and_click(self.format_locator(self.GENDER_RADIO, gender.capitalize()))

        return self

    @allure.step("Set mobile field to {mobile}")
    def set_mobile(self, mobile):
        self.set_field(self.MOBILE_INPUT, mobile)

        return self

    @allure.step("Set subjects field to {subjects}")
    def set_subjects(self, subjects):
        for subject in subjects:
            self.set_field(self.SUBJECTS_INPUT, subject)
            self.press_enter(self.SUBJECTS_INPUT)

        return self

    @allure.step("Set subjects field to {abs_path_to_file}")
    def set_picture_file(self, abs_path_to_file):
        self.set_file(self.PICTURE_FILE_INPUT, abs_path_to_file)

        return self

    @allure.step("Set current address field to {address}")
    def set_current_address(self, address):
        self.set_field(self.ADDRESS_INPUT, address)

        return self

    @allure.step("Set hobbies to {hobbies}")
    def set_hobbies(self, hobbies):
        for hobby in hobbies:
            self.hover_and_click(self.format_locator(self.HOBBIES_CHECKBOX, hobby))

        return self

    @allure.step("Modal title should be {title}")
    def assert_modal_title(self, title):
        assert title == self.get_element(self.MODAL_WINDOW_TITLE).text, f"Title is not equal to {title}"

        return self

    @allure.step("Compare modal window user data with test user data {user_data}")
    def assert_table_values(self, user_data):
        result_table_dict = WebTableElement(self.browser, self.MODAL_WINDOW_TABLE).get_dict()
        mapped_user_data = map_user_data(user_data)

        for key, value in result_table_dict.items():
            assert value == mapped_user_data[key], f"{value} is not equal to {mapped_user_data[key]}"

        return self
