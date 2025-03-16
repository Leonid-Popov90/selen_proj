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

from locators import BasePageLocator as BPL


class BasePage:
    """
    Базовый класс для работы с веб-страницами.

    Этот класс предоставляет общие методы для взаимодействия с элементами страницы,
    такие как открытие страницы, переход на страницу логина, поиск, изменение языка и другие.

    Атрибуты:
        driver (WebDriver): Экземпляр веб-драйвера для взаимодействия с браузером.
        url (str): URL-адрес страницы, с которой будет работать класс.
    """

    def __init__(self, driver: WebDriver, url: str):
        """
        Инициализирует экземпляр BasePage.

        Аргументы:
            driver (WebDriver): Экземпляр веб-драйвера (например, Chrome, Firefox).
            url (str): URL-адрес страницы, которую нужно открыть.
        """
        self.driver = driver
        self.url = url

    def open(self):
        """
        Открывает страницу по указанному URL-адресу.

        Использует метод `get` веб-драйвера для перехода на страницу.
        """
        self.driver.get(self.url)

    def go_to_login(self):
        """
        Переходит на страницу логина.

        Нажимает на кнопку логина, используя локатор из BPL.LOGIN_BOTTON.
        """
        self.driver.find_element(*BPL.LOGIN_BOTTON).click()

    def input_search(self, text):
        """
        Выполняет поиск по введенному тексту.

        Аргументы:
            text (str): Текст для поиска.

        Шаги:
            1. Вводит текст в поисковую строку, используя локатор BPL.SEARCH_LINE.
            2. Нажимает кнопку поиска, используя локатор BPL.SEARCH_BUTTON.
        """
        self.driver.find_element(*BPL.SEARCH_LINE).send_keys(text)
        self.driver.find_element(*BPL.SEARCH_BUTTON).click()

    def click_Ockar(self):
        """
        Нажимает на кнопку "Ockar".

        Использует локатор BPL.OSCAR_BUTTON для нажатия на кнопку.
        """
        self.driver.find_element(*BPL.OSCAR_BUTTON).click()

    def change_language(self, language):
        """
        Изменяет язык интерфейса на указанный.

        Аргументы:
            language (str): Значение языка, на который нужно изменить (например, "en" для английского).

        Шаги:
            1. Находит элемент выбора языка, используя локатор BPL.LANGUAGE_BUTTON.
            2. Выбирает язык из выпадающего списка с помощью `Select`.
            3. Нажимает кнопку подтверждения изменения языка, используя локатор BPL.GO_LANGUAGE.
        """
        select = self.driver.find_element(*BPL.LANGUAGE_BUTTON)
        select = Select(select)
        select.select_by_value(language)
        self.driver.find_element(*BPL.GO_LANGUAGE).click()

    def go_in_basket(self):
        """
        Переходит в корзину.

        Нажимает на кнопку корзины, используя локатор BPL.BASKET_BUTTON.
        """
        self.driver.find_element(*BPL.BASKET_BUTTON).click()

    

    

        
        

        