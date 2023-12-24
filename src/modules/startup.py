import os, logging
from termcolor import colored
from logging import LogRecord


def init_logging():
    """Initializes logging for the bot, using the logger 'main'"""
    if os.getenv("LOGGING_LEVEL") is not None:
        logLevel = os.getenv("LOGGING_LEVEL")
        if logLevel == 'debug':
            logLevel = logging.DEBUG
        elif logLevel == 'info':
            logLevel = logging.INFO
        else:
            logLevel = logging.INFO
    else:
        logLevel = logging.INFO

    class CustomFormatter(logging.Formatter):
        FORMAT = '[%(asctime)s]  [%(funcName)s @ %(module)s] %(message)s'
        FORMATS = {
            logging.DEBUG: colored("[%(levelname)s]", "light_cyan", attrs=["bold"]) + colored(" - ", attrs=["bold"]) + colored(FORMAT, "white"),
            logging.INFO: colored("[%(levelname)s]", "cyan", attrs=["bold"]) + colored(" - ", attrs=["bold"]) + colored(FORMAT, "white"),
            logging.WARNING: colored("[%(levelname)s]", "yellow", attrs=["bold"]) + colored(" - ", attrs=["bold"]) + colored(FORMAT, "yellow"),
            logging.ERROR: colored("[%(levelname)s]", "red", attrs=["bold"]) + colored(" - ", attrs=["bold"]) + colored(FORMAT, "red"),
        }

        def format(self, record: LogRecord) -> str:
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = logging.Formatter(log_fmt)
            return formatter.format(record)

    logger = logging.getLogger("main")
    logger.setLevel(logLevel)

    ch = logging.StreamHandler()
    ch.setLevel(logLevel)
    ch.setFormatter(CustomFormatter())

    logger.addHandler(ch)

    logger.debug("Debug mode enabled")