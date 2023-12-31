from selene import browser, have, query


class MainPage:
    main_title = 'h1.main__title'
    card_level = 'p.level-card__title'
    card_number = '//p[@class = "level-card__text"]'

    def get_card_level(self):
        return browser.element(self.card_level).get(query.text)

    def get_card_number(self):
        return browser.element(self.card_number).get(query.text)[-13::]


main_page = MainPage()
