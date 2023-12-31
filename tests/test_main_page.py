import time

import allure
from pages.registration_page import registration_page
from test_data.card_data import VALID_CARD
from pages.main_page import main_page
from pages.base_page import base_page
from test_data.enums.card_level import CardLevel


class TestMainPage:

    @allure.title("Card level check")
    def test_card_level(self, browser_management):
        with allure.step("Open login page"):
            registration_page.open_page()
        with allure.step("Entering the card number"):
            registration_page.enter_card_number(VALID_CARD.card_number)
        with allure.step("Entering the password"):
            registration_page.enter_password(VALID_CARD.password)
            time.sleep(3)
        with allure.step("Click login button"):
            registration_page.click_login_button()
        card_level = main_page.get_card_level()
        with allure.step("Card level check"):
            base_page.assert_equals(CardLevel.BRONZE.value, card_level,
                                    f'Уровень карты - {card_level}, а должен быть {CardLevel.BRONZE.value}')

    @allure.title("Card number check")
    def test_card_number(self, browser_management):
        with allure.step("Open login page"):
            registration_page.open_page()
        with allure.step("Entering the card number"):
            registration_page.enter_card_number(VALID_CARD.card_number)
        with allure.step("Entering the password"):
            registration_page.enter_password(VALID_CARD.password)
            time.sleep(3)
        with allure.step("Click login button"):
            registration_page.click_login_button()
            card_number = main_page.get_card_number()
        with allure.step("Card number check"):
            base_page.assert_equals(VALID_CARD.card_number, card_number,
                                    f'Номер карты - {card_number}, а должен быть {VALID_CARD.card_number}')
