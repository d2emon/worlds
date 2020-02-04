from flask import current_app, request
from . import blueprint
from app.api.helpers import try_response
from database.character import Character


@blueprint.route('/character', methods=['POST'])
def start_character():
    name = request.json.get('name') or request.values.get('name')
    try:
        return {'character': Character.start(name).serialize()}
    except AssertionError as e:
        return {'error': str(e)}, 400
    except OverflowError as e:
        return {'error': str(e)}, 400
    except Exception as e:
        return {'error': str(e)}, 500


@blueprint.route('/character/<character_id>', methods=['GET'])
def get_character(character_id):
    try:
        character = next(Character.get(character_id), None)
        if character is None:
            return {'error': "Character not found"}, 404
        return {'character': character.serialize()}
    except Exception as e:
        return {'error': str(e)}, 500


@blueprint.route('/character/<character_id>', methods=['PUT'])
def put_character(character_id):
    character = next(Character.get(character_id), None)
    if character is None:
        return {'error': "Character not found"}, 404

    event_id = (request.json and request.json.get('event_id')) or request.values.get('event_id')
    if event_id is not None:
        character.event_id = event_id
    character.save()

    return {'character': character.serialize()}


@blueprint.route('/find/<name>', methods=['GET'])
def find_character(name):
    try:
        character = next(Character.find(name), None)
        return {'character': character.serialize() if character else None}
    except Exception as e:
        return {'error': str(e)}, 500
