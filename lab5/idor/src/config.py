import os
APP_DIR = os.path.abspath(os.path.dirname(__file__))
START_ID = 12

ADMIN_PASS = os.environ.get('ADM_PASS', 'lol')
ADMIN_PATH = os.environ.get('ADM_PATH', '/really-weird-path-as-censored')
FLAG_IDOR = os.environ.get('FLAG_IDOR', 'try-this-but-remotely')
FLAG_IDOR_SLUG = os.environ.get('FLAG_IDOR_SLUG', "8")
MAGIC_FLAG = os.environ.get('MAGIC_FLAG', 'oh-wow-you-got-here')
MAGIC_FLAG_SLUG = os.environ.get('MAGIC_SLUG', 'you-wont-bruteforce-it')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-secret-key-really'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(APP_DIR, 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SITE_WIDTH = 800
    FLASK_DEBUG = 0
