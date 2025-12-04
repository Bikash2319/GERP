from Setup import *
from Locators import *
import requests
import json

# token = ""
base_url = "https://app.release.gensomerp.com"
# headers = {
#     "Authorization": f"Bearer {token}",
#     "Content-Type": "application/json"
# }
      

driver, wait, actions = setup_driver()
login(driver, base_url)

driver.get("https://app.release.gensomerp.com/new-assets")

asset= "new SMB one"
asset_name = asset.lower()

wait.until(ec.element_to_be_clickable\
    ((By.XPATH, "//input[@formcontrolname='asset_name']"))).send_keys(asset)
time.sleep(2)
# print("111111111111111111111111")
category_dd = wait.until(ec.element_to_be_clickable\
    ((By.XPATH, "//p-select[@formcontrolname='asset_category_id']")))
# print("2222222222222222222222222")
actions.move_to_element(category_dd).click().perform()
time.sleep(3)

if "inv" in asset_name:
    wait.until(ec.element_to_be_selected\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='Inverters']"))).click()

elif "smb" in asset_name:
    smb_opt = wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='String Monitoring Box']")))
    actions.move_to_element(smb_opt).click().perform()
    asset_type_dd = wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-select[@formcontrolname='asset_type_id']")))
    actions.move_to_element(asset_type_dd).click().perform()
    scb_asset = wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='SCB']")))
    actions.move_to_element(scb_asset).click().perform()
    
    

elif "wms" in asset_name:
    wait.until(ec.element_to_be_selected\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='Weather Monitoring System']"))).click()

else:
    print(f"No {asset_name} found.")


time.sleep(10)
