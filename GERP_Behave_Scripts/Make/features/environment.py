import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service(r"C:\Program Files\Python\Scripts\chromedriver.exe")
chrome_options = Options()

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 20)
    context.actions = ActionChains(context.driver)

    if 'login_required' in scenario.tags:
        context.driver.get("https://app.release.gensomerp.com/login")
        context.driver.find_element(By.XPATH, "//input[@placeholder='name@example.com']")\
            .send_keys("bikash.sahoo@sharajman.com")
        context.driver.find_element(By.XPATH, "//input[@formcontrolname='password']")\
            .send_keys("Admin1234")
        context.driver.find_element(By.XPATH, "//button[text()='Login ']").click()
        context.wait.until(ec.url_contains('solar'))
        print("Login successfull.")
        time.sleep(1)


def after_scenario(context, scenario):
    time.sleep(1)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='navbarSupportedContent']/div/app-vertical-navigation/ul[2]/li[6]/a/div"))).click()
    time.sleep(1)
    context.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "[ptooltip='Logout']"))).click()
    


