from selene import browser, query


class MainPage:
    cart = 'div[data-meta-name="BasketButton"][data-meta-count="0"]'
    login = '#__next > div > div.css-bo8bch.e1s351fz0 > div > div.css-1l8w4nq.es4sr930 > div > div > div.e1r0p2ss0.css-cvzj2n.e1loosed0 > div.css-1cs774w.e10bp8150 > div.css-1vb2hqj.e38q5fc0'
    smartphone = 'a[href="/catalog/smartfony/"]'
    login_form = 'input[name="login"]'
    password_form = 'input[name="pass"]'
    login_button = 'button.e4uhfkv0.css-ajbuym.e4mggex0'
    user_name = 'span.en3k2720.e106ikdt0.css-1rzz8dw.e1gjr6xo0[color="None"]'
    failed_login = '.LoginPageLayout__error-message'

    def open_page(self):
        browser.open('/')
        return self

    def click_cart(self):
        return browser.element(self.cart)

    def click_login(self):
        return browser.element(self.login).click()

    def click_smartphone_page(self):
        return browser.element(self.smartphone).click()

    def enter_login(self, login):
        browser.element(self.login_form).type(login)

    def enter_password(self, password):
        browser.element(self.password_form).type(password)

    def click_login_button(self):
        browser.element(self.login_button).click()

    def get_user_name(self):
        return browser.element(self.user_name).get(query.text)

    def get_failed_login_massage(self):
        return browser.element(self.failed_login).get(query.text)


main_page = MainPage()
