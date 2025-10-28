import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


chrome_option = Options()
service = Service(executable_path=r"C:\Program Files\Python\Scripts\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_option, service=service)
driver.maximize_window()
driver.implicitly_wait(20)
wait = WebDriverWait(driver, 20)

driver.get("https://app.release.gensomerp.com/login")

wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@placeholder='name@example.com']"))).send_keys("bikash.sahoo@sharajman.com")
wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']"))).send_keys("Admin1234")
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Login ']"))).click()
wait.until(ec.url_contains("solar"))
print("Overview Dashboard")

toaster = wait.until(ec.presence_of_element_located((By.ID, "toast-container")))
toaster.click()

wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='navbarSupportedContent']/div/app-vertical-navigation/ul[2]/li[6]/a/div"))).click()
time.sleep(1)
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "[ptooltip='Logout']"))).click()
time.sleep(.5)
if "Successfully" in toaster.text:
    print("Toaster contains successfully.")
    driver.quit()
else:
    print(toaster.text)


time.sleep(5)

    