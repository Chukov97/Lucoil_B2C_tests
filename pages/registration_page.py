from selene import browser


class RegistrationPage:
    input_card_number = 'input[name="cardNumber"]'
    input_password = 'input[name="password"]'
    login_button = '.Header-module__loginButton___dSht-'
    failed_login_form = 'p.modal__text'

    def open_page(self):
        browser.open('/')
        return self

    def enter_card_number(self, card_number):
        browser.element(self.input_card_number).type(card_number)

    def enter_password(self, password):
        browser.element(self.input_password).type(password)

    def click_login_button(self):
        browser.element(self.login_button).click()


registration_page = RegistrationPage()
