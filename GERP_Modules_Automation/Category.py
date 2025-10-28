from Setup import *
from Locators import *
from selenium.webdriver.support import expected_conditions as ec

def add_new_category(wait, category):
    wait.until(ec.element_to_be_clickable(add_category)).click()
    wait.until(ec.element_to_be_clickable(category_input)).clear()
    wait.until(ec.element_to_be_clickable(category_input)).send_keys(category)
    wait.until(ec.element_to_be_clickable(save_button)).click()
    wait.until(ec.element_to_be_clickable(toaster)).click()
    time.sleep(1)
    
def delete_category(wait, category):
    # wait.until(ec.element_to_be_clickable(search_bar)).clear()
    wait.until(ec.presence_of_element_located(search_bar)).send_keys(category)
    time.sleep(1)
    wait.until(ec.element_to_be_clickable(delete_icon)).click()
    wait.until(ec.element_to_be_clickable(yes_button)).click()
    
    








