import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd

TOKEN = r"C:\Automation\GERP\GERP_Modules_Automation\token.txt"


def setup_driver():  
    time.sleep(0.5)
    # chrome_options.add_argument("--ignore-certificate-errors")
    # chrome_options.add_argument("--ignore-ssl-errors")
    # chrome_options.add_argument("--allow-insecure-localhost") 
    chrome_option = Options()
    service = Service(executable_path=r"C:\Program Files\Python\Scripts\chromedriver.exe")
    driver = webdriver.Chrome(options=chrome_option, service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10) 
    actions = ActionChains(driver)
    return driver, wait, actions
    
def read_token():
    if os.path.exists(TOKEN):
        with open(TOKEN, "r") as f:
            return f.read().strip()
    else:
        print("No token available.")     
    return None

def save_token(token):
    with open(TOKEN, "w") as f:
        f.write(token)

def login(driver, domain):
    driver.get(f"{domain}/login")
    #login with token
    token = read_token()
    if token:
        driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
        time.sleep(1)
        driver.get(f"{domain}/solar-plant-dashboard")
        try:
            WebDriverWait(driver, 10).until(ec.url_contains("solar"))
            print("Logged in with saved token")
            return
        except:
            print("Token expired or invalid, logging in with credentials...")

    #Login with credentials
    driver.get(f"{domain}/login")
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='email']"))).send_keys("bikash.sahoo@sharajman.com")
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='password']"))).send_keys("Gensom@1234")
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Login ']"))).click()
    WebDriverWait(driver, 10).until(ec.url_contains("solar-plant-dashboard"))
    print("Logged in with credentials")

    #Save new token
    new_token = WebDriverWait(driver, 15).until(
        lambda d: d.execute_script("return window.localStorage.getItem('token');")
    )
    if new_token:
        save_token(new_token)
        print(f"New token saved to token.txt : {new_token}")
        
        
def logout_gensom(wait):
    wait.until(ec.presence_of_element_located((By.XPATH, "//li[@placement='bottom-end']"))).click()
    time.sleep(0.5)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-button[@ptooltip='Logout']"))).click()
    if os.path.exists(TOKEN):
        with open(TOKEN, "w") as f:
            f.truncate(0)
        print("Token cleared successfully after logout.")
    else:
        print("Token not found, nothing to clear.")
        

def click_on(driver , wait, element):
    actions = ActionChains(driver)
    actions.click(wait.until(ec.element_to_be_clickable(element))).send_keys(Keys.ENTER).perform()
    time.sleep(2)
    # actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "[fill='url(#pattern0_48_8)']")).perform()
    
    
