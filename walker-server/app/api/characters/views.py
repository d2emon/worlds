from . import blueprint
from app.api.helpers import try_response
from database.character import Character


@blueprint.route('/find/<name>', methods=['GET'])
def find_character(name):
    return try_response(lambda: {
        'character': next(Character.find(name), None),
    })
