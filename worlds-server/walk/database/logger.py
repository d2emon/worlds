import logging


handler = logging.StreamHandler()
logger = logging.getLogger('DB')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
