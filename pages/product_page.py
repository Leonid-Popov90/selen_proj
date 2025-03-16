from pages.base_page import BasePage
from locators import PtoductPageLocator as PPL

class ProductPage(BasePage):
    def buy_book(self):
        """
        Добавляет книгу в корзину и проверяет, что сообщение о добавлении корректно.

        Шаги:
        1. Нажимает на кнопку "Добавить в корзину".
        2. Получает название книги со страницы.
        3. Получает текст сообщения о добавлении в корзину.
        4. Проверяет, что сообщение содержит название книги и текст о добавлении в корзину.

        Исключения:
        - Если кнопка "Добавить в корзину" не найдена, выбрасывается исключение.
        - Если название книги или сообщение не найдены, выбрасывается исключение.
        - Если сообщение не соответствует ожидаемому, выбрасывается AssertionError.
        """
        self.driver.find_element(*PPL.BUTTON_ADD_TO_BASKET).click()
        name = self.driver.find_element(*PPL.NAME_OF_BOOK).text
        message = self.driver.find_element(*PPL.GREEN_LINE).text
        assert name + " has been added to your basket." == message