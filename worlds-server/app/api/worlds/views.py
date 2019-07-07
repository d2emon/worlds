from flask import jsonify
from . import blueprint
from .data import WORLDS
from .wikifiles import get_wiki


def image_url(image):
    if not image:
        image = 'portal.jpg'
    return '/media/images/worlds/{}'.format(image)


def world_text(world_data):
    wiki = world_data.get('wiki')
    if wiki is None:
        return world_data.get('text')
    return get_wiki(wiki)


@blueprint.route('/', methods=['GET'])
def worlds():
    return jsonify({
        'status': 'success',
        'worlds': [{
            'id': world_data.get('id'),
            'slug': world_data.get('slug'),
            'title': world_data.get('title'),
            'image': image_url(world_data.get('image')),
        } for world_data in WORLDS],
    })


@blueprint.route('/<slug>', methods=['GET'])
def world(slug):
    world = next((world for world in WORLDS if world.get('slug') == slug), None)
    if world is None:
        return jsonify({
            'status': 'fail',
        })

    return jsonify({
        'status': 'success',
        'world': {
            'id': world.get('id'),
            'slug': world.get('slug'),
            'title': world.get('title'),
            'image': image_url(world.get('image')),
            'text': world_text(world),
        },
    })
