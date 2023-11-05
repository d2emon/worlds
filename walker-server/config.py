import os


# configuration
class Config:
    DEBUG = True

    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    SECRET_KEY = os.getenv('FLASK_SECRET', 'MySecretKey')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)

    # MEDIA_URL = BACK + 'files'
    MEDIA_FOLDER = os.path.join(ROOT_DIR, 'media')

    WIKI_ROOT = os.path.join(MEDIA_FOLDER, 'wiki')

    # RESIZE_URL = MEDIA_URL
    # RESIZE_ROOT = os.path.join(MEDIA_FOLDER)
