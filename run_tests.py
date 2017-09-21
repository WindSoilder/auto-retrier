import unittest

from tests.core import CoreFunctionTest
from tests.mail import MailTest


def suite():
    suite = unittest.TestSuite()
    loader = unittest.defaultTestLoader
    suite.addTest(loader.loadTestsFromTestCase(CoreFunctionTest))
    suite.addTest(loader.loadTestsFromTestCase(MailTest))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest="suite")
