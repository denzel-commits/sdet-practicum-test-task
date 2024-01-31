import allure
from selenium.webdriver.common.by import By
from src.base_classes.base_page import BasePage


class StudentRegistrationForm(BasePage):
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#userEmail")
    # //following-sibling::label
    GENDER_MALE_RADIO = (By.XPATH, "//input[@name='gender' and @value='Male']//following-sibling::label")
    GENDER_FEMALE_RADIO = (By.XPATH, "//input[@name='gender' and @value='Female']//following-sibling::label")
    GENDER_OTHER_RADIO = (By.XPATH, "//input[@name='gender' and @value='Other']//following-sibling::label")

    MOBILE_INPUT = (By.CSS_SELECTOR, "#userNumber")

    DOB_DATE_PICKER_INPUT = (By.CSS_SELECTOR, "#dateOfBirthInput")

    DOB_MONTH_SELECT = (By.XPATH, "//div[@class='react-datepicker']//select[@class='react-datepicker__month-select']")
    DOB_YEAR_SELECT = (By.XPATH, "//div[@class='react-datepicker']//select[@class='react-datepicker__year-select']")
    # DOB_PREV_BUTTON = (By.XPATH, "//div[@class='react-datepicker']//button[contains(@class, 'react-datepicker__navigation--previous')]")
    # DOB_NEXT_BUTTON = (By.XPATH, "//div[@class='react-datepicker']//button[contains(@class, 'react-datepicker__navigation--next')]")

    SUBJECTS_INPUT = (By.CSS_SELECTOR, "#subjectsInput")

    HOBBIES_SPORTS_CHECKBOX = (By.XPATH, "//input[@id='hobbies-checkbox-1']//following-sibling::label")
    HOBBIES_READING_CHECKBOX = (By.XPATH, "//input[@id='hobbies-checkbox-2']//following-sibling::label")
    HOBBIES_MUSIC_CHECKBOX = (By.XPATH, "//input[@id='hobbies-checkbox-3']//following-sibling::label")

    PICTURE_FILE_INPUT = (By.XPATH, "//input[@type='file' and @id='uploadPicture']")

    ADDRESS_INPUT = (By.CSS_SELECTOR, "#currentAddress")

    STATE_SELECT = (By.CSS_SELECTOR, "#stateCity-wrapper div#state")
    CITY_SELECT = (By.CSS_SELECTOR, "#stateCity-wrapper div#city")

    # state menu
    # <div class =" css-26l3qy-menu" > < div class =" css-11unzgr" > < div class =" css-1n7v3ny-option" id="react-select-3-option-0" tabindex="-1" > NCR < / div > < div class =" css-yt9ioa-option" id="react-select-3-option-1" tabindex="-1" > Uttar Pradesh < / div > < div class =" css-yt9ioa-option" id="react-select-3-option-2" tabindex="-1" > Haryana < / div > < div class =" css-yt9ioa-option" id="react-select-3-option-3" tabindex="-1" > Rajasthan < / div > < / div > < / div >

    def _get_date_element(self, date):
        return self.get_element((By.XPATH,
                                 f"//div[contains(@class, 'react-datepicker__day')][text()='{date}']"))

    @allure.step("Set birthdate field to {date} {month} {year}")
    def set_date_of_birth(self, date, month, year):
        self.set_field(self.DOB_DATE_PICKER_INPUT, '')

        self.set_select_field_by_value(self.DOB_MONTH_SELECT, (month-1))
        self.set_select_field_by_value(self.DOB_YEAR_SELECT, year)
        self._get_date_element(date).click()

        return self

    @allure.step("Set first name field to {firstname}")
    def set_first_name(self, firstname):
        self.set_field(self.FIRST_NAME_INPUT, firstname)

        return self

    @allure.step("Set last name field to {lastname}")
    def set_last_name(self, lastname):
        self.set_field(self.LAST_NAME_INPUT, lastname)

        return self

    @allure.step("Set last name field to {email}")
    def set_email(self, email):
        self.set_field(self.EMAIL_INPUT, email)

        return self

    @allure.step("Set gender radio to male")
    def set_gender_male(self):
        self.hover_and_click(self.GENDER_MALE_RADIO)

        return self

    @allure.step("Set gender radio to female")
    def set_gender_female(self):
        self.hover_and_click(self.GENDER_FEMALE_RADIO)

        return self

    @allure.step("Set gender radio to other")
    def set_gender_other(self):
        self.hover_and_click(self.GENDER_OTHER_RADIO)

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

    @allure.step("Set hobbies to sports")
    def set_hobbies_sports(self):
        self.hover_and_click(self.HOBBIES_SPORTS_CHECKBOX)

        return self

    @allure.step("Set hobbies to sports")
    def set_hobbies_reading(self):
        self.hover_and_click(self.HOBBIES_READING_CHECKBOX)

        return self

    @allure.step("Set hobbies to sports")
    def set_hobbies_music(self):
        self.hover_and_click(self.HOBBIES_MUSIC_CHECKBOX)

        return self
