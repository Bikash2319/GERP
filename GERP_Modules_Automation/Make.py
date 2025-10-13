from selenium import webdriver
from selenium.webdriver.common.by import By
from Setup import *

driver, wait = setup_driver()

domain = "https://app.release.gensomerp.com"

login(driver, domain)

time.sleep(3)







