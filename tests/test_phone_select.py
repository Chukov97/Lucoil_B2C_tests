import allure
from pages.base_page import base_page
from pages.main_page import main_page
from pages.all_smartphone_page import all_smartphone_page
from pages.smartphone_page import smartphone_page
from pages.cart_page import cart_page


class TestPhoneSelect:

    @allure.title("Check phone price")
    def test_check_phone_price(self, browser_management):
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

    @allure.title("Add phone to cart")
    def test_check_phone_price_in_cart(self, browser_management):
        with allure.step("Open main page"):
            main_page.open_page()
        with allure.step("Open smartphone page"):
            main_page.click_smartphone_page()
        with allure.step("Select phone"):
            all_smartphone_page.select_phone()
        with allure.step("Get price phone"):
            phone_price = smartphone_page.get_price()
        with allure.step("Add smartphone to cart"):
            smartphone_page.add_to_cart()
        with allure.step("Go to cart"):
            smartphone_page.go_to_cart()
        with allure.step("Get price phone in cart"):
            phone_price_in_cart = cart_page.get_price()
        with allure.step("Price phone check in cart"):
            base_page.assert_equals(phone_price, phone_price_in_cart,
                                    f'Цена телефона {phone_price_in_cart}, а должна быть {phone_price}')
