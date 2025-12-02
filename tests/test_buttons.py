from playwright.sync_api import Page, expect
from time import sleep

def test_button_exists(page: Page):
    page.goto("https://www.wildberries.ru/catalog/126793555/detail.aspx")
    sleep(5)
    button = page.locator('.mo-button mo-button_view_fill mo-button_colors_brand mo-button_width_fill mo-button_size_large')
    expect.button.to_be_visible()




