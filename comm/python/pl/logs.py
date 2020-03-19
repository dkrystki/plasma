"""Logging module to standardize use of logging."""

import logging
import graypy


class GelfHandler(graypy.GELFTCPHandler):
    def __init__(self, *args, app: str, namespace: str, **kwargs):
        super().__init__(*args, extra_fields=True, **kwargs)

        self.app = app
        self.namespace = namespace

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
        record.namespace_name = self.namespace
        return super().makePickle(record)


def setup(namespace: str, app: str) -> None:
    logger = logging.getLogger(__name__)
    graypy_handler = GelfHandler('graylog-tcp.graylog', 12201, app=app, namespace=namespace)
    graypy_handler.setLevel(logging.DEBUG)
    logger.addHandler(graypy_handler)
