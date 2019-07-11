from flask import jsonify
from . import blueprint
from data.geneverse import GENEVERSE, Thing, THING_ERROR


@blueprint.route('/', methods=['GET'])
def geneverse():
    return jsonify({
        'status': 'success',
        'things': [Thing(**data).as_dict() for data in GENEVERSE.all()],
    })


@blueprint.route('/<slug>', methods=['GET'])
def thing(slug):
    data = GENEVERSE.by_slug(slug)
    if data is None:
        return jsonify({
            'status': 'fail',
            'thing': THING_ERROR.as_dict(),
        })

    return jsonify({
        'status': 'success',
        'thing': Thing(**data).as_dict(),
    })
