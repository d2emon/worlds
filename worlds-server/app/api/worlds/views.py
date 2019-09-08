from flask import jsonify
from . import blueprint
from data.worlds import WORLDS, World


class RecordNotFound(Exception):
    pass


def world_by_slug(slug):
    data = WORLDS.by_slug(slug)
    if data is None:
        raise RecordNotFound()
    return World(**data)


def planet_by_slug(world_id, planet_id):
    item = world_by_slug(world_id).get_planet(planet_id)
    if item is None:
        raise RecordNotFound()
    return item


def wiki_by_slug(world_id=None, planet_id=None, page_id=None):
    if world_id is None:
        return None
    return world_by_slug(world_id).get_wiki(
        planet_id=planet_id,
        page_id=page_id,
    )


def try_response(f):
    try:
        return jsonify({
            'status': 'success',
            **f(),
        })
    except RecordNotFound:
        return jsonify({'status': 'fail'})


@blueprint.route('/', methods=['GET'])
def worlds():
    return try_response(lambda: {
        'worlds': [World(**data).as_dict() for data in WORLDS.all()],
    })


@blueprint.route('/world/<world_id>', methods=['GET'])
def get_world(world_id):
    return try_response(lambda: {
        'world': world_by_slug(world_id).as_dict(full=True),
    })


@blueprint.route('/world/<world_id>/planet/<planet_id>', methods=['GET'])
def get_planet(world_id, planet_id):
    return try_response(lambda: {
        'planet': planet_by_slug(world_id, planet_id).as_dict(),
    })


@blueprint.route('/wiki/world/<world_id>/planet/<planet_id>/page/<path:page_id>', methods=['GET'])
@blueprint.route('/wiki/world/<world_id>/page/<path:page_id>', methods=['GET'])
@blueprint.route('/wiki/page/<path:page_id>', methods=['GET'])
def get_wiki(world_id=None, planet_id=None, page_id='index'):
    return try_response(lambda: {
        'wiki': wiki_by_slug(
            world_id=world_id,
            planet_id=planet_id,
            page_id=page_id,
        ),
    })
