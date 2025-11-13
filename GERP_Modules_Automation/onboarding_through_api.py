import requests
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjoyNiwidXNlcl9pZCI6MzEsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzYzMDg3NjQxfQ.w5OBc87pyleU_6WiwmdfzjMHTnh75-jtblnbLVMb4DU"
# base_url = "https://app.release.gensomerp.com"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


plant_payload = {
    "plant_code": "Testing ID-002", #need to fetch from excel sheet
    "plant_name": "Testing Project-002", #need to fetch from excel sheet
    "short_name": "002Project", #need to fetch from excel sheet
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
    "display_order": 101 #need to fetch from the excel sheet
}


create_plant_url = "https://app.release.gensomerp.com/api/add_basic_plant_details"

try:
    response = requests.post(create_plant_url, headers=headers, data=json.dumps(plant_payload))
    print("Status Code:", response.status_code)

    if response.status_code == 201:
        response_data = response.json()
        project_id = response_data.get("data", {}).get("plant_id")

        if not project_id:
            print("Could not extract project_id from response.")
        else:
            print(f"Project ID: {project_id}")

            try:
                site_user_url = f"https://app.release.gensomerp.com/api/link_user_to_project/{project_id}"
                site_person_payload = {
                    "user_id": 31,
                    "role_type": "SITE_TECH"
                }

                link_response = requests.post(site_user_url, headers=headers, data=json.dumps(site_person_payload))
                print("\nLink User Status Code:", link_response.status_code)

                if link_response.status_code == 200:
                    print(f"User linked successfully to project ID {project_id}")
                else:
                    print(f"Failed to link user: {link_response.text}")

            except requests.exceptions.RequestException as e:
                print(f"Error while linking user to project: {e}")

    else:
        print(f"Project creation failed: {response.text}")

except requests.exceptions.Timeout:
    print("Request timed out. Please check your network connection.")
except requests.exceptions.ConnectionError:
    print("Network connection error. Please verify internet connectivity.")
except requests.exceptions.RequestException as e:
    print(f"Unexpected error while creating project: {e}")
