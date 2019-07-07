from flask import Blueprint


blueprint = Blueprint('categories_blueprint', __name__, url_prefix='/api/categories')


from .views import *
