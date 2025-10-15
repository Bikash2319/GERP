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

    # if 'login_required' in scenario.tags:
    #     context.driver.get("https://refex.dev.gensomerp.com/login")
    #     context.driver.find_element(By.XPATH, "//input[@formcontrolname='email']")\
    #         .send_keys("bikash.sahoo@sharajman.com")
    #     context.driver.find_element(By.XPATH, "//input[@formcontrolname='password']")\
    #         .send_keys("Admin@1234")
    #     context.driver.find_element(By.XPATH, "//button[text()='Login ']").click()
    #     context.wait.until(ec.url_contains('dash'))
    #     print("Login successfull.")
    #     time.sleep(2)


def after_scenario(context, scenario):
    profile = context.wait.until(ec.element_to_be_clickable((By.XPATH, "(//img[@class='rounded-circle'])[1]")))
    time.sleep(0.5)
    context.actions.move_to_element(profile).click().perform()
    logout = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//header//app-vertical-navigation//a[text() =' Logout']")))
    time.sleep(0.5)
    context.actions.move_to_element(logout).click().perform()
    context.driver.quit()
    


