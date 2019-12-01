"""Logging module to standardize use of logging."""

import logging
import graypy
from loguru import logger


class GelfHandler(graypy.GELFTCPHandler):
    def __init__(self, *args, app: str, **kwargs):
        super().__init__(*args, extra_fields=True, **kwargs)

        self.app = app

    def makePickle(self, record):
        """Add a null terminator to generated pickles as TCP frame objects
        need to be null terminated

        :param record: :class:`logging.LogRecord` to create a null
            terminated GELF log.
        :type record: logging.LogRecord

        :return: Null terminated bytes representing a GELF log.
        :rtype: bytes
        """
        record.app = self.app
        return super().makePickle(record)


def setup(app: str) -> None:
    graypy_handler = GelfHandler('graylog-tcp.graylog', 12201, app=app)
    graypy_handler.setLevel(logging.DEBUG)
    logger.add(graypy_handler, format="{message}", colorize=False)
