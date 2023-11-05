from flask import Blueprint


blueprint = Blueprint('characters_blueprint', __name__, url_prefix='/api/character')


from .views import *
