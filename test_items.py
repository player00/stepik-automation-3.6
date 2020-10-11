class TestAddToBasketButton:
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    def test_add_to_basket_button(self, browser):
        browser.get(self.link)
        assert browser.find_element_by_xpath("//form[@id='add_to_basket_form']/button")
