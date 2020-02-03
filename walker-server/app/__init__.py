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


# @app.route('/<path:path>')
# @app.route('/', defaults={'path': ''})
# def index(path):
#     if current_app.config.get('FLASK_ENV') == 'development':
#         spa = requests.get("{}{}".format(current_app.config.get('FRONT'), path))
#         return (
#             spa.content,
#             spa.status_code,
#             spa.headers.items()
#         )
#     return send_file(os.path.join(current_app.config.get('DIST_ROOT'), 'index.html'))


# error 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
