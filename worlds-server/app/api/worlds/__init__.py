from flask import Blueprint


blueprint = Blueprint('worlds_blueprint', __name__, url_prefix='/api/worlds')


from .views import *
