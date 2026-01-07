from Setup import *
from Locators import *

driver, wait, actions = setup_driver()

base_url = "https://app.release.gensomerp.com"

login(driver, base_url)

click_on(driver, wait, side_bar)
click_on(driver, wait, asset_menu)
click_on(driver, wait, asset_list)
click_on(driver, wait, add_asset_btn)

wait.until(ec.element_to_be_clickable((By.XPATH, "//p-select[@formcontrolname='asset_category_id']"))).click()
time.sleep(1)
if "inv" in asset_name:
    wait.until(ec.element_to_be_selected\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='Inverters']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-select[@formcontrolname='asset_type_id']"))).click()
    wait.until(ec.element_to_be_selected\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='String Inverter']"))).click()
    
    

elif "smb" in asset_name:
    wait.until(ec.element_to_be_selected\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='String Monitoring Box']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-select[@formcontrolname='asset_type_id']"))).click()
    wait.until(ec.element_to_be_selected\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='SCB']"))).click()
    

elif "wms" in asset_name:
    wait.until(ec.element_to_be_selected\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='Weather Monitoring System']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-select[@formcontrolname='asset_type_id']"))).click()
    wait.until(ec.element_to_be_selected\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='Humidity Sensor']"))).click()
    
elif "MFM" or "meter" in asset_name:
    wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='Multi Functional Meter']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-select[@formcontrolname='asset_type_id']"))).click()
    wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='Energy Meter']"))).click()
    
    
else:
    print(f"No {asset_name} found.")



time.sleep(3)
logout_gensom(wait)

