from flask import jsonify
from . import blueprint
from .data import CATEGORIES


@blueprint.route('/', methods=['GET'])
def all_categories():
    return jsonify({
        'status': 'success',
        'categories': CATEGORIES,
    })
