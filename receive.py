import email
import imaplib
import env


class Receive():
    def __init__(self):
        self.auth()


    def auth(self):
        # setup authentication
        # in a function to allow later account changes
        creds = env.Credentials()
        self.EMAIL = creds.EMAIL
        self.PASSWORD = creds.PASSWORD
        self.SERVER = creds.SERVER

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
