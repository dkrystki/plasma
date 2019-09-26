import sys
import unittest
import logging
import tempfile
import unittest.mock as mock
from pathlib import PosixPath
from io import StringIO

import ptcomm.logs


class LoggingTestCase(unittest.TestCase):
    def setUp(self):
        self.test_dir = PosixPath(tempfile.mkdtemp())
        self.old_stderr = sys.stderr
        sys.stderr = self.test_stderr = StringIO()

    def tearDown(self):
        sys.stderr = self.old_stderr

    @mock.patch('graypy.handler.DatagramHandler.send')
    def test_logging(self, mock_graypy_send):
        filename = self.test_dir/"log.log"
        logger = logging.getLogger(__name__)  # pylint: disable=
        ptcomm.logs.setup(logger, filename)

        with open(filename, 'r') as f:
            self.assertEqual(len(f.read()), 0)

        mock_graypy_send.assert_not_called()
        logger.info("test")
        mock_graypy_send.assert_called()

        self.assertGreater(len(self.test_stderr.getvalue()), 0)

        with open(filename, 'r+') as f:
            self.assertGreater(len(f.read()), 0)

if __name__ == '__main__':
    unittest.main()