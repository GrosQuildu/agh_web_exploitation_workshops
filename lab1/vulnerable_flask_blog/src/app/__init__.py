import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_login import LoginManager
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from config import Config, APP_DIR
from app.setup import randomFlag
from app.proxy import ReverseProxied
from shutil import copyfile
from glob import glob

app = Flask(__name__)
app.config.from_object(Config)
# app.wsgi_app = ReverseProxied(app.wsgi_app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
dotenv_path = os.path.join(APP_DIR, '.env')
load_dotenv(dotenv_path)
login = LoginManager(app)
login.login_view = 'login'

if not os.path.exists('/tmp/suspicious_file.txt'):
    with open('/tmp/suspicious_file.txt', 'w+') as f:
        f.write('yeah-there-should-be-our-flag')

randomFlag()

if not os.path.exists('./app/static/__pycache__'):
    os.mkdir('./app/static/__pycache__')
    
for f in glob(r'./app/__pycache__/setup.cpython*.pyc'):
    copyfile(f, './app/static/__pycache__/{}'.format(os.path.basename(f)))

if os.path.exists('./app/static/setup.py'):
    os.remove('./app/static/setup.py')

from app import routes, models, errors