import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import os

TODAY_ISO = datetime.today().date().isoformat()
CURRENT_PATH = os.path.dirname(__file__)
FORMATTER = logging.Formatter(
    "%(levelname)s — %(asctime)s — %(message)s", "%Y-%m-%d %H:%M:%S")
# FORMATTER = logging.Formatter(
#     "%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = f"{CURRENT_PATH}/logs/{TODAY_ISO}.log"


class CustomLogger:

    @staticmethod
    def get_console_handler():
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(FORMATTER)
        return console_handler

    @staticmethod
    def get_file_handler():
        file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
        file_handler.setFormatter(FORMATTER)
        return file_handler

    @classmethod
    def get_logger(cls, logger_name):
        logger = logging.getLogger(logger_name)
        # better to have too much log than not enough
        logger.setLevel(logging.DEBUG)
        logger.addHandler(cls.get_console_handler())
        logger.addHandler(cls.get_file_handler())
        # with this pattern, it's rarely necessary to propagate the error up to parent
        logger.propagate = False
        return logger
