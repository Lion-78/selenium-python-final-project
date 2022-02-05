from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button 'Add to basket' isn't displayed"

    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def product_name_is_presented(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def add_to_basket_message_is_presented(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADDING), "Message about adding is not presented"

    def should_item_in_basket(self):
        self.should_item_name_equal()
        self.should_item_cost_equal()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_not_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def should_item_name_equal(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == message, "No product name in the message about adding to basket"

    def should_item_cost_equal(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, "Prices in basket and in product page isn't equal"
