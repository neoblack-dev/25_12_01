from playwright.sync_api import Page, expect
from time import sleep

def test_button_exists(page: Page):
    page.goto("https://www.citilink.ru/")
    sleep(5)
    button = page.get_by_role("button", name='Создать сборку')
    expect(button).to_be_visible()
    page.get_by_role("button", name='Создать сборку').click()
    sleep(5)




