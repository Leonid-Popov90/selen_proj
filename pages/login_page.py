from pages.base_page import BasePage
from locators import LoginPageLocator as LPL
import random

class LoginPage(BasePage):
    """Класс для работы со страницей логина и регистрации.

    Этот класс предоставляет методы для взаимодействия с элементами страницы логина и регистрации,
    такие как ввод пароля, email, нажатие кнопок и генерация случайного email.
    """

    def input_password_login(self, password):
        """Вводит пароль в поле для ввода пароля на странице логина.

        Args:
            password (str): Пароль, который нужно ввести.
        """
        self.driver.find_element(*LPL.LINE_PASSWORD_LOGIN).send_keys(password)

    def input_password_reg1(self, password):
        """Вводит пароль в первое поле для ввода пароля на странице регистрации.

        Args:
            password (str): Пароль, который нужно ввести.
        """
        self.driver.find_element(*LPL.LINE_PASSWORD1).send_keys(password)

    def input_password_reg2(self, password):
        """Вводит пароль во второе поле для ввода пароля на странице регистрации.

        Args:
            password (str): Пароль, который нужно ввести.
        """
        self.driver.find_element(*LPL.LINE_PASSWORD2).send_keys(password)

    def click_button_login(self):
        """Нажимает кнопку 'Логин' на странице логина."""
        self.driver.find_element(*LPL.BUTTON_LOG).click()

    def click_button_reg(self):
        """Нажимает кнопку 'Регистрация' на странице регистрации."""
        self.driver.find_element(*LPL.BUTTON_REG).click()

    def click_button_forget_pass(self):
        """Нажимает кнопку 'Забыли пароль' на странице логина."""
        self.driver.find_element(*LPL.BUTTON_FORGOT_PASSWORD).click()

    def input_line_email_reg(self, email):
        """Вводит email в поле для ввода email на странице регистрации.

        Args:
            email (str): Email, который нужно ввести.
        """
        self.driver.find_element(*LPL.lINE_EMAIL_REG).send_keys(email)

    def input_line_email_log(self, email):
        """Вводит email в поле для ввода email на странице логина.

        Args:
            email (str): Email, который нужно ввести.
        """
        self.driver.find_element(*LPL.lINE_EMAIL_LOG).send_keys(email)
    
    @staticmethod
    def gen_gmail():
        """Генерирует случайный email в формате 'tradllad<число>@gmail.ru'.

        Returns:
            str: Сгенерированный email.
        """
        email = "tradllad" + str(random.randint(10, 100000000)) + "@gmail.ru"
        return email

    def login(self):
        """Выполняет процесс логина на сайте.

        Вводит заранее заданные email и пароль, затем нажимает кнопку 'Логин'.
        """
        self.input_line_email_log('eqwer12312@gmail.ru')
        self.input_password_login("QazQaz123")
        self.click_button_login()

    def register(self):
        """Выполняет процесс регистрации на сайте.

        Генерирует случайный email, вводит пароль и подтверждение пароля,
        затем нажимает кнопку 'Регистрация'.
        """
        self.input_line_email_reg(self.gen_gmail())
        self.input_password_reg1("QazQaz123")
        self.input_password_reg2("QazQaz123")
        self.click_button_reg()

    
        