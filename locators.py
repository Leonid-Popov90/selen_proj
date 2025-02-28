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
    LOGIN_BOTTON = (By.ID, "login_link") #
    OSCAR_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[1]/a') #
    LANGUAGE_BUTTON = (By.NAME, 'language') #
    GO_LANGUAGE = (By.XPATH, '/html/body/div[1]/div[2]/div/form/button') #
    SEARCH_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[2]/div/div[2]/form/input') #
    SEARCH_LINE = (By.ID, 'id_q') #
    BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
