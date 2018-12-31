# PythonEmail
This script lets you send emails from a gmail account to another email address.

Before you run the script run the following in the command line: 'python -m smtpd -c DebuggingServer -n localhost:1025'. Add 'sudo' at the beginning if you are on Linux.

Also ensure the "Allow less secure apps" setting is turned ON for your account. 

This script takes in a couple parameters to send an email; senders email,senders email password ,receivers email, and the number of times the email is to be sent. 

The message to be sent should be edited in the code itself as to ensure formatting is preserved. 

This script is a fun experiment and is not meant to promote email spam. 

Please see: https://realpython.com/python-send-email/ and: https://developers.google.com/gmail/api/quickstart/python for more info.
