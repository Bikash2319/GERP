import requests
import os


base_url ="https://app.release.gensomerp.com/api"
make_input = "makeapi"
category_input = "categoryapi"
sub_category_input = "subcategoryapi"
model_input = "modelapi"





login_payload = {
    "email":"bikash.sahoo@sharajman.com",
    "password":"Gensom@1234"
    }

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjoyNiwidXNlcl9pZCI6MzEsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzY1MjQyMDM1fQ.dN_5z3Qb6jt634D8ery1Oz0amRAaq3Pq93geWhhZLZg"
header = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

#create make
create_make_url = f"{base_url}/create_make"
create_make_payload = {"make_name": make_input}
response = requests.post(create_make_url, json= create_make_payload, headers= header)
print(response.status_code)
print(response.json())
make_id = response.json().get("make_id")


#update make
update_make_url = f"{base_url}/update_make"
update_make_payload = {
    "make_id":make_id,
    "make_name":f"{make_input} updated"}
response = requests.post(update_make_url, json=update_make_payload, headers= header)
print(response.status_code)
print(response.json())


#create category
create_category_url =f"{base_url}/create_category"
create_category_payload = {"category": category_input}
response = requests.post(create_category_url, json=create_category_payload, headers= header)
print(response.status_code)
print(response.json())
category_id = response.json().get("data", {}).get("classification_id")
print(category_id)


#update category
update_category_url = f"{base_url}/get_specific_category_data"
update_category_payload = {"category_id": category_id,
                           "category":f"{category_input} updated"}
response = requests.post(update_category_url, json= update_category_payload, headers= header)
print(response.status_code)
print(response.json())


#create sub category
create_sub_category_url = f"{base_url}/create_sub_category"
create_sub_category_payload = {
    "sub_category": sub_category_input,
    "parent_id": category_id,
    "reorder_level":"false",
    "serial_no":"false",
    "require_tilt_angle":"false",
    "require_mounting_type":"false"
    }
response = requests.post(create_sub_category_url, json=create_sub_category_payload, headers=header)
print(response.status_code)
print(response.json())
sub_category_id = response.json().get("data")
print(sub_category_id)


#update sub category
update_sub_category_url = f"{base_url}/update_sub_category"
update_sub_category_payload = {
    "category_id":sub_category_id,
    "sub_category":f"{sub_category_input} updated",
    "parent_id":category_id,
    "sub_category_code":"IT029",
    "reorder_level":"false",
    "serial_no":"false",
    "require_tilt_angle":"false",
    "require_mounting_type":"false"}
response = requests.post(update_sub_category_url, json=update_sub_category_payload, headers= header)
print(response.status_code)
print(response.json())

#create model
create_model_url = f"{base_url}/create_model"
create_model_payload = {"category_id":category_id,
                        "sub_category_id":sub_category_id,
                        "make_id":make_id,
                        "model_name":model_input}
response = requests.post(create_model_url, json=create_model_payload, headers=header)
print(response.status_code)
print(response.json())
model_id = response.json().get("model_id")


#update model
update_model_url = f"{base_url}/update_model"
update_model_payload = {
    "model_id":model_id,
    "category_id":category_id,
    "sub_category_id":sub_category_id,
    "make_id":make_id,
    "model_name":f"{model_input} updated"}
response = requests.post(update_model_url, json=update_model_payload, headers= header)
print(response.status_code)
print(response.json())


#delete model
delete_model_url = f"{base_url}/delete_model"
delete_model_payload = {"model_id":model_id}
response = requests.post(delete_model_url, json=delete_model_payload, headers= header)
print(response.status_code)
print(response.json())


#delete sub category
delete_sub_category_url = f"{base_url}/remove_sub_category"
delete_sub_category_payload = {"category_id":sub_category_id,
                               "parent_id":category_id}
response = requests.post(delete_sub_category_url, json=delete_sub_category_payload, headers=header)
print(response.status_code)
print(response.json())


#delete category
delete_category_url = f"{base_url}/remove_category"
delete_category_payload = {"category_id":category_id}
response = requests.post(delete_category_url, json=delete_category_payload, headers=header)
print(response.status_code)
print(response.json())


# delete make
delete_make_url = f"{base_url}/delete_make"
delete_make_payload = {"make_id": make_id}
response = requests.post(delete_make_url, json=delete_make_payload, headers=header )
print(response.status_code)
print(response.json())