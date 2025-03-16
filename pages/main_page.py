from pages.base_page import BasePage
from locators import MainPageLocator as MPL

class MainPage(BasePage):
    """
    Класс для работы с главной страницей.

    Наследует функциональность от BasePage и добавляет методы, специфичные для главной страницы.
    """

    def check_reg(self):
        """
        Проверяет успешность регистрации пользователя.

        Ожидаемый результат:
            - Сообщение "Thanks for registering!" должно отображаться на странице.

        Шаги:
            1. Получает текст элемента, указывающего на завершение регистрации, используя локатор MPL.REGISTER_END.
            2. Сравнивает полученный текст с ожидаемым сообщением.

        Исключения:
            - Если текст не совпадает с ожидаемым, выбрасывается AssertionError.
        """
        expected_res = "Thanks for registering!"
        end = self.driver.find_element(*MPL.REGISTER_END).text
        assert end == expected_res

    def go_to_profile(self):
        """
        Переходит в профиль пользователя.

        Шаги:
            1. Нажимает на кнопку перехода в профиль, используя локатор MPL.BUTTON_GO_TO_PROFILE.
        """
        self.driver.find_element(*MPL.BUTTON_GO_TO_PROFILE).click()
    