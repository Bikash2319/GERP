from selenium.webdriver.common.by import By

#universal locators
search_bar = (By.XPATH, "//input[@placeholder='Search']")
cancel_button = (By.XPATH, "//button[text()='Cancel']")
save_button = (By.XPATH, "//button[text()='Save']")
update_button = (By.XPATH, "//button[text()='Update']")
view_icon = (By.XPATH, "//a[@ngbtooltip='View']")
edit_icon = (By.XPATH, "//a[@ngbtooltip='Edit']")
delete_icon = (By.XPATH, "//a[@ngbtooltip='Delete']")
yes_button = (By.XPATH, "//button[text()='Yes']")
toaster = (By.ID, "toast-container")

#sidebar locator
side_bar = (By.XPATH, "//aside[@class='left-sidebar']")

#locators of sidebar menu
dashboard_menu = (By.XPATH, "//aside//span[text()= 'Dashboard ']")
management_menu = (By.XPATH, "//aside//span[text()= 'Management ']")
master_menu = (By.XPATH, "//aside//span[text()= 'Master ']")
ticket_menu = (By.XPATH, "//aside//span[text()= 'Ticket ']")
master_menu = (By.XPATH, "//aside//span[text()= 'Master ']")
maintenance_menu = (By.XPATH, "//aside//span[text()= 'Maintenance ']")
asset_menu = (By.XPATH, "//aside//span[text()= 'Asset ']")
overview_dashboard = (By.XPATH, "//aside//span[text()= 'Overview Dashboard  ']")

#management menu
user_management = (By.XPATH, "//aside//span[text()= 'User Management']")
project_management = (By.XPATH, "//aside//span[text()= 'Project Management']")
vendor_management = (By.XPATH, "//aside//span[text()= 'Vendor Management']")
team_management = (By.XPATH, "//aside//span[text()= 'Team Management']")
invenvtory_management = (By.XPATH, "//aside//span[text()= 'Inventory Management']")

#master menu
make_master = (By.XPATH, "//aside//span[text()= 'Make']")
warehouse_master = (By.XPATH, "//aside//span[text()= 'Warehouse']")
activity_master = (By.XPATH, "//aside//span[text()= 'Activity']")
incident_master = (By.XPATH, "//aside//span[text()= 'Incident']")
element_master = (By.XPATH, "//aside//span[text()= 'Element']")
company_master = (By.XPATH, "//aside//span[text()= 'Company']")
category_master = (By.XPATH, "//aside//span[text()= 'Category']")
cluster_master = (By.XPATH, "//aside//span[text()= 'Cluster']")
sub_category_master = (By.XPATH, "//aside//span[text()= 'Sub Category']")
item_master = (By.XPATH, "//aside//span[text()= 'Items']")
model_master = (By.XPATH, "//aside//span[text()= 'Model']")
alarm_master = (By.XPATH, "//aside//span[text()= 'Alarm']")
inventory_master = (By.XPATH, "//aside//span[text()= 'Inventory']")

#Ticket module sub-menu
notification_dashboard  = (By.XPATH, "//aside//span[text()= 'Notification Dashboard']")
ticket_dashboard = (By.XPATH, "//aside//span[text()= 'Ticket Dashboard']")
technician_dashboard = (By.XPATH, "//aside//span[text()= 'Technician Dashboard']")
alert_list = (By.XPATH, "//aside//span[text()= 'Alert List']")

#dashboard sub-menus
inventory_dashboard = (By.XPATH, "//aside//span[text()= 'Inverter Dashboard']")
ws_dashboard = (By.XPATH, "//aside//span[text()= 'WS Dashboard']")
mfm_dashboard = (By.XPATH, "//aside//span[text()= 'MFM Dashboard']")
smb_dashboard = (By.XPATH, "//aside//span[text()= 'SMB Dashboard']")
trend_dashboard = (By.XPATH, "//aside//span[text()= 'Trend Dashboard']")
cmms_dashboard = (By.XPATH, "//aside//span[text()= 'CMMS Dashboard']")
inverter_list_view = (By.XPATH, "//aside//span[text()= 'Inverter List View']")
inverter_performance = (By.XPATH, "//aside//span[text()= 'Inverter Performance']")
inverter_dashboard = (By.XPATH, "//aside//span[text()= 'Inverter Dashboard']")
smb_details_dashboard = (By.XPATH, "//aside//span[text()= 'SMB Details Dashboard']")
manage_band = (By.XPATH, "//aside//span[text()= 'Manage Band']")
upload_dsm_schedule = (By.XPATH, "//aside//span[text()= 'Upload Dsm Schedule']")
string_dashboard = (By.XPATH, "//aside//span[text()= 'String Dashboard']")

#maintenance sub-menu
scheduler = (By.XPATH, "//aside//span[text()= 'Scheduler']")
task_viewer = (By.XPATH, "//aside//span[text()= 'Task Viewer']")
maintenance_new = (By.XPATH, "//aside//span[text()= 'Maintenance New']")

#Make module
add_make = (By.XPATH, "//div[@ngbtooltip='Add Make']")
make_input = (By.XPATH, "//input[@formcontrolname='make_name']")




    