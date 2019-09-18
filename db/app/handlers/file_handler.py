import os
from logging.handlers import RotatingFileHandler


def file_handler(config):
    path = config.get('LOG_PATH')
    if not os.path.exists(path):
        # os.mkdir(path)
        return None
    if not config.get('LOG_FILE'):
        return None
    return RotatingFileHandler(config.get('LOG_FILE'), maxBytes=10240, backupCount=10)
