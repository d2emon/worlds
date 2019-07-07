from flask import jsonify
from . import blueprint
from data.categories import CATEGORIES


@blueprint.route('/', methods=['GET'])
def all_categories():
    return jsonify({
        'status': 'success',
        'categories': CATEGORIES.all(),
    })
