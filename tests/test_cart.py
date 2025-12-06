from playwright.sync_api import Page
from time import sleep
from pages.cart_page import CartPage

def test_is_cart_empty(page: Page):
    cart_page = CartPage(page)
    cart_page.open()
    cart_page.cart_is_empty()

def test_return_from_empty_cart(page: Page):
    cart_page = CartPage(page)
    test_is_cart_empty(page)
    cart_page.click_cart_button_back()


