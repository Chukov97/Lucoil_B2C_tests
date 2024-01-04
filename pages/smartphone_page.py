from selene import browser, query


class SmartphonePage:
    price = 'div[data-meta-name="PriceBlock__price"]'

    def get_price(self):
        return browser.element(self.price).get(query.text)[:-1]


smartphone_page = SmartphonePage()
