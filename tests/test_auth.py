import allure
from test_data.user_data import VALID_CREDENTIALS, INVALID_CREDENTIALS
from pages.base_page import base_page
from pages.main_page import main_page


class TestLogin:

    @allure.title("Successful login")
    def test_login_valid_credentials(self, browser_management):
        with allure.step("Open main page"):
            main_page.open_page()
        with allure.step("Open login form"):
            main_page.click_login()
        with allure.step("Entering the card number"):
            main_page.enter_login(VALID_CREDENTIALS.login)
        with allure.step("Entering the password"):
            main_page.enter_password(VALID_CREDENTIALS.password)
        with allure.step("Click login button"):
            main_page.click_login_button()
        with allure.step("Getting user name"):
            user_name = main_page.get_user_name()
        with allure.step("Сheck user name"):
            base_page.assert_equals('тест', user_name, f'Имя пользователя {user_name}, а должно быть тест')

    @allure.title("Failed login")
    def test_login_invalid_credentials(self, browser_management):
        with allure.step("Open main page"):
            main_page.open_page()
        with allure.step("Open login form"):
            main_page.click_login()
        with allure.step("Entering the card number"):
            main_page.enter_login(INVALID_CREDENTIALS.login)
        with allure.step("Entering the password"):
            main_page.enter_password(INVALID_CREDENTIALS.password)
        with allure.step("Click login button"):
            main_page.click_login_button()
        with allure.step("Get failed login massage"):
            failed_login_massage = main_page.get_failed_login_massage()
        with allure.step("Сheck failed login massage"):
            base_page.assert_equals('Неверный логин или пароль', failed_login_massage,
                                    f'Сообщение равно {failed_login_massage}, а должно быть "Неверный логин или пароль"')
