'''
unittest for functions in mail.py
'''
import unittest
import smtplib
import socket
from .context import retrier


class MailTest(unittest.TestCase):
    def test_set_message(self):
        receiver = 'test@test.com'
        sender = receiver
        subject = 'test_subject'
        content = 'test_content'
        msg = retrier.set_message(sender, receiver, subject, content)
        self.assertEqual(msg['To'], receiver)
        self.assertEqual(msg['From'], sender)
        self.assertEqual(msg['Subject'], subject)

    def test_connect_smtp_server(self):
        smtp_server = 'localhost'
        smtp = retrier.connect_smtp_server(smtp_server)
        self.assertIsInstance(smtp, smtplib.SMTP)
        smtp.close()

    def test_connect_unreachable_smtp_server_with_domain_name(self):
        smtp_server = 'unreachable'
        self.assertRaises(ConnectionError,
                          retrier.connect_smtp_server, smtp_server)

    def test_connect_unreachable_smtp_server_with_ip(self):
        smtp_server = '10.1.23.32'
        self.assertRaises(ConnectionRefusedError,
                          retrier.connect_smtp_server, smtp_server)
