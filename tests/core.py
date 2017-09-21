'''
unittest for functions in core.py
'''
import unittest
from .context import retrier


class CoreFunctionTest(unittest.TestCase):
    def test_auto_retry(self):
        url = 'http://www.bing.com'
        email = 'test@email.com'
        self.assertTrue(retrier.auto_retry(url, email))

    def test_auto_retry_when_lack_schema(self):
        url = 'www.bing.com'
        email = 'test@email.com'
        self.assertTrue(retrier.auto_retry(url, email))

    def test_is_server_side_error(self):
        expect_err_codes = [500, 501, 502, 503, 504]
        for err_code in expect_err_codes:
            self.assertTrue(retrier.is_server_side_error(err_code))
        client_err_codes = [400, 404, 403]
        for err_code in client_err_codes:
            self.assertFalse(retrier.is_server_side_error(err_code))
