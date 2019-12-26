import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'blog-secret-key'
    WTF_CSRF_ENABLED = False
