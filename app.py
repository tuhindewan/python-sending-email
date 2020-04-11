from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

# Create the root message and fill in from, to, and subject headers
str_from = "Saiduzzaman Tuhin"
str_to = "artisan.python@gmail.com"
message = MIMEMultipart()
message['from'] = str_from
message['to'] = str_to
message['subject'] = "This is a test"
message.attach(MIMEText("Body"))

# add images
fp = open('image.jpg', 'rb')
msgImage = MIMEImage(fp.read(), _subtype='jpg')
fp.close()
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(str_to, 'ash1201033m')
    smtp.send_message(message)
    print('SENT...')
