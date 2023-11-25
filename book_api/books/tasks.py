from time import sleep
from django.core.mail import send_mail
from celery import shared_task
import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 

sender_email = os.getenv('SENDER_MAIL', 'Amunet.manager@gmail.com')
sender_password = os.getenv('SENDER_PASSWORD', 'zppz czjb qvok irrn')

@shared_task
def send_hello_massage(recipient_mail):
    ticket_body = 'Hello'
    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)
        msg = MIMEMultipart()


        msg["From"] = sender_email
        msg["To"] = recipient_mail
        msg["Subject"] = f'Welcome to ...'


        text = ticket_body
        msg.attach(MIMEText(text, "plain"))
    
    
        smtp_server.sendmail(sender_email, recipient_mail, msg.as_string())
    

        smtp_server.quit()
        
    except Exception as e:
        print(e)
