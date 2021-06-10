from .base_page import BasePage
from .locators import LocatorsInBasket



class BasketPage(BasePage):
    def should_be_not_product_in_basket(self):
        assert self.is_not_element_present(*LocatorsInBasket.PRODUCT_IN_BASKET)

    def should_basket_is_empty(self):
        assert self.is_element_present(*LocatorsInBasket.BASKET_IS_EMPTY)

