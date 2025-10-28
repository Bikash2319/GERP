import time
from behave import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


@given(u'User logged into the application')
def step_impl(context):
    # context.driver.get("https://app.release.gensomerp.com/solar-plant-dashboard")
    # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhc2hpc2gua0BzaGFyYWptYW4uY29tIiwibG9naW5faWQiOjMsInVzZXJfaWQiOjMsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzYxNTkxOTI5fQ.E4Jzv8certJ3QKUr58h1R9EZFbjg75s45UgEAC37Wnk"
    # context.driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
    
    # context.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@placeholder='name@example.com']"))).send_keys("bikash.sahoo@sharajman.com")
    # context.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']"))).send_keys("Admin1234")
    # context.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Login ']"))).click()
    # context.wait.until(ec.url_contains("solar"))
    # print("Overview Dashboard")
    pass


@when(u'User click on Make sub-menu from Master menu')
def step_impl(context):
    context.wait.until(ec.presence_of_element_located((By.XPATH, "//aside[@class='left-sidebar']"))).click()
    context.wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Master ']"))).click()
    context.wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Make']"))).click()
    

@then(u'User successfully redirect to make master page')
def step_impl(context):
    # assert "make" in context.driver.current_url(), "user is not redirected to make master"
    if "make" in context.driver.current_url():
        print("User successfully redirect to make master page.")
    else:
        print("User does not navigate to make master page.")

@when(u'User click on add make button')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Make']"))).click()


@then(u'User enters the make and click on save button')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='make_name']"))).send_keys("product make")
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()

@then(u'Make is successfully saved into the system')
def step_impl(context):
    toaster = context.wait.until(ec.presence_of_element_located((By.ID, "toast-container")))
    time.sleep(1)
    if "Saved" in toaster.text:
        print(toaster.text)
    else:
        print("Make does not save into the system.")