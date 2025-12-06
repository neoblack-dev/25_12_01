from playwright.sync_api import Page
from time import sleep
from pages.simple_page import SimplePage


def test_button_exists(page: Page):
    simple_page = SimplePage(page)
    simple_page.open_main()
    sleep(1)
    simple_page.check_button_create()
    sleep(5)


def test_button_click(page: Page):
    simple_page = SimplePage(page)
    simple_page.open_main()
    sleep(1)
    simple_page.click_button_create()
    sleep(5)

def test_page_text_is_(page: Page):
    simple_page = SimplePage(page)
    simple_page.open_main()
    simple_page.click_button_create()
    simple_page.check_page_text()


