from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import ProductPageLocators
import time
import pytest

links = [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", marks=pytest.mark.skip),
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", marks=pytest.mark.skip),
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", marks=pytest.mark.skip),
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", marks=pytest.mark.skip),
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", marks=pytest.mark.skip),
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", marks=pytest.mark.skip),
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", marks=pytest.mark.skip),
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9", marks=pytest.mark.skip)
        ]


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email, password)
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_authorized_user()

    @pytest.mark.parametrize('link', links)
    def test_user_cant_see_success_message(self, browser, link):
        # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        main_page = ProductPage(browser, link)
        main_page.open()
        main_page.should_not_be_success_message()

    @pytest.mark.parametrize('link', links)
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.product_name_is_presented()
        page.should_not_be_success_message()
        page.should_be_add_to_basket_btn()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        page.should_item_in_basket()

@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
      page = ProductPage(browser, link)
      page.open()
      page.should_not_be_success_message()

@pytest.mark.parametrize('link', links)
@pytest.mark.need_review
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

@pytest.mark.parametrize('link', links)
def test_guest_can_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_success_message()

@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', links)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.parametrize('link', links)
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_basket_not_contains_items()
    basket_page.should_message_basket_is_empty_is_present()

@pytest.mark.parametrize('link', links)
def test_guest_can_see_product_in_basket_opened_from_product_page(browser, link): #negative test
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_basket_contains_items()
    basket_page.should_message_basket_is_empty_is_not_present()
