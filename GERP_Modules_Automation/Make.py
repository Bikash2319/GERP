from Setup import *
from Locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# driver, wait = setup_driver()
# domain = "https://app.release.gensomerp.com"

# login(driver, domain

# wait.until(ec.presence_of_element_located(side_bar)).click()
# wait.until(ec.presence_of_element_located(master_menu)).click()
# wait.until(ec.presence_of_element_located(make_master)).click()

# wait.until(ec.element_to_be_clickable(add_make)).click()
# wait.until(ec.element_to_be_clickable(make_input)).clear()
# wait.until(ec.element_to_be_clickable(make_input)).send_keys("Test Make")
# wait.until(ec.element_to_be_clickable(save_button)).click()

# time.sleep(5)
# logout_gensom(wait)


def add_new_make(driver, wait, make):
    wait.until(ec.element_to_be_clickable(add_make)).click()
    wait.until(ec.element_to_be_clickable(make_input)).clear()
    wait.until(ec.element_to_be_clickable(make_input)).send_keys(make)
    wait.until(ec.element_to_be_clickable(save_button)).click()
    
def delete_make(driver, wait, make):
    # wait.until(ec.element_to_be_clickable(search_bar)).clear()
    print("1111111111111111111111")
    wait.until(ec.presence_of_element_located(search_bar)).send_keys(make)
    print("22222222222222222222")
    time.sleep(1)
    print("333333333333333333333333")
    wait.until(ec.element_to_be_clickable(delete_icon)).click()
    wait.until(ec.element_to_be_clickable(yes_button)).click()
    
    







# time.sleep(3)







