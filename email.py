#this script will send a prewritten email to a given address a given number of times.
#this script is not intended nor meant to encourage spam
"""<---------------------------------------------------------------------------------------------------------------------->"""
#NOTE: Before you run, enter the line below into the command line
#python -m smtpd -c DebuggingServer -n localhost:1025
import smtplib, ssl

port = 465  # For SSL

email = input("Type your gmail address and press enter: ") #user input if prefered
password = input("Type your password and press enter: ")
receiver_email = input("Enter receiver email address and press enter: ")
send = int(input("How many times do you want to send it:"))
#what is being sent, Subject: xxx, will appear as subject line of email
message = """\
Subject: Lorem Ipsum 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Regards,
John Smith
"""

"""<---------------------------------------------------------------------------------------------------------------------->"""

# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(email, password)
    for i in range(0,send):
        server.sendmail(email, receiver_email, message)