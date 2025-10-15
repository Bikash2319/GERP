from selenium import webdriver
from selenium.webdriver.common.by import By
from Setup import *
from Locators import *

driver, wait = setup_driver()
domain = "https://app.release.gensomerp.com"

wait.until(ec.presence_of_element_located(side_bar)).click()
wait.until(ec.presence_of_element_located(master_menu)).click()
wait.until(ec.presence_of_element_located(make_master)).click()



def add_new_make( wait, make):
    wait.until(ec.element_to_be_clickable(add_make)).send_keys(make)
    wait.until(ec.element_to_be_clickable(save_button)).click()

time.sleep(5)
logout_gensom(wait)






# time.sleep(3)







