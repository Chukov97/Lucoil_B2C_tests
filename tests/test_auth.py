import time
from selene import browser, be
import allure
from test_data.card_data import VALID_CREDENTIALS, INVALID_CARD
from pages.base_page import base_page
from pages.main_page import main_page


class TestLogin:

    @allure.title("Successful login")
    def test_login_valid_card(self, browser_management):
        with allure.step("Open main page"):
            main_page.open_page()
        with allure.step("Open login form"):
            main_page.click_login()
        with allure.step("Entering the card number"):
            main_page.enter_login(VALID_CREDENTIALS.login)
        with allure.step("Entering the password"):
            main_page.enter_password(VALID_CREDENTIALS.password)
            time.sleep(3)
        with allure.step("Click login button"):
            main_page.click_login_button()
        # with allure.step("Сhecking the test on the page"):
        #     base_page.should_have_correct_text(element_selector=main_page.main_title,
        #                                        expected_text='Добрый день')

    @allure.title("Failed login")
    def test_login_invalid_card(self, browser_management):
        with allure.step("Open login page"):
            registration_page.open_page()
        with allure.step("Entering the card number"):
            registration_page.enter_card_number(INVALID_CARD.login)
        with allure.step("Entering the password"):
            registration_page.enter_password(INVALID_CARD.password)
            time.sleep(3)
        with allure.step("Click login button"):
            registration_page.click_login_button()
        with allure.step("Сhecking the test on the page"):
            base_page.should_have_correct_text(element_selector=registration_page.failed_login_form,
                                               expected_text='Номер карты или пароль введены неверно')
