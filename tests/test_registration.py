import os
import allure
from configuration import TEST_DATA_PATH
from src.pages.student_registration import StudentRegistrationForm


@allure.feature("Registration")
class TestRegistration:
    @allure.title("Test student registration")
    def test_student_registration(self, browser, remove_ads, scroll_down, user_data):

        StudentRegistrationForm(browser)\
            .set_first_name(user_data["firstname"])\
            .set_last_name(user_data["lastname"])\
            .set_email(user_data["email"])\
            .set_gender(user_data["gender"])\
            .set_mobile(user_data["mobile"]) \
            .set_date_of_birth(**user_data["birthdate"]) \
            .set_subjects(user_data["subjects"]) \
            .set_picture_file(os.path.join(TEST_DATA_PATH, user_data["picture"])) \
            .set_hobbies(user_data["hobbies"])\
            .set_current_address(user_data["address"])\
            .set_state(user_data["state"])\
            .set_city(user_data["city"])\
            .click_submit_button()\
            .assert_modal_title("Thanks for submitting the form") \
            .assert_table_values(user_data)
