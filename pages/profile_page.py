from pages.base_page import BasePage
from locators import ProfilePageLocator as PPPL

class ProfilePage(BasePage):
    """
    Класс для работы со страницей профиля пользователя.

    Наследует функциональность от BasePage и предоставляет методы для взаимодействия
    с элементами страницы профиля, такими как изменение пароля, редактирование личных данных и т.д.
    """

    def input_new_password1(self, text):
        """
        Вводит новый пароль в первое поле для ввода пароля.

        Аргументы:
            text (str): Новый пароль, который нужно ввести.
        """
        self.driver.find_element(*PPPL.LINE_NEW_PASSWORD1).send_keys(text)

    def input_new_password2(self, text):
        """
        Вводит новый пароль во второе поле для подтверждения пароля.

        Аргументы:
            text (str): Новый пароль, который нужно подтвердить.
        """
        self.driver.find_element(*PPPL.LINE_NEW_PASSWORD2).send_keys(text)

    def input_old_password(self, text):
        """
        Вводит текущий (старый) пароль.

        Аргументы:
            text (str): Текущий пароль пользователя.
        """
        self.driver.find_element(*PPPL.LINE_OLD_PASSWORD).send_keys(text)

    def click_save_pass(self):
        """
        Нажимает кнопку сохранения нового пароля.
        """
        self.driver.find_element(*PPPL.BUTTON_SAVE_PASS).click()

    def click_cancel_pass(self):
        """
        Нажимает кнопку отмены изменения пароля.
        """
        self.driver.find_element(*PPPL.BUTTON_CANCEL_PASS).click()

    def click_change_password(self):
        """
        Нажимает кнопку для перехода в режим изменения пароля.
        """
        self.driver.find_element(*PPPL.BUTTON_CHANGE_PASS).click()

    def input_first_name(self, text):
        """
        Вводит новое имя пользователя.

        Аргументы:
            text (str): Новое имя пользователя.
        """
        self.driver.find_element(*PPPL.LINE_FIRST_NAME).send_keys(text)

    def input_last_name(self, text):
        """
        Вводит новую фамилию пользователя.

        Аргументы:
            text (str): Новая фамилия пользователя.
        """
        self.driver.find_element(*PPPL.LINE_LAST_NAME).send_keys(text)

    def input_email(self, text):
        """
        Вводит новый email пользователя.

        Аргументы:
            text (str): Новый email пользователя.
        """
        self.driver.find_element(*PPPL.LINE_EMAIL).send_keys(text)

    def click_save_name(self):
        """
        Нажимает кнопку сохранения изменений имени, фамилии и email.
        """
        self.driver.find_element(*PPPL.BUTTON_SAVE_NAME).click()

    def click_cancel_name(self):
        """
        Нажимает кнопку отмены изменений имени, фамилии и email.
        """
        self.driver.find_element(*PPPL.BUTTON_CANCEL_NAME).click()

    def click_edit_profile(self):
        """
        Нажимает кнопку для перехода в режим редактирования профиля.
        """
        self.driver.find_element(*PPPL.BUTTON_EDIT_PROFILE).click()


    
    
    
    