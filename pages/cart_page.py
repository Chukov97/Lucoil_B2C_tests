from selene import browser, query


class CartPage:
    price = 'span[data-meta-is-total="notTotal"]'
    clean_cart_button = 'div[data-meta-name="DeleteAction"]'
    clean_cart_text = 'div.css-0.e2u3r4f0'

    def get_price(self):
        return browser.element(self.price).get(query.text)[:-1]

    def clean_cart(self):
        return browser.element(self.clean_cart_button).click()

    def get_clean_cart_text(self):
        return browser.element(self.clean_cart_text).get(query.text)


cart_page = CartPage()
