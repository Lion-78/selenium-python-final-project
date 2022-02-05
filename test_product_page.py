from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
import time
import pytest

links =[
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
        ]

@pytest.mark.parametrize('link', links)
@pytest.mark.skip
@pytest.mark.xfail(reason="I don't understand")
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    page.product_name_is_presented()
    page.should_not_be_success_message()

    page.should_be_add_to_basket_btn()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_item_in_basket()
    # time.sleep(10)

@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_success_message()

@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_disappeared_success_message()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.parametrize('link', links)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_basket_not_contains_items()
    # basket_page.should_basket_contains_items()
    basket_page.should_message_basket_is_empty_is_present()
    # basket_page.should_message_basket_is_empty_is_not_present()

@pytest.mark.parametrize('link', links)
def test_guest_can_see_product_in_basket_opened_from_product_page_1(browser, link): #negative test_1
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_basket_contains_items()

@pytest.mark.parametrize('link', links)
def test_guest_can_see_product_in_basket_opened_from_product_page_2(browser, link): #negative test_2
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_message_basket_is_empty_is_not_present()