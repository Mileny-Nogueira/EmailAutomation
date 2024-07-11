import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Credentials for login
user       = "your email"
password   = "your password"

# Recipient data
recipient = "email_recipient@gmail.com"
subject   = "example"
text      = "example"

message = MIMEMultipart()
message['From']    = user
message['To']      = recipient
message['Subject'] = subject
message.attach(MIMEText(text, 'plain'))

try:
  with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(user, password)
    server.sendmail(user, recipient, message.as_string())
  print("Email sent successfully!")
except Exception as e:
  print(f"Error: {e}")