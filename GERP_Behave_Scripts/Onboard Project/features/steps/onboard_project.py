import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from behave import *


@given(u'User should redirect to Make master and enter a make')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[@class='left-sidebar']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Master ']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Make']"))).click()
    time.sleep(0.5)
    # context.wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Make']"))).click()
    # context.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='make_name']"))).send_keys("gerp make")
    # context.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()
    # time.sleep(1)
    # context.wait.until(ec.presence_of_element_located((By.ID, "toast-container"))).click()


@given(u'User should redirect to Category master and enter a category')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[@class='left-sidebar']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Master ']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Category']"))).click()
    time.sleep(0.5)
    


@given(u'User should redirect to Model master and enter a model')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[@class='left-sidebar']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Master ']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Model']"))).click()
    time.sleep(0.5)



@given(u'User should redirect to sub category master and enter a sub-category')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[@class='left-sidebar']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Master ']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Sub Category']"))).click()
    time.sleep(0.5)


@given(u'User should redirect to warehouse master and enter a warehouse')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[@class='left-sidebar']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Master ']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Warehouse']"))).click()
    time.sleep(0.5)


@given(u'User should redirect to inventory master and enter an inventory')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[@class='left-sidebar']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Master ']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Inventory']"))).click()
    time.sleep(0.5)


@given(u'User should redirect to project management and fill out basic details page')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside[@class='left-sidebar']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//aside//span[text()= 'Project Management']"))).click()
    time.sleep(0.5)
    context.wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Project']"))).click()
    time.sleep(0.5)


@given(u'User navigate to site person tab and enter a User')
def step_impl(context):
    pass


@given(u'User navigate to logger tab and enter a logger')
def step_impl(context):
    pass


@given(u'User navigate to the equipment tab and enter equipment name to enter all the equipments')
def step_impl(context):
    pass


@then(u'User navigate to the project management page and make the project live')
def step_impl(context):
    pass

@then(u'Added project successfully displayed on the overview dashboard page')
def step_impl(context):
    pass