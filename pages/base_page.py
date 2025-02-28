
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

class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url
    
    def open(self):
        self.driver.get(self.url)

    def go_to_login(self):
        self.driver.find_element(By.ID, "login_link").click()

        