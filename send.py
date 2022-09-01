import smtplib
from email.mime.text import MIMEText
import client_dep as Client


class Send():
    def __init__(self):
        print('')

    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    # use username or email to log in
    username = 'dbdanielbboling70@gmail.com'
    password = 'ijdwpwguacflurbb'

    #from_addr = 'dbdanielbboling70@gmail.com'
    #to_addrs = ['dbolingconsulting@gmail.com']

    # the email lib has a lot of templates
    # for different message formats,
    # on our case we will use MIMEText
    # to send only text
    #message = MIMEText('Hello World')
    #message['subject'] = 'Hello'
    #message['from'] = from_addr
    #message['to'] = ', '.join(to_addrs)

    # we'll connect using SSL
    #server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # to interact with the server, first we log in
    # and then we send the message
    #server.login(username, password)
    #server.sendmail(from_addr, to_addrs, message.as_string())
    #server.quit()
