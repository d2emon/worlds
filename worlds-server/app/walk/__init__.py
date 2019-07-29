from flask import Blueprint


blueprint = Blueprint('walk_blueprint', __name__, url_prefix='/walk')


from .views import *
