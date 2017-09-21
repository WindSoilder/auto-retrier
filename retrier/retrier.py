import logging
import socket

from .core import try_fetch_until_success, is_server_side_error
from .mail import set_message, connect_smtp_server,\
    login_smtp_server


def auto_retry(url: str, receiver: str) -> bool:
    ''' try to fetch url until success, and send email to notify it '''
    DEFAULT_SUBJECT = 'Access success for {url}'.format(url=url)
    DEFAULT_CONTENT = '''
        Access success now, you can try to access the page by your self
    '''

    try_fetch_until_success(url)
    try:
        smtp_server = connect_smtp_server('localhost')
    except ConnectionRefusedError as e:
        logging.error('Connect to local smtp server failed '
                      'may be there is no smtp server here')
        return False
    else:
        self_identify = 'auto-retrier@retrier.com'
        msg = set_message(self_identify, receiver,
                          DEFAULT_SUBJECT, DEFAULT_CONTENT)
        smtp_server.send_message(msg)
        smtp_server.close()
        return True
