import os, logging
logger = logging.getLogger("main")
class E621_API():
    def __init__(self) -> None:
        if os.getenv("E621_USERNAME") == None:
            logger.error("E621_USERNAME environment variable not set! Read the repo README for more info and to know why this is required.")
            exit("E621_USERNAME environment variable not set! Read the repo README for more info and to know why this is required.")