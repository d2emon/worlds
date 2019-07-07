from flask import jsonify
from . import blueprint
from data.worlds import WORLDS


@blueprint.route('/', methods=['GET'])
def worlds():
    return jsonify({
        'status': 'success',
        'worlds': [{
            'id': world_data.get('id'),
            'slug': world_data.get('slug'),
            'title': world_data.get('title'),
            'image': WORLDS.image_url(world_data),
        } for world_data in WORLDS.all()],
    })


@blueprint.route('/<slug>', methods=['GET'])
def world(slug):
    world_data = WORLDS.by_slug(slug)
    if world_data is None:
        return jsonify({
            'status': 'fail',
        })

    return jsonify({
        'status': 'success',
        'world': {
            'id': world_data.get('id'),
            'slug': world_data.get('slug'),
            'title': world_data.get('title'),
            'image': WORLDS.image_url(world_data),
            'text': WORLDS.world_text(world_data),
        },
    })
