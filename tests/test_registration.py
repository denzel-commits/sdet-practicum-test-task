import os

import allure

from configuration import TEST_DATA_PATH
from src.pages.student_registration import StudentRegistrationForm


class TestRegistration:
    @allure.title("Test student registration")
    def test_student_registration(self, browser):

        file = os.path.join(TEST_DATA_PATH, "picture.png")

        # preparations, can be added to setup fixture + another fixture with test data
        browser.execute_script("$('#fixedban').remove()")

        StudentRegistrationForm(browser)\
            .set_first_name("text")\
            .set_last_name("text")\
            .set_email("text")\
            .set_gender_female()\
            .set_mobile("text") \
            .set_date_of_birth(date=5, month=1, year=1984) \
            .set_subjects(["English", "Maths", "Chemistry"]) \
            .set_picture_file(file) \
            .set_hobbies_sports()\
            .set_hobbies_music()\
            .set_current_address("text, text text, country, city")

        assert True
