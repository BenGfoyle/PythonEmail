#this script will send a prewritten email to a given address a given number of times.
#this script is not intended nor meant to encourage spam
#NOTE: Before you run, enter the line below into the command line
#python -m smtpd -c DebuggingServer -n localhost:1025
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import random


port = 465  # For SSL
emailAddr = YOUR_GMAIL
password = YOUR_PASSWORD
recAddr = []
rec = random.choice(recAddr)
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'EP Fourth Year Class'
msgRoot['From'] = emailAddr

msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('<img src="cid:image1">', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('rick.gif', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(emailAddr, password)
    server.sendmail(msgRoot['From'], rec, msgRoot.as_string())
