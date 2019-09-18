import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    ADMINS = ['admin@example.com']

    # Log
    LOG_PATH = os.environ.get('LOG_PATH') or os.path.join(basedir, 'log')
    LOG_FILE = os.environ.get('LOG_FILE') or os.path.join(LOG_PATH, 'blog.log')

    # Mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT') or 25
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    POSTS_PER_PAGE = 25

    # Secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'blog-secret-key'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
