#!/usr/bin/python
import config
import codecs

from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

def LoadContent():
    f = codecs.open('template_email/index.html', 'r', 'utf-8')
    return f.read()


sender = 'example@mail.pl'
receivers = ['example@mail.com']


content = LoadContent()

message = MIMEText(content.encode('utf-8'), 'html')
message['Subject'] = 'Newsletter SMTP e-mail test'
message['From'] = sender



try:
   smtpConn = SMTP(config.SMTP_SERVER)
   smtpConn.login(config.EMAIL_USERNAME, config.EMAIL_PASSWORD)
   try:
       smtpConn.sendmail(sender, receivers, message.as_string())
   finally:
       smtpConn.quit()

   print "Successfully sent email"
except Exception, exc:
   print "mail failed " + str(exc)
