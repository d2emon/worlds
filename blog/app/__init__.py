from flask import Flask
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)

# Modules
CORS(app)

from app import routes
