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


class BasePageLocator:
    """Локаторы для базовой страницы.

    Содержит локаторы для элементов, которые присутствуют на всех страницах сайта.
    """

    LOGIN_BOTTON = (By.ID, "login_link")
    """Локатор кнопки для перехода на страницу логина."""

    OSCAR_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[1]/a')
    """Локатор кнопки 'Oscar' в шапке сайта."""

    LANGUAGE_BUTTON = (By.NAME, 'language')
    """Локатор кнопки выбора языка."""

    GO_LANGUAGE = (By.XPATH, '/html/body/div[1]/div[2]/div/form/button')
    """Локатор кнопки подтверждения выбора языка."""

    SEARCH_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[2]/div/div[2]/form/input')
    """Локатор кнопки поиска."""

    SEARCH_LINE = (By.ID, 'id_q')
    """Локатор строки поиска."""

    BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    """Локатор кнопки корзины."""


class LoginPageLocator:
    """Локаторы для страницы логина и регистрации."""

    lINE_EMAIL_REG = (By.NAME, "registration-email")
    """Локатор поля для ввода email при регистрации."""

    LINE_PASSWORD1 = (By.NAME, "registration-password1")
    """Локатор первого поля для ввода пароля при регистрации."""

    LINE_PASSWORD2 = (By.NAME, "registration-password2")
    """Локатор второго поля для ввода пароля при регистрации."""

    BUTTON_REG = (By.NAME, "registration_submit")
    """Локатор кнопки подтверждения регистрации."""

    lINE_EMAIL_LOG = (By.NAME, 'login-username')
    """Локатор поля для ввода email при логине."""

    LINE_PASSWORD_LOGIN = (By.NAME, 'login-password')
    """Локатор поля для ввода пароля при логине."""

    BUTTON_LOG = (By.NAME, 'login_submit')
    """Локатор кнопки подтверждения логина."""

    BUTTON_FORGOT_PASSWORD = (By.XPATH, '//*[@id="login_form"]/p/a')
    """Локатор кнопки 'Забыли пароль?'."""


class MainPageLocator:
    """Локаторы для главной страницы."""

    REGISTER_END = (By.CLASS_NAME, "alertinner")
    """Локатор сообщения об успешной регистрации."""

    BUTTON_GO_TO_PROFILE = (By.XPATH, '//*[@id="top_page"]/div[2]/div/ul/li[1]/a')
    """Локатор кнопки перехода в профиль пользователя."""


class ProfilePageLocator:
    """Локаторы для страницы профиля пользователя."""

    LINE_OLD_PASSWORD = (By.NAME, "old_password")
    """Локатор поля для ввода старого пароля."""

    LINE_NEW_PASSWORD1 = (By.NAME, "new_password1")
    """Локатор первого поля для ввода нового пароля."""

    LINE_NEW_PASSWORD2 = (By.NAME, "new_password2")
    """Локатор второго поля для ввода нового пароля."""

    BUTTON_SAVE_PASS = (By.XPATH, '//*[@id="change_password_form"]/div[4]/div/button')
    """Локатор кнопки сохранения нового пароля."""

    BUTTON_CANCEL_PASS = (By.XPATH, '//*[@id="change_password_form"]/div[4]/div/a')
    """Локатор кнопки отмены изменения пароля."""

    BUTTON_CHANGE_PASS = (By.XPATH, '//*[@id="default"]/div[2]/div/div/div/a[1]')
    """Локатор кнопки перехода к форме изменения пароля."""

    BUTTON_EDIT_PROFILE = (By.XPATH, '//*[@id="default"]/div[2]/div/div/div/a[2]')
    """Локатор кнопки перехода к форме редактирования профиля."""

    LINE_FIRST_NAME = (By.NAME, 'first_name')
    """Локатор поля для ввода имени."""

    LINE_LAST_NAME = (By.NAME, 'last_name')
    """Локатор поля для ввода фамилии."""

    LINE_EMAIL = (By.NAME, 'email')
    """Локатор поля для ввода email."""

    BUTTON_SAVE_NAME = (By.XPATH, '//*[@id="profile_form"]/div[4]/div/button')
    """Локатор кнопки сохранения изменений в профиле."""

    BUTTON_CANCEL_NAME = (By.XPATH, '//*[@id="profile_form"]/div[4]/div/button')
    """Локатор кнопки отмены изменений в профиле."""


class PtoductPageLocator:
    """Локаторы для страницы продукта."""

    NAME_OF_BOOK = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    """Локатор названия книги на странице продукта."""

    BUTTON_ADD_TO_BASKET = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    """Локатор кнопки 'Добавить в корзину'."""

    GREEN_LINE = (By.XPATH, '//*[@id="messages"]/div[1]')
    """Локатор зеленого сообщения (например, об успешном добавлении в корзину)."""
    
