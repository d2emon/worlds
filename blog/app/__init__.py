from flask import Flask
from flask_cors import CORS
from config import Config

# instantiate the app
app = Flask(__name__)
app.config.from_object(Config)

# Modules
CORS(app)

from app import routes
