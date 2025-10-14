from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

search_bar = wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
add_make = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Make']")))
cancel_button = wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Cancel']")))
save_button = wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
    