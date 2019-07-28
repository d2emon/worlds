import os
import requests
from flask import Flask, current_app, jsonify, make_response, send_file, send_from_directory
from flask_cors import CORS
from flask_resize import Resize


# instantiate the app
app = Flask(__name__)

# Configuration
app.config.from_object('config.Config')
if app.debug:
    app.logger.info('Config: {}'.format(app.config))

# Modules
CORS(app)
resize = Resize(app)

# Blueprints
from .images import blueprint as images
app.register_blueprint(images)

# API
from .api.categories import blueprint as categories
app.register_blueprint(categories)

from .api.portal import blueprint as portal
app.register_blueprint(portal)

from .api.worlds import blueprint as worlds
app.register_blueprint(worlds)

from .api.generated import blueprint as generated
app.register_blueprint(generated)


@app.route('/<path:path>')
@app.route('/', defaults={'path': ''})
def index(path):
    if current_app.config.get('FLASK_ENV') == 'development':
        spa = requests.get("{}{}".format(current_app.config.get('FRONT'), path))
        return (
            spa.content,
            spa.status_code,
            spa.headers.items()
        )

    return send_file(os.path.join(current_app.config.get('DIST_ROOT'), 'index.html'))


# error 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# media
@app.route('/files/<path:path>')
def media(path):
    path = os.path.join(current_app.config.get('MEDIA_FOLDER'), path)
    if not os.path.exists(path):
        return make_response(jsonify({'error': 'Media not found'}), 404)
    return send_file(os.path.join(current_app.config.get('MEDIA_FOLDER'), path))
    # return send_from_directory(current_app.config.get('MEDIA_FOLDER'), filename, as_attachment=True)
