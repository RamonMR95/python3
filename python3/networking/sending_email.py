import smtplib
from email.mime.text import MIMEText

body = "This is a sample email"

msg = MIMEText(body)
msg['From'] = "testgemailpy@gmail.com"
msg['To'] = "testgemailpy@gmail.com"
msg['Subject'] = "Bored"
pwd = input("Enter the password: ")
server = smtplib.SMTP('smtp.gmail.com', 587)

try:
    server.starttls()
    server.login("testgemailpy@gmail.com", pwd)
    server.send_message(msg)
    print("Email sent")
except Exception as e:
    print(e)
finally:
    server.quit()


