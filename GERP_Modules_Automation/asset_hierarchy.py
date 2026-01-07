from Setup import *
from Locators import *

driver, wait, actions = setup_driver()
domain = "https://app.release.gensomerp.com"

login(driver, domain)

# wait.until(ec.element_to_be_clickable(toaster)).click()

click_on(driver, wait, side_bar)
click_on(driver, wait, asset_menu)
click_on(driver, wait, asset_heirarchy)

# wait.until(ec.element_to_be_clickable((By.XPATH, "//h4[text()='Asset Details']"))).click()

wait.until(ec.element_to_be_clickable(ah_project_dd)).click()

#enter equipment name
equipment_name = 'DEMO-Demo Project-001'
ah_project_search_item = wait.until(ec.element_to_be_clickable((By.XPATH, f"//p-dropdownitem//li//span[text()='{equipment_name}']")))
ah_project_search_item.click()








time.sleep(5) 
logout_gensom(wait)