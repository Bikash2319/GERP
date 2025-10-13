from selenium import webdriver
from selenium.webdriver.common.by import By
from Setup import *
from Universal_locators import *

driver, wait = setup_driver()

domain = "https://app.release.gensomerp.com"

login(driver, domain)

time.sleep(2)
side_bar.click()
print("Sidebar is clicked.")


time.sleep(3)







