from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message['from'] = "Saiduzzaman Tuhin"
message['to'] = "artisan.python@gmail.com"
message['subject'] = "This is a test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('artisan.python@gmail.com', 'ash1201033m')
    smtp.send_message(message)
    print('SENT...')
