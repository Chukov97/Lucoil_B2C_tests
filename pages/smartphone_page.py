from selene import browser, query


class SmartphonePage:
    price = 'div[data-meta-name="PriceBlock__price"]'
    add_to_cart_button = 'button[data-meta-name="BasketDesktopButton"]'
    go_to_cart_button = 'a.css-1k0cnlg.e1mnvjgw0 > button.e4uhfkv0.css-gh3izc.e4mggex0'

    def get_price(self):
        return browser.element(self.price).get(query.text)[:-1]

    def add_to_cart(self):
        return browser.element(self.add_to_cart_button).click()

    def go_to_cart(self):
        return browser.element(self.go_to_cart_button).click()


smartphone_page = SmartphonePage()
