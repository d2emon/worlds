from flask import Blueprint


blueprint = Blueprint('generated_blueprint', __name__, url_prefix='/api/generated')


from .views import *
