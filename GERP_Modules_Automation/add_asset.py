from Setup import *
from Locators import *


driver, wait, actions = setup_driver()

domain = "https://app.release.gensomerp.com"

login(driver, domain)

driver.get(f"{domain}/new-assets")

asset_name = ""

wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='asset_name']"))).send_keys(asset_name)

wait.unti(ec.element_to_be_clickable((By.XPATH, "//p-select[@formcontrolname='asset_category_id']"))).click()

if "inv" in asset_name:
    wait.until(ec.element_to_be_selected\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='Inverters']"))).click()

elif "smb" in asset_name:
    wait.until(ec.element_to_be_selected\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='String Monitoring Box']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-select[@formcontrolname='asset_type_id']"))).click()
    wait.until(ec.element_to_be_selected\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='SCB']"))).click()
    
    

elif "wms" in asset_name:
    wait.until(ec.element_to_be_selected\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='Weather Monitoring System']"))).click()

else:
    print(f"No {asset_name} found.")