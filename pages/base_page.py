from selene import browser, have


class BasePage:

    @staticmethod
    def should_have_correct_text(element_selector, expected_text):
        browser.element(element_selector).should(have.text(expected_text))

    @staticmethod
    def assert_equals(expected, actual, actual_msg):
        assert expected == actual, actual_msg


base_page = BasePage()
