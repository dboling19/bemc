import email
import imaplib

class Receive():
    def __init__(self):
        self.auth()


    def auth(self):
        # setup authentication
        # in a function to allow later account changes
        self.EMAIL = 'dbdanielbboling70@gmail.com'
        self.PASSWORD = 'ijdwpwguacflurbb'
        self.SERVER = 'imap.gmail.com'
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
