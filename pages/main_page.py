from pages.base_page import BasePage
from locators import MainPageLocator as MPL

class MainPage(BasePage):
    def check_reg(self):
        expected_res = "Спасибо за регистрацию!"
        end = self.driver.find_element(*MPL.REGISTER_END).text
        assert end == expected_res