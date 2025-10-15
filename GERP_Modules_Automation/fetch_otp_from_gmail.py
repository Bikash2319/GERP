# from dotenv import load_dotenv
import re
from imap_tools import MailBox, AND
import os
# # Load .env file
# load_dotenv()
# # Read variables
# email_user = os.getenv('EMAIL_USER')
# email_pass = os.getenv('EMAIL_PASS')

# email_user = "bikashsahoo82490@gmail.com"
# email_pass = "cxrk hmyo hwmk cbfg"
email_user = "bikash.sahoo@sharajman.com"
email_pass = "ntzt ivoh nrbl bdyi"

with MailBox("imap.gmail.com").login(email_user, email_pass, "GenSOM ERP Event Reminder") as mailbox:
    # print(mailbox.folder.list())
    
    for mail in mailbox.fetch(reverse=True, mark_seen=False, limit=5):
        print(mail.subject, mail.date,)
        print(mail.text)



























# def check_latest_email():
#     # Connect to Gmail's IMAP server
#     with MailBox('imap.gmail.com').login(email_user, email_pass, 'Inbox') as mailbox:
#         # Fetch the latest unread email
#         emails = list(mailbox.fetch(AND(seen=False), limit=1, reverse=True))
#         if len(emails) == 0:
#             return None, None, None  # No Emails Found
#         return emails[0]
# if __name__ == "__main__":
#     email = check_latest_email()
#     if email:
#         print("Email subject: ", email.subject)
#         print("Email text: ", email.text)
#         print("Email from: ", email.from_)
#     else:
#         print("No new emails found.")
        

# def extract_otp(email_text):
#     # Regex pattern to match a 6-digit number
#     otp_pattern = re.compile(r'\b\d{6}\b')
#     match = otp_pattern.search(email_text)
#     if match:
#         return match.group()
#     return None
# #Example to extract otp from email
# otp = extract_otp(email.text)
# if otp:
#     print("Extracted OTP: ", otp)
# else:
#     print("No OTP found in the email content.")