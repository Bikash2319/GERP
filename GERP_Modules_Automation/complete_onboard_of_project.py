from selenium.webdriver.support import expected_conditions as ec
from Setup import *
from Locators import *
from Make import add_new_make, delete_make

driver, wait = setup_driver()
domain = "https://ap.release.gensomerp.com"

login(driver, domain)

wait.until(ec.presence_of_element_located(side_bar)).click()
wait.until(ec.presence_of_element_located(master_menu)).click()
time.sleep(2)
wait.until(ec.presence_of_element_located(make_master)).click()
time.sleep(0.5)
make = "new 111111111111111"
add_new_make(driver,wait,make)
time.sleep(1)
delete_make(driver,wait,make)
time.sleep(2)
wait.until(ec.presence_of_element_located(model_master)).click()




time.sleep(5)
logout_gensom(wait)