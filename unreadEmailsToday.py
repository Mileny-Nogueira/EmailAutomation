import subprocess
import sys
from datetime import date

try:
    import imap_tools
except ImportError:
    print("Package imap_tools not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "imap_tools"])
    import imap_tools

from imap_tools import MailBox, A

# Credentials for login
user     = "your email"
password = "your password"

def fetch_unread_emails(user, password):
    try:
        with MailBox("imap.gmail.com").login(user, password, 'INBOX') as mailbox:
   
            emails = mailbox.fetch(A(seen=False))
            
            for email in emails:                
                if email.date.date() == date.today():
                    print(f"From: {email.from_}")
                    print(f"Subject: {email.subject}")
                    print(f"Content: \n{email.text}")
                    print("============================================")          
    except Exception as e:
        print(f"Error fetching emails: {e}")

fetch_unread_emails(user, password)