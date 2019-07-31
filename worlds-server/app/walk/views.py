from flask import jsonify
from walk.exceptions import ActionError
from walk.parser import Parser
from walk.room import look_room, go_direction
from . import blueprint


@blueprint.route('/go/<direction>', methods=['GET'])
def go(direction):
    try:
        direction_id = Parser.get_direction_id(direction)
        return jsonify(go_direction(direction_id))
    except ActionError as e:
        return jsonify({'error': str(e)})


@blueprint.route('/look', methods=['GET'])
def look():
    room = look_room()
    return jsonify({
        'result': not room['error'],
        'error': room['error'],
        'room': room,
    })


@blueprint.route('/look/at/<word>', methods=['GET'])
def look_at(word):
    # examcom()
    return jsonify({'result': 'Ok'})


@blueprint.route('/look/in/', methods=['GET'])
@blueprint.route('/look/into/', methods=['GET'])
@blueprint.route('/look/in/<word>', methods=['GET'])
@blueprint.route('/look/into/<word>', methods=['GET'])
def look_in(word=None):
    if word is None:
        return jsonify({'error': "In what?"})

    # a = fobna(word)
    # if a is None:
    #   return jsonify({'error': "What?"})
    # if not a.bit[14]:
    #   return jsonify({'error': "That isn't a container"})
    # if a.bit[2] and a.state != 0:
    #   return jsonify({'error': "It's closed!"})
    # bprintf("The %s contains:\n",oname(a))
    # aobjsat(a,3)
    return jsonify({'result': 'Ok'})
