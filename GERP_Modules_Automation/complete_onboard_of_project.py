from selenium.webdriver.support import expected_conditions as ec
from Setup import *
from Locators import *
from input import *
from Make import add_new_make
from Category import add_new_category
from Model import add_new_model

driver, wait, actions = setup_driver()
domain = "https://app.release.gensomerp.com"

login(driver, domain)

wait.until(ec.element_to_be_clickable(toaster)).click()

#add new make
actions.move_to_element(wait.until(ec.element_to_be_clickable(side_bar))).perform()
click_on(driver, wait, master_menu)
click_on(driver, wait, make_master)
add_new_make(wait, make_name)
# actions.move_to_element(wait.until(ec.element_to_be_clickable(side_bar))).perform()
# click_on(driver, wait, master_menu)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[fill='url(#pattern0_48_8)']")).perform()
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[class='card-title']")).click()
# click_on(driver, wait, master_menu)

#add new category
actions.move_to_element(wait.until(ec.element_to_be_clickable(side_bar))).perform()
# click_on(driver, wait, master_menu)
click_on(driver, wait, category_master)
add_new_category(wait, category_name)
actions.move_to_element(wait.until(ec.element_to_be_clickable(side_bar))).perform()
click_on(driver, wait, master_menu)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[fill='url(#pattern0_48_8)']")).perform()
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[class='card-title']")).click()



#add new model
actions.move_to_element(wait.until(ec.element_to_be_clickable(side_bar))).perform()
# click_on(driver, wait, master_menu)
click_on(driver, wait, model_master)
add_new_model(wait, make_name, category_name, sub_category_name, model_name)
actions.move_to_element(wait.until(ec.element_to_be_clickable(side_bar))).perform()
click_on(driver, wait, master_menu)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[fill='url(#pattern0_48_8)']")).perform()
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[class='card-title']")).click()



logout_gensom(wait)