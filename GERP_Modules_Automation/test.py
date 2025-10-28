from Locators import *
from Setup import *


driver, wait = setup_driver()
domain = "https://app.release.gensomerp.com"

login(driver, domain)
actions = ActionChains(driver)

wait.until(ec.presence_of_element_located((By.ID, "toast-container"))).click()

#make
actions.move_to_element(wait.until(ec.element_to_be_clickable(side_bar))).perform()
click_on(driver, wait, master_menu)
click_on(driver, wait, make_master)
time.sleep(1)
print(driver.current_url)
click_on(driver, wait, master_menu)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[fill='url(#pattern0_48_8)']")).perform()
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[class='card-title']")).click()

#model
actions.move_to_element(wait.until(ec.element_to_be_clickable(side_bar))).perform()
click_on(driver, wait, master_menu)
click_on(driver, wait, model_master)
time.sleep(1)
print(driver.current_url)
click_on(driver, wait, master_menu)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[fill='url(#pattern0_48_8)']")).perform()
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[class='card-title']")).click()

#category
actions.move_to_element(wait.until(ec.element_to_be_clickable(side_bar))).perform()
click_on(driver, wait, master_menu)
click_on(driver, wait, category_master)
time.sleep(1)
print(driver.current_url)
click_on(driver, wait, master_menu)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[fill='url(#pattern0_48_8)']")).perform()
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[class='card-title']")).click()


#inventory
actions.move_to_element(wait.until(ec.element_to_be_clickable(side_bar))).perform()
click_on(driver, wait, master_menu)
click_on(driver, wait, inventory_master)
time.sleep(1)
print(driver.current_url)
click_on(driver, wait, master_menu)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[fill='url(#pattern0_48_8)']")).perform()
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[class='card-title']")).click()




logout_gensom(wait)
