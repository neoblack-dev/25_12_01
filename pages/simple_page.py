from playwright.sync_api import expect
BUTTON = 'Создать сборку'
TEXT = 'Конфигуратор ПК'

class SimplePage:
    def __init__(self, page):
        self.page = page

    def open_main(self):
        self.page.goto("https://www.citilink.ru/")

    def check_button_create(self):
        button = self.page.get_by_role("button", name=BUTTON)
        expect(button).to_be_visible()

    def click_button_create(self):
        button = self.page.get_by_role("button", name=BUTTON)
        button.click()

    def check_page_text(self):
        h1_element = self.page.locator('h1')
        expect(h1_element).to_have_text(TEXT)
