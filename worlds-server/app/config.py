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
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')
    WIKI_DIR = os.path.join(ROOT_DIR, 'wiki')

    MEDIA_FOLDER = os.path.join(ROOT_DIR, 'media')

    RESIZE_URL = BACK + 'media/images'
    RESIZE_ROOT = os.path.join(MEDIA_FOLDER, 'images')

    # SQLALCHEMY_DATABASE_URI = "sqlite://"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # if not os.path.exists(DIST_DIR):
    #     raise Exception("DIST_DIR not found: {}".format(DIST_DIR))
