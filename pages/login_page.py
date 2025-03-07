from pages.base_page import BasePage
from locators import LoginPageLocator as LPL
import random

class LoginPage(BasePage):
    def input_password_login(self, password):
        self.driver.find_element(*LPL.LINE_PASSWORD_LOGIN).send_keys(password)

    def input_password_reg1(self, password):
        self.driver.find_element(*LPL.LINE_PASSWORD1).send_keys(password)

    def input_password_reg2(self, password):
        self.driver.find_element(*LPL.LINE_PASSWORD2).send_keys(password)

    def click_button_login(self):
        self.driver.find_element(*LPL.BUTTON_LOG).click()

    def click_button_reg(self):
        self.driver.find_element(*LPL.BUTTON_REG).click()

    def click_button_forget_pass(self):
        self.driver.find_element(*LPL.BUTTON_FORGOT_PASSWORD).click()

    def input_line_email_reg(self, email):
        self.driver.find_element(*LPL.lINE_EMAIL_REG).send_keys(email)

    def input_line_email_log(self, email):
        self.driver.find_element(*LPL.lINE_EMAIL_LOG).send_keys(email)
    
    @staticmethod
    def gen_gmail():
        email = "tradllad" + str(random.randint(10, 100000000)) + "@gmail.ru"
        return email

    def login(self):
        self.input_line_email_log('eqwer12312@gmail.ru')
        self.input_password_login("QazQaz123")
        self.click_button_login()

    def register(self):
        self.input_line_email_reg(self.gen_gmail())
        self.input_password_reg1("QazQaz123")
        self.input_password_reg2("QazQaz123")
        self.click_button_reg()

    
        