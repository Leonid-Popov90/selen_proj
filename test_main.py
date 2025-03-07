from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.remote.webdriver import WebDriver

import selenium

import random

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

import math

from selenium.webdriver.support.ui import Select

import pytest

import os

def test(driver):
    page = MainPage(driver, "https://selenium1py.pythonanywhere.com/en-gb/")
    page.open()
    
def test_guest_can_login(driver):
    page = LoginPage(driver, 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
    page.open()
    page.register()
    page = MainPage(driver, driver.current_url)
    page.check_reg()
    



