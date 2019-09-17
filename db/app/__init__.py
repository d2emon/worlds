from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

# instantiate the app
app = Flask(__name__)
app.config.from_object(Config)

# Modules
CORS(app)

login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import routes, models
