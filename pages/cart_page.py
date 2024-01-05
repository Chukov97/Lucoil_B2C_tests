from selene import browser, query


class CartPage:
    price = 'span[data-meta-is-total="notTotal"]'

    def get_price(self):
        return browser.element(self.price).get(query.text)[:-1]


cart_page = CartPage()
