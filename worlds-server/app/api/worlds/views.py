from flask import current_app
from . import blueprint
from app.api.helpers import try_response
from worlds import WorldModel


@blueprint.route('/', methods=['GET'])
def worlds():
    return try_response(lambda: {
        'worlds': [world.as_dict() for world in WorldModel.all()],
    })


@blueprint.route('/world/<world_id>', methods=['GET'])
def get_world(world_id):
    return try_response(lambda: {
        'world': WorldModel.by_slug(world_id).as_dict(full=True),
    })


@blueprint.route('/world/<world_id>', methods=['PUT'])
def put_world(world_id):
    current_app.logger.debug(world_id)
    return try_response(lambda: {
        'world': WorldModel.by_slug(world_id).as_dict(full=True),
    })


@blueprint.route('/world/<world_id>/planet/<planet_id>', methods=['GET'])
def get_planet(world_id, planet_id):
    return try_response(lambda: {
        'planet': WorldModel.planet(world_id, planet_id).as_dict(full=True),
    })


@blueprint.route('/wiki/world/<world_id>/planet/<planet_id>/<page_type>/<path:page_id>', methods=['GET'])
@blueprint.route('/wiki/world/<world_id>/page/<path:page_id>', methods=['GET'])
@blueprint.route('/wiki/page/<path:page_id>', methods=['GET'])
def get_wiki(world_id=None, planet_id=None, page_id='index', page_type='page'):
    return try_response(lambda: {
        'wiki': WorldModel.wiki(
            world_id=world_id,
            planet_id=planet_id,
            page_id=page_id,
            page_type=page_type,
        ),
    })
