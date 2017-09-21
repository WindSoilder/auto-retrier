import socket
from smtplib import SMTP
from email.message import EmailMessage


def set_message(sender: str, receiver: str,
                subject: str, content: str) -> EmailMessage:
    ''' set message information and return EmailMessage object '''
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content = content
    return msg


def connect_smtp_server(smtp_server: str, port: int=25) -> SMTP:
    ''' connect to smtp server and return the relative object '''
    try:
        smtp_server = SMTP(host=smtp_server, port=port)
    except socket.gaierror as e:
        raise ConnectionError(e.strerror)
    else:
        return smtp_server


def login_smtp_server(smtp: SMTP, username: str, password: str) -> None:
    ''' login to smtp server through username and password '''
    smtp.login(username, password)
