import urwid
import sys
import send
import email
import html2text
import os
import mailparser
from receive import Receive


class Client():

    def create_email_list(self):
        # does not display list - only generates it
        receive = Receive()
        self.mail = receive.mail
        mail_ids = receive.fetch_mail()
        body = []
        for i in mail_ids:
            status, data = self.mail.fetch(i, '(RFC822)')

            for response_part in data:
                if isinstance(response_part, tuple):    
                ## not sure what the point of this is for as response part in my testing 
                ## only ever has 2 indexes, both are tuples
                ## assume this is for edgecases
                    message = email.message_from_bytes(response_part[1])
                    ## response_part only have 2 indexes - the first is the email info (RFC822)
                    ## the second is the actual email content

                    
            mail_from = message['from']
            mail_subject = message['subject']
            button = urwid.Button(f'{mail_from} | {mail_subject}')
            urwid.connect_signal(button, 'click', self.item_chosen, i)
            body.append(urwid.AttrMap(button, None, focus_map='reversed'))
        return urwid.ListBox(urwid.SimpleFocusListWalker(body))


    def item_chosen(self, button, choice):
        status, data = self.mail.fetch(choice, '(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])


                if message.is_multipart():
                    mail_content = ''

                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()

                else:
                    mail_content = message.get_payload()

                mail_from = message['from']
                mail_subject = message['subject']
                response = urwid.Text([f'{mail_content}'])
                self.main.original_widget = urwid.Filler(urwid.Pile([response]))


    def show_email_list(self):
        self.main = urwid.Padding(self.create_email_list())
        top = urwid.Overlay(self.main, urwid.SolidFill(u'\N{MEDIUM SHADE}'), align='center', width=('relative', 100), valign='middle', height=('relative', 100), min_width=20, min_height=9)
        urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()



client = Client()
client.show_email_list()

