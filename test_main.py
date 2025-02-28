from pages.main_page import MainPage

def test(driver):
    page = MainPage(driver, "https://selenium1py.pythonanywhere.com/en-gb/")
    page.open()
