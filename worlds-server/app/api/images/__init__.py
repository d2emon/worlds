from flask import Blueprint


blueprint = Blueprint('images_blueprint', __name__, url_prefix='/thumbs')


from .views import *
