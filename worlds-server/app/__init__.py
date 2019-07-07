import os
import requests
from flask import Flask, current_app, jsonify, make_response, send_file, send_from_directory
from flask_cors import CORS
from flask_resize import Resize


# instantiate the app
app = Flask(
    __name__,
    # static_folder="../paperdoll-inventory/public",
    # template_folder="../paperdoll-inventory",
)

# Configuration
app.config.from_object('app.config.Config')
if app.debug:
    app.logger.info('Config: {}'.format(app.config))

# enable CORS
CORS(app)

# resizer
resize = Resize(app)

# Blueprints
from .api.categories import blueprint as categories
app.register_blueprint(categories)

from .api.images import blueprint as images
app.register_blueprint(images)

from .api.portal import blueprint as portal
app.register_blueprint(portal)

from .api.worlds import blueprint as worlds
app.register_blueprint(worlds)


@app.route('/<path:path>')
@app.route('/', defaults={'path': ''})
def index(path):
    if current_app.config['FLASK_ENV'] == 'development':
        spa = requests.get("{}{}".format(current_app.config['FRONT'], path))
        return (
            spa.content,
            spa.status_code,
            spa.headers.items()
        )

    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    # return app.send_static_file("index.html")
    # return render_template("index.html")
    # return send_from_directory(dist_dir, path)
    return send_file(entry)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# error 404
@app.errorhandler(404)
def not_found(error):
    print(error)
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/media/<path:filename>')
def download_file(filename):
    return send_from_directory(current_app.config.get('MEDIA_FOLDER'), filename, as_attachment=True)
