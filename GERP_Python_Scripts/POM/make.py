from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from locators.make_locators import Make_Webelements


def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(self.driver, 20)


class make_page:
    def add_new_make(driver):
        print(Make_Webelements.add_make.click())