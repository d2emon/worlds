import os


# configuration
class Config:
    DEBUG = True

    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    SECRET_KEY = os.getenv('FLASK_SECRET', 'MySecretKey')

    FRONT = os.getenv('WORLDS_FRONT', "http://127.0.0.1:8080/")
    BACK = os.getenv('WORLDS_BACK', "http://127.0.0.1:5000/")

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)

    MEDIA_URL = BACK + 'files'
    MEDIA_FOLDER = os.path.join(ROOT_DIR, 'media')

    DIST_ROOT = os.path.join(ROOT_DIR, 'dist')
    WIKI_ROOT = os.path.join(MEDIA_FOLDER, 'wiki')

    RESIZE_URL = MEDIA_URL
    RESIZE_ROOT = os.path.join(MEDIA_FOLDER)

    # if not os.path.exists(DIST_DIR):
    #     raise Exception("DIST_DIR not found: {}".format(DIST_DIR))
