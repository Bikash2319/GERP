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


"https://refex.beta.gensomsolar.com/api/add_asset_basic"
{"asset_name":"Data Logger","asset_category_id":2,"asset_type_id":17,"status":"Active","criticality":"High","description":"","serial_number":"Data Logger - 0013","part_number":"","cost_center":"","supplier":""}

"https://refex.beta.gensomsolar.com/api/add_asset_technical"
{"manufacturer":17,"model":28,"certification":[],"capacity":null,"voltage":null,"current":null,"power":null,"rated_power":null,"efficiency":null,"operating_tem":"","ip_rating":"","ac_capacity":null,"dc_capacity":null,"asset_id":2038}