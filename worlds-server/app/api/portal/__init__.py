from flask import Blueprint


blueprint = Blueprint('portal_blueprint', __name__, url_prefix='/api/portal')


from .views import *
