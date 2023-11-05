from flask import Blueprint


blueprint = Blueprint('wiki_blueprint', __name__, url_prefix='/api/wiki')


from .views import *
