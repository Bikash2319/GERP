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


# /html/body/app-root/app-full-layout/div/div[1]/div/app-plant-form-wizard/section/div/div[2]\
#                  /div/app-asset-hierarchy-layout/div/div[2]/div[1]/div/div[2]\
#                             /p-tree/div/div/ul/p-treenode/li/div/span/span/div/div[2]/button/span
                                             
                             

# /html/body/app-root/app-full-layout/div/div[1]/div/app-plant-form-wizard/section/div/div[2]\
#                 /div/app-asset-hierarchy-layout/div/div[2]/div[1]/div/div[2]\
#                             /p-tree/div/div/ul/p-treenode/li/ul/p-treenode/li/div/span[2]/span/div/div[2]/button[1]/span
                            

# /html/body/app-root/app-full-layout/div/div[1]/div/app-plant-form-wizard/section/div/div[2]\
#                  /div/app-asset-hierarchy-layout/div/div[2]/div[1]/div/div[2]\
#                             /p-tree/div/div/ul/p-treenode/li/ul/p-treenode/li/ul/p-treenode/li/div/span[2]/span/div         

driver, wait, actions = setup_driver()
login(driver, base_url)

driver.get("https://app.release.gensomerp.com/new-assets")

asset= "new SMB one"
asset_name = asset.lower()

wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='asset_name']"))).send_keys(asset)

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


time.sleep(10)
