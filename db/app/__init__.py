from config import Config
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)
app.config.from_object(Config)

# Modules
CORS(app)

login = LoginManager(app)
login.login_view = 'login'

mail = Mail(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)


from app import handlers, routes, models, errors
