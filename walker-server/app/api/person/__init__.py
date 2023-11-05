from flask import Blueprint


blueprint = Blueprint('person_blueprint', __name__, url_prefix='/api/person')


from .views import *
