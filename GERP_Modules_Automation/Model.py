from Setup import *
from Locators import *
from selenium.webdriver.support import expected_conditions as ec

def add_new_model(wait, make_name, category_name, sub_category_name, model_name):
    wait.until(ec.element_to_be_clickable(add_model)).click()
    make_dd = Select(wait.until(ec.element_to_be_clickable(model_make_dd)))
    make_dd.select_by_visible_text(make_name)
    category_dd = Select(wait.until(ec.element_to_be_clickable(category_dd)))
    category_dd.select_by_visible_text(category_name)
    sub_cat_dd = Select(wait.until(ec.element_to_be_clickable(model_sub_category_dd)))
    sub_cat_dd.select_by_visible_text(sub_category_name)
    wait.until(ec.element_to_be_clickable(model_input)).send_keys(model_name)
    wait.until(ec.element_to_be_clickable(save_button)).click()
    wait.until(ec.element_to_be_clickable(toaster)).click()
    time.sleep(1)