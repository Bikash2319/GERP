import requests
import json
from Setup import *
from Locators import *

token = ""
base_url = "https://app.release.gensomerp.com"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

driver, wait, actions = setup_driver()
login(driver, base_url)

file_path = "C:\Automation\GERP\project_details.xlsx"
df = pd.read_excel(file_path, "demo")
data_list = df.to_dict(orient="records")


for i in range(1, 2):
    for item in data_list:
        project_name = item.get("project_name")
        # print(f"DEMO-{project_name}-{i:03d}")
        display_order = i + 100
        plant_payload = {
            "plant_code": f"demo-{project_name}-{i:03d}", #need to fetch from excel sheet
            "plant_name": f"DEMO-{project_name}-{i:03d}", #need to fetch from excel sheet
            "short_name": f"{project_name}{i:03d}", #need to fetch from excel sheet
            "site_address": "Testing address", #need to fetch from the excel sheet
            "state_id": "3", #need to fetch from the excel sheet
            "latitude": 52.96, #need to fetch from the excel sheet
            "longitude": 52.36, #need to fetch from the excel sheet
            "cluster_id": "3",
            "company_id": "21",
            "domain": "SOLAR_MANAGEMENT",
            "sub_domain": "SOLAR_POWER_STORAGE",
            "technology_type": "MONOCRYSTALLINE",
            "installation_type": "GROUND MOUNT",
            "mounting_type": "FIXED TILT",
            "tilt": 30.5,
            "dc_capacity": 1000, #need to fetch from the excel sheet
            "ac_capacity": 1500, #need to fetch from the excel sheet
            "commisioning_date": "2025-11-12",
            "warehouse_id": "97",
            "tariff": 100,
            "data_frequency": "5", #need to fetch from excel sheet
            "is_wms_installed": True,
            "is_smb_installed": True,
            "start_time": "07:00",
            "end_time": "19:30",
            "display_order": display_order #need to fetch from the excel sheet
        }
        create_plant_url = f"{base_url}/api/add_basic_plant_details"
        
        time.sleep(2)
        try:
            response = requests.post(create_plant_url, headers=headers, data=json.dumps(plant_payload))
            print("Status Code:", response.status_code)
            
            if response.status_code == 201:
                response_data = response.json()
                project_id = response_data.get("data", {}).get("plant_id")
                
                if not project_id:
                    print("Unable to fetch the project id from the response.")
                else:
                    print(f"Project ID: {project_id}")
                    
                    try:
                        site_user_url = f"{base_url}/api/link_user_to_project/{project_id}"
                        site_person_payload = {
                            "user_id": 31,
                            "role_type": "SITE_TECH"
                        }
                        link_response = requests.post(site_user_url, headers=headers, data=json.dumps(site_person_payload))

                        if link_response.status_code == 201:
                            print(f"User linked successfully to project ID {project_id}")
                        else:
                            print("User linking failed.")
                    except requests.exceptions.RequestException as e:
                        print(f"Error while linking user to project: {e}")
                        
            else:
                print(f"Project creation failed: {response.text}")
                
        except requests.exceptions.Timeout:
            print("Request timed out")

    actions.move_to_element(wait.until(ec.element_to_be_clickable(side_bar))).perform()
    click_on(driver, wait, asset_menu)
    
    #Add asset module----------------------------------------------------------------------
    
    driver.get("https://app.release.gensomerp.com/new-assets")

    asset= "new SMB one"
    asset_name = asset.lower()

    wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//input[@formcontrolname='asset_name']"))).send_keys(asset)
    time.sleep(2)
    category_dd = wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-select[@formcontrolname='asset_category_id']")))
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
        print(f"No category similar to {asset_name} found.")

    


    

