from playwright.sync_api import expect
from pages.base_page import BasePage
TEXT_EMPTY = 'В корзине нет товаров'
TEXT_EMPTY_RETURN_BUTTON = 'Вернуться к покупкам'

class CartPage(BasePage):
    url = 'https://www.citilink.ru/order/'

    def cart_is_empty(self):
        # Просто ищем по тексту - Playwright сам найдёт нужный элемент
        text_element = self.page.get_by_text('В корзине нет товаров')
        expect(text_element).to_be_visible()

    def click_cart_button_back(self):
        button = self.page.locator('a.e3gy1620')
        button.click()
        #self.page.wait_for_load_state('networkidle')



