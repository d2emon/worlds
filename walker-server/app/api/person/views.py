from flask import request
from . import blueprint
from database.person import Person


def get_value(key, default=None):
    value = (request.json and request.json.get(key)) or request.values.get(key)
    return value if value is not None else default


@blueprint.route('/<name>', methods=['GET'])
def get_person(name):
    try:
        person = next(Person.get(name), None)
        if person is None:
            return {'error': "Person not found"}, 404
        return {'person': person.serialize()}
    except Exception as e:
        return {'error': str(e)}, 500


@blueprint.route('/<name>', methods=['PUT'])
def put_person(name):
    person = next(Person.get(name), Person())
    person.name = name
    person.strength = get_value('strength', person.strength)
    person.level = get_value('level', person.level)
    person.flags = get_value('flags', person.flags)
    person.score = get_value('score', person.score)
    person.save()
    return {'person': person.serialize()}


@blueprint.route('/<name>', methods=['DELETE'])
def delete_person(name):
    person = next(Person.get(name), None)
    if person is None:
        return {'error': "Person not found"}, 404
    return {'result': person.remove()}
