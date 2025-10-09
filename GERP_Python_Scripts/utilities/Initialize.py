from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Driver:
    def get_driver(browser, timeout):
        if browser.lower() == "chrome":
            driver = webdriver.Chrome()
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox()
        else:
            raise Exception (f"Unsupported browser: {browser}")
        
        driver.maximize_window()
        driver.implicitly_wait(timeout)
        wait = WebDriverWait(driver, timeout)
        return driver, wait
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        def get_driver(browser, timeout):
            if browser.lower() == "chrome":
                driver = webdriver.Chrome()
            elif browser.lower() == "firefox":
                driver = webdriver.Firefox()
            else:
                raise Exception(f"Unsupported browser!: {browser}")
            
            driver.maximize_window()
            driver.implicitly_wait(timeout)
            wait = WebDriverWait(driver, timeout)
            return driver, wait