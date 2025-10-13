import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# =================== CONFIGURATION ===================
EMAIL = "bikashsahoo470@gmail.com"
PASSWORD = "your_password_or_app_password"
SUBJECT_KEYWORD = "Password"   # or "OTP", "Verification Code"
OTP_REGEX = r"\b(\d{4,8})\b"   # Adjust pattern as needed
WAIT_TIME = 5                  # seconds between checks
TIMEOUT = 120                  # total seconds to wait for OTP email
# ======================================================


def get_otp_from_gmail():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # Uncomment below if you want to run it in background
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)

    # Step 1: Go to Gmail login
    driver.get("https://mail.google.com/")
    print("Navigating to Gmail...")

    # Step 2: Login to Gmail
    wait.until(EC.presence_of_element_located((By.ID, "identifierId"))).send_keys(EMAIL)
    driver.find_element(By.ID, "identifierNext").click()

    wait.until(EC.presence_of_element_located((By.NAME, "Passwd"))).send_keys(PASSWORD)
    driver.find_element(By.ID, "passwordNext").click()

    print("Logged in successfully! Waiting for inbox to load...")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.F.cf.zt")))  # Gmail inbox table

    # Step 3: Wait for email arrival
    start_time = time.time()
    otp = None

    while time.time() - start_time < TIMEOUT:
        print("Checking for new OTP email...")
        time.sleep(WAIT_TIME)
        driver.refresh()

        # Step 4: Find the email whose subject contains keyword
        emails = driver.find_elements(By.CSS_SELECTOR, "tr.zA")
        for email in emails:
            subject = email.text
            if SUBJECT_KEYWORD.lower() in subject.lower():
                print(f"Found matching email: {subject}")
                email.click()
                time.sleep(2)

                # Step 5: Extract OTP from the email body
                body_elements = driver.find_elements(By.CSS_SELECTOR, "div.a3s.aiL div, div.a3s.aiL")
                full_text = " ".join([el.text for el in body_elements])
                print("Email body:", full_text)

                match = re.search(OTP_REGEX, full_text)
                if match:
                    otp = match.group(1)
                    print(f"✅ OTP Found: {otp}")
                else:
                    print("❌ OTP not found in the email body.")
                break

        if otp:
            break

    driver.quit()

    if otp:
        return otp
    else:
        print("❌ No OTP email found within timeout.")
        return None


# Example usage:
if __name__ == "__main__":
    otp_value = get_otp_from_gmail()
    if otp_value:
        print("OTP:", otp_value)
    else:
        print("Failed to get OTP.")
