import time
from selene import browser, be
import allure
from test_data.card_data import VALID_CREDENTIALS, INVALID_CARD
from pages.base_page import base_page
from pages.main_page import main_page
from pages.all_smartphone_page import all_smartphone_page
from pages.smartphone_page import smartphone_page


class TestLogin:

    @allure.title("Successful login")
    def test_login_valid_card(self, browser_management):
        with allure.step("Open main page"):
            main_page.open_page()
        with allure.step("Open smartphone page"):
            main_page.click_smartphone_page()
        with allure.step("Select phone"):
            all_smartphone_page.select_phone()
        with allure.step("Get price phone"):
            phone_price = smartphone_page.get_price()
        with allure.step("Price phone check"):
            base_page.assert_equals('74 990', phone_price, f'Цена телефона {phone_price}, а должна быть 74 990')
