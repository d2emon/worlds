from flask import jsonify
from . import blueprint
from data.worlds import WORLDS, World


@blueprint.route('/', methods=['GET'])
def worlds():
    return jsonify({
        'status': 'success',
        'worlds': [World(**data).as_dict() for data in WORLDS.all()],
    })


@blueprint.route('/<slug>', methods=['GET'])
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
