import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders


def SendAnEmail( usr, psw, fromaddr, toaddr,subject, formats, details):
    # SMTP server
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(usr,psw)
    #print(server.login(urs,psw))
    # Send 
    msg=""
    for i in range(len(formats)):
        msg+=(formats[i]+details[i]+"\n\n")

    message = 'Subject: {}\n\n{}'.format(subject, msg)
    server.sendmail(fromaddr, toaddr, message)
    server.quit()

if __name__ == '__main__':
    # Fill info...
    usr='mars.secure.transport.bot@gmail.com'
    psw='Mars@123'
    fromaddr= usr
    toaddr='srinivasthedeveloper@gmail.com'
    SendAnEmail( usr, psw, fromaddr, toaddr)
