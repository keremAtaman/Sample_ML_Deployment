import logging

def getLogger():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)
    return logger