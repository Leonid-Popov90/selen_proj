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

class LoginPageLocator:
    lINE_EMAIL_REG = (By.NAME, "registration-email") #
    LINE_PASSWORD1 = (By.NAME, "registration-password1") #
    LINE_PASSWORD2 = (By.NAME, "registration-password2") #
    BUTTON_REG = (By.NAME, "registration_submit") #
    lINE_EMAIL_LOG = (By.NAME, 'login-username') 
    LINE_PASSWORD_LOGIN = (By.NAME, 'login-password') #
    BUTTON_LOG = (By.NAME, 'login_submit') #
    BUTTON_FORGOT_PASSWORD = (By.XPATH, '//*[@id="login_form"]/p/a') #

class MainPageLocator:
    REGISTER_END = (By.CLASS_NAME, "alertinner")
