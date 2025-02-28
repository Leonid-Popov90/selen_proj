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
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url
    
    def open(self):
        self.driver.get(self.url)

    def go_to_login(self):
        self.driver.find_element(*BPL.LOGIN_BOTTON).click()

    def input_search(self, text):
        self.driver.find_element(*BPL.SEARCH_LINE).send_keys(text)
        self.driver.find_element(*BPL.SEARCH_BUTTON).click()

    def click_Ockar(self):
        self.driver.find_element(*BPL.OSCAR_BUTTON).click()

    def change_language(self, language):
        select = self.driver.find_element(*BPL.LANGUAGE_BUTTON)
        select = Select(select)
        select.select_by_value(language)

        self.driver.find_element(*BPL.GO_LANGUAGE).click()

    def go_in_basket(self):
        self.driver.find_element(*BPL.BASKET_BUTTON).click()

    

        
        

        