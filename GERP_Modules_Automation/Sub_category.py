from Setup import *
from Locators import *
from selenium.webdriver.support import expected_conditions as ec

def add_new_subCategory(wait, make_name, category_name, sub_category_name, model_name):
    wait.until(ec.element_to_be_clickable(add_sub_category)).click()
    category_dd = Select(wait.until(ec.element_to_be_clickable(subCat_category_dd)))
    category_dd
    wait.until(ec.element_to_be_clickable(model_input)).send_keys(model_name)
    wait.until(ec.element_to_be_clickable(save_button)).click()
    wait.until(ec.element_to_be_clickable(toaster)).click()
    time.sleep(1)