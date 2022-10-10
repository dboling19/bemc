import email
import imaplib
import sys
from dotenv import load_dotenv
import os


class Receive():
    def __init__(self):
        load_dotenv()
        self.auth()


    def auth(self):
        # setup authentication
        # in a function to allow later account changes
        self.EMAIL = os.environ.get('EMAIL')
        self.PASSWORD = os.environ.get('PASSWORD')
        self.SERVER = os.environ.get('SERVER')

        self.mail = imaplib.IMAP4_SSL(self.SERVER)
        self.mail.login(self.EMAIL, self.PASSWORD)

    
    def fetch_mail(self):
        self.mail.select('inbox')
        # set mail folder of logged in account

        status, data = self.mail.search(None, 'ALL')
        mail_ids = []

        for block in data:
            mail_ids += block.split()

        return mail_ids
