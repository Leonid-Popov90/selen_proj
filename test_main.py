from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.remote.webdriver import WebDriver
from pages.profile_page import ProfilePage

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
    """Проверка открытия главной страницы.

    Открывает главную страницу сайта и проверяет её доступность.

    Args:
        driver: WebDriver, используемый для взаимодействия с браузером.
    """
    page = MainPage(driver, "https://selenium1py.pythonanywhere.com/en-gb/")
    page.open()


def test_guest_can_login(driver):
    """Проверка возможности регистрации нового пользователя.

    Открывает страницу логина, выполняет регистрацию нового пользователя,
    затем проверяет успешность регистрации на главной странице.

    Args:
        driver: WebDriver, используемый для взаимодействия с браузером.
    """
    page = LoginPage(driver, 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
    page.open()
    page.register()
    page = MainPage(driver, driver.current_url)
    page.check_reg()


def test_guest_can_change_password(driver):
    """Проверка возможности смены пароля.

    Открывает страницу логина, выполняет регистрацию нового пользователя,
    переходит в профиль пользователя и проверяет доступность страницы профиля.

    Args:
        driver: WebDriver, используемый для взаимодействия с браузером.
    """
    page = LoginPage(driver, 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
    page.open()
    page.register()
    page = MainPage(driver, driver.current_url)
    page.go_to_profile()
    page = ProfilePage(driver, driver.current_url)


    



