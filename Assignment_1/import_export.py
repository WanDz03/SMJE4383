import pandas as pd
import smtplib
#import os
import ssl
from email.message import EmailMessage

file_1 = pd.read_csv('/home/wan_dz/github/SMJE4383/Assignment_1/name_height.csv')
print(file_1)

file_1.to_csv("file2.csv")

email_user = 'firdauswan645@gmail.com'
email_password = 'tykyupcfcxpptfko'
email_receiver = 'cannonjohn03@gmail.com'



subject = 'There is notification'
body = """

The csv file was successfully exported

"""
em = EmailMessage()
em['From']= email_user
em['To']= email_receiver
em['Subject']= subject
em.set_content(body)


context= ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context= context) as smtp:
	smtp.login(email_user, email_password)
	smtp.sendmail(email_user, email_receiver ,em.as_string())
