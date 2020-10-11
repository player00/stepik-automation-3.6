class TestAddToBasketButton:
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    def test_add_to_basket_button(self, browser):
        browser.get(self.link)
        button = browser.find_elements_by_class_name("btn-add-to-basket")
        assert button, "button not found"
