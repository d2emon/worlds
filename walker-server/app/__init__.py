# import os
# import requests
from flask import Flask, current_app, jsonify, make_response, send_file, send_from_directory
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)

# Configuration
app.config.from_object('config.Config')
if app.debug:
    app.logger.info('Config: {}'.format(app.config))

# Modules
CORS(app)

# Blueprints
# from .images import blueprint as images
# app.register_blueprint(images)

# API
from .api.characters import blueprint as characters
app.register_blueprint(characters)

from .api.person import blueprint as person
app.register_blueprint(person)


# error 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
