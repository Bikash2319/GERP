from Setup import *
from Locators import *

domain = "https://refex.beta.gensomsolar.com"

# domain = "https://app.release.gensomerp.com"

driver, wait, actions = setup_driver()
login(driver, domain)

# wait.until(ec.element_to_be_clickable(toaster)).click()

click_on(driver, wait, side_bar)
click_on(driver, wait, asset_menu)
click_on(driver, wait, asset_list)


for i in range(5, 90):
    time.sleep(0.5)
    click_on(driver, wait, add_asset_btn)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='asset_name']"))).send_keys("Data Logger")


    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-select[@formcontrolname='asset_category_id']"))).click()
    time.sleep(0.5)
    wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='Communication & Data Equipment']"))).click()


    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-select[@formcontrolname='asset_type_id']"))).click()
    time.sleep(1)
    wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='Data Logger']"))).click()



    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-select[@formcontrolname='status']"))).click()
    time.sleep(0.5)
    wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='Active']"))).click()


    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-select[@formcontrolname='criticality']"))).click()
    time.sleep(0.5)
    wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='High']"))).click()

    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-floatlabel//input[@formcontrolname='serial_number']"))).click()
    time.sleep(0.5)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='serial_number']"))).send_keys(f"Data Logger-000{i}")

    click_on(driver, wait, save_asset_btn)
    time.sleep(1)

    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-tablist//p-tab[text()='Technical']"))).click()

    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-select[@inputid='make_id']"))).click()
    time.sleep(0.5)
    wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='suryalogic']"))).click()

    wait.until(ec.element_to_be_clickable((By.XPATH, "//p-select[@inputid='model_id']"))).click()
    time.sleep(0.5)
    wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-selectitem//li//span[normalize-space(text())='LOGGER']"))).click()

    click_on(driver, wait, save_asset_btn)
    click_on(driver, wait, toaster)
    time.sleep(0.5)
    click_on(driver, wait, cancel_asset_btn)
    


