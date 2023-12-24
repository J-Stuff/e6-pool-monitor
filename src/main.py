import logging, os
from .modules.startup import init_logging

init_logging()
logger = logging.getLogger("main")
logger.debug("Logging initialized")
logger.info("Starting up...")