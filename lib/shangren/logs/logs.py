"""Logging module standardizes use of logging."""

from typing import Optional
import logging
import graypy


def setup(logger: logging.Logger, filename: Optional[str]=None) -> logging.Logger:
    # create formatter
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s (%(message)s)')

    # create file handler which logs even debug messages
    if filename is not None:
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # graylog handler
    graypy_handler = graypy.GELFHandler('graylog.pi', 12201)
    graypy_handler.setLevel(logging.DEBUG)
    logger.addHandler(graypy_handler)

    logger.setLevel(logging.DEBUG)

    return logger
