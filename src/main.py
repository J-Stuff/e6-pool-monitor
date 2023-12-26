import logging, os
from modules.startup import init_logging
from termcolor import colored
from dotenv import load_dotenv

print(colored("[BOOTLOADER]", "cyan", attrs=["bold"]) + colored(" - ", attrs=["bold"]) + colored("Initializing...", "white"))
load_dotenv()
init_logging()
logger = logging.getLogger("main")
logger.debug("Logging initialized")
logger.info("Starting up...")