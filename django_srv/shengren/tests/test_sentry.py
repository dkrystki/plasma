import unittest
from unittest.mock import patch

import raven

from shengren.sentry import Sentry


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = raven.Client('http://38be5e94729741d886accf2f95a856a0:68fd34b485644fbb8d70c76d24f4d41f@sentry.pi/2')

    @patch('raven.Client.captureException')
    def test_fun(self, mock_capture_exception):
        @Sentry(self.client)
        def fun():
            a = 1/0

        with self.assertRaises(ZeroDivisionError):
            fun()
        mock_capture_exception.assert_called_once()

    @patch('raven.Client.captureException')
    def test_cls(self, mock_capture_exception):
        @Sentry(self.client)
        class Cls:
            def failing(self):
                a = 1/0

            def not_failing(self):
                a = 2

        with self.assertRaises(ZeroDivisionError):
            obj = Cls()
            obj.failing()

        obj = Cls()
        obj.not_failing()

        mock_capture_exception.assert_called_once()

if __name__ == '__main__':
    unittest.main()
