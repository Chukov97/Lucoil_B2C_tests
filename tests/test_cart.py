import allure
from pages.base_page import base_page
from pages.main_page import main_page
from pages.all_smartphone_page import all_smartphone_page
from pages.smartphone_page import smartphone_page
from pages.cart_page import cart_page


class TestCart:

    @allure.title("Clear cart")
    def test_check_phone_price_in_cart(self, browser_management):
        with allure.step("Open main page"):
            main_page.open_page()
        with allure.step("Open smartphone page"):
            main_page.click_smartphone_page()
        with allure.step("Select phone"):
            all_smartphone_page.select_phone()
        with allure.step("Add smartphone to cart"):
            smartphone_page.add_to_cart()
        with allure.step("Go to cart"):
            smartphone_page.go_to_cart()
        with allure.step("Clear cart"):
            cart_page.clean_cart()
        with allure.step("Get text after clear cart"):
            text = cart_page.get_clean_cart_text()
        with allure.step("Check text after clear cart"):
            base_page.assert_equals(f'В корзине нет товаров', text,
                                    f'Текст в пустой корзине - {text}, а должен быть "В корзине нет товаров"')
