import time

import allure
from pages.registration_page import registration_page
from test_data.card_data import VALID_CARD, INVALID_CARD
from pages.base_page import base_page
from pages.main_page import main_page


class TestLogin:

    @allure.title("Successful login")
    def test_login_valid_card(self, browser_management):
        with allure.step("Open login page"):
            registration_page.open_page()
        with allure.step("Entering the card number"):
            registration_page.enter_card_number(VALID_CARD.card_number)
        with allure.step("Entering the password"):
            registration_page.enter_password(VALID_CARD.password)
            time.sleep(3)
        with allure.step("Click login button"):
            registration_page.click_login_button()
        with allure.step("Сhecking the test on the page"):
            base_page.should_have_correct_text(element_selector=main_page.main_title,
                                               expected_text='Добрый день')

    @allure.title("Failed login")
    def test_login_invalid_card(self, browser_management):
        with allure.step("Open login page"):
            registration_page.open_page()
        with allure.step("Entering the card number"):
            registration_page.enter_card_number(INVALID_CARD.card_number)
        with allure.step("Entering the password"):
            registration_page.enter_password(INVALID_CARD.password)
            time.sleep(3)
        with allure.step("Click login button"):
            registration_page.click_login_button()
        with allure.step("Сhecking the test on the page"):
            base_page.should_have_correct_text(element_selector=registration_page.failed_login_form,
                                               expected_text='Номер карты или пароль введены неверно')
