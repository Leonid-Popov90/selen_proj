import time
import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
  driver = webdriver.Chrome()
  yield driver
  time.sleep(1)
  driver.quit()