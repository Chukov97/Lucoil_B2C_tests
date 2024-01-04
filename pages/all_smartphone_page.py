from selene import browser, be


# vojoh86370@watrf.com
# Citilink2024!

class AllSmartphonePage:
    phone = 'a[title="Смартфон Huawei P60 Pro 8/256Gb,  MNA-LX9,  черный"]'

    def select_phone(self):
        return browser.element(self.phone).click()


all_smartphone_page = AllSmartphonePage()
