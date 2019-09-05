from flask import jsonify
from . import blueprint
from data.worlds import WORLDS, World


@blueprint.route('/', methods=['GET'])
def worlds():
    return jsonify({
        'status': 'success',
        'worlds': [World(**data).as_dict() for data in WORLDS.all()],
    })


@blueprint.route('/world/<world_id>', methods=['GET'])
def world(world_id):
    data = WORLDS.by_slug(world_id)
    if data is None:
        return jsonify({'status': 'fail'})

    return jsonify({
        'status': 'success',
        'world': World(**data).as_dict(full=True),
    })


@blueprint.route('/world/<world_id>/wiki/<path:page>', methods=['GET'])
def get_wiki(world_id, page):
    data = WORLDS.by_slug(world_id)
    if data is None:
        return jsonify({'status': 'fail'})

    return jsonify({
        'status': 'success',
        'wiki': World(**data).get_wiki(page),
    })


@blueprint.route('/world/<world_id>/planet/<planet>', methods=['GET'])
def get_planet(world_id, planet):
    data = WORLDS.by_slug(world_id)
    if data is None:
        return jsonify({'status': 'fail'})

    return jsonify({
        'status': 'success',
        'planet': World(**data).get_planet(planet),
    })
