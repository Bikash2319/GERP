from behave import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


@given(u'User should navigate to login page')
def step_impl(context):
    context.driver.get("https://app.release.gensomerp.com/login")
    assert "login" in context.driver.current_url, "Login page unreachable. Please try again!"


@when(u'User enter valid email and Password')
def step_impl(context):
    email_field = context.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='email']")))
    email_field.send_keys("bikash.sahoo@sharajman.com")
    
    password_field = context.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
    password_field.send_keys("Admin1234")
    
    
@when(u'User enter invalid email and invalid Password')
def step_impl(context):
    email_field = context.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='email']")))
    email_field.send_keys("bikash@sharajman.com")
    
    password_field = context.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
    password_field.send_keys("Admin12345625")


@when(u'User click on Login button')
def step_impl(context):
    login_btn = context.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text() = 'Login ']")))
    login_btn.click()
    context.time.sleep(2)


@then(u'User should able to logged into the application and Overview Dashboard page should be displayed')
def step_impl(context):
    assert "solar" in context.driver.current_url, "Dashboard page is displayed."

@then(u'User should not able to logged in and error toaster message should displayed')
def step_impl(context):
    pass