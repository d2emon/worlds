from flask import jsonify
from . import blueprint
from data.worlds import WORLDS, World


@blueprint.route('/', methods=['GET'])
def worlds():
    return jsonify({
        'status': 'success',
        'worlds': [World(**data).as_dict() for data in WORLDS.all()],
    })


@blueprint.route('/world/<slug>', methods=['GET'])
def world(slug):
    data = WORLDS.by_slug(slug)
    if data is None:
        return jsonify({
            'status': 'fail',
        })

    return jsonify({
        'status': 'success',
        'world': World(**data).as_dict(full=True),
    })


@blueprint.route('/wiki/<slug>/<path:page>', methods=['GET'])
def wiki(slug, page):
    data = WORLDS.by_slug(slug)
    if data is None:
        return jsonify({
            'status': 'fail',
        })

    return jsonify({
        'status': 'success',
        'wiki': World(**data).get_wiki(page),
    })
