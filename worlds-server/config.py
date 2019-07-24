import os


# configuration
class Config:
    DEBUG = True

    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    SECRET_KEY = os.getenv('FLASK_SECRET', 'MySecretKey')

    FRONT = "http://localhost:8080/"
    BACK = "http://localhost:5000/"

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)

    MEDIA_URL = BACK + 'media'
    MEDIA_FOLDER = os.path.join(ROOT_DIR, 'media')

    DIST_ROOT = os.path.join(ROOT_DIR, 'dist')
    WIKI_ROOT = os.path.join(MEDIA_FOLDER, 'wiki')

    RESIZE_URL = MEDIA_URL + '/images'
    RESIZE_ROOT = os.path.join(MEDIA_FOLDER, 'images')

    # if not os.path.exists(DIST_DIR):
    #     raise Exception("DIST_DIR not found: {}".format(DIST_DIR))
