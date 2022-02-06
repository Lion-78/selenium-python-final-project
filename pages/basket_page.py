from .base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_basket_not_contains_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTAINS_ITEMS), "Basket contains items"

    def should_basket_contains_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_CONTAINS_ITEMS), "Basket not contains items"

    def should_message_basket_is_empty_is_present(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY),\
            "'Basket is not empty' is not present"

    def should_message_basket_is_empty_is_not_present(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY),\
            "'Basket is empty' is not present"