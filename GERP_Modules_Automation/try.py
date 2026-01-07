from Setup import *
from Locators import *

# domain = "https://refex.beta.gensomsolar.com/"

domain = "https://app.release.gensomerp.com"

driver, wait, actions = setup_driver()
login(driver, domain)
