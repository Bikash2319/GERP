from Setup import *
from imap_tools import MailBox, AND

driver, wait = setup_driver()

driver.get("https://app.release.gensomerp.com/login")

# forget_passoword_link = wait.until(ec.element_to_be_clickable((By.XPATH, "//label/span[text()='Click Here ']")))
# forget_passoword_link.click()
wait.until(ec.element_to_be_clickable((By.XPATH, "//label/span[text()='Click Here ']"))).click()

wait.until(ec.url_contains("forgot-password"))

# email_field = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='email']")))
# email_field.send_keys("bikash.sahoo@sharajman.com")
wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='email']")))\
    .send_keys("bikash.sahoo@sharajman.com")

# ph_no_field = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='mobile']")))
# ph_no_field.send_keys("+918249073673")
wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "[formcontrolname='mobile']")))\
    .send_keys("+918249073673")

# generate_button = wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Generate OTP']")))
# generate_button.click()
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='Generate OTP']"))).click()

# Get date, subject and body len of all emails from INBOX folder
with MailBox('mail.google.com').login('bikash.sahoo@sharajaman.com', 'vlvx oqyj rzsr rhhp') as mailbox:
    for msg in mailbox.fetch():
        print(msg.date, msg.subject, len(msg.text or msg.html))







time.sleep(5)