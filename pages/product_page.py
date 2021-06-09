from .base_page import BasePage
from .locators import AddToBasketLocators



class ProductPage (BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*AddToBasketLocators.ADD_TO_BASKET)
        link.click()
        self.solve_quiz_and_get_code()
        return ProductPage(browser=self.browser, url=self.browser.current_url)

    def should_text_book(self):
        book_name = self.browser.find_element(*AddToBasketLocators.BOOK_NAME).text
        book_name_in_alert = self.browser.find_element(*AddToBasketLocators.BOOK_NAME_IN_ALERT).text
        assert book_name == book_name_in_alert, "Name book is not presented"

    def should_sum_of_basket(self):
        book_price = self.browser.find_element(*AddToBasketLocators.PRICE_BOOK).text
        sum_basket = self.browser.find_element(*AddToBasketLocators.SUM_IN_BASKET).text
        assert book_price == sum_basket, "Sum basket is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*AddToBasketLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappered(self):
        assert self.is_disappeared(*AddToBasketLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
