from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class universal_locator:
    
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    
    #sidebar locator
    side_bar = wait.until(ec.presence_of_element_located((By.XPATH, "//aside[@class='left-sidebar']")))
    
    #locators of sidebar menu
    dashboard_menu = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Dashboard ']")))
    management_menu = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Management ']")))
    master_menu = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Master ']")))
    ticket_menu = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Ticket ']")))
    master_menu = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Master ']")))
    maintenance_menu = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Maintenance ']")))
    asset_menu = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Asset ']")))
    overview_dashboard = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Overview Dashboard  ']")))
    
    #management menu
    user_management = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'User Management']")))
    project_management = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Project Management']")))
    vendor_management = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Vendor Management']")))
    team_management = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Team Management']")))
    invenvtory_management = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Inventory Management']")))
    
    #master menu
    make_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Make']")))
    warehouse_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Warehouse']")))
    activity_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Activity']")))
    incident_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Incident']")))
    element_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Element']")))
    company_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Company']")))
    category_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Category']")))
    cluster_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Cluster']")))
    sub_category_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Sub Category']")))
    item_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Items']")))
    model_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Model']")))
    alarm_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Alarm']")))
    inventory_master = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Inventory']")))
    
    #Ticket module sub-menu
    notification_dashboard  = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Notification Dashboard']")))
    ticket_dashboard = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Ticket Dashboard']")))
    technician_dashboard = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Technician Dashboard']")))
    alert_list = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Alert List']")))
    
    #dashboard sub-menus
    inventory_dashboard = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Inverter Dashboard']")))
    ws_dashboard = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'WS Dashboard']")))
    mfm_dashboard = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'MFM Dashboard']")))
    smb_dashboard = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'SMB Dashboard']")))
    trend_dashboard = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Trend Dashboard']")))
    cmms_dashboard = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'CMMS Dashboard']")))
    inverter_list_view = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Inverter List View']")))
    inverter_performance = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Inverter Performance']")))
    inverter_dashboard = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Inverter Dashboard']")))
    smb_details_dashboard = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'SMB Details Dashboard']")))
    manage_band = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Manage Band']")))
    upload_dsm_schedule = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Upload Dsm Schedule']")))
    string_dashboard = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'String Dashboard']")))

    #maintenance sub-menu
    scheduler = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Scheduler']")))
    task_viewer = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Task Viewer']")))
    maintenance_new = wait.until(ec.presence_of_element_located((By.XPATH, "//aside//span[text()= 'Maintenance New']")))
    

    