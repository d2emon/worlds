import random
from flask import jsonify
from walk.actions import quit_game
from walk.exceptions import ActionError, StopGame
from walk.parser import Parser
from walk.player import PLAYER
from . import blueprint


def on_error(message):
    return jsonify({'error': str(message)})


def on_stop(message):
    # pbfr()
    # Globals.pr_due = 0  # So we dont get a prompt after the exit
    # keysetback()
    return jsonify({'crapup': str(message)})


@blueprint.route('/restart', methods=['GET'])
def restart():
    PLAYER.room_id = random.choice((
        -5,
        -183,
    ))
    return jsonify({'result': True})


@blueprint.route('/quit', methods=['GET'])
def quit_system():
    try:
        return jsonify(quit_game(Parser("quit")))
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


@blueprint.route('/go/<direction>', methods=['GET'])
def go(direction):
    try:
        direction_id = Parser.get_direction_id(direction) - 2
        return jsonify(PLAYER.go(direction_id))
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


@blueprint.route('/look', methods=['GET'])
def look():
    try:
        room = PLAYER.look()
        return jsonify({
            'result': room.get('result'),
            'error': room.get('error'),
            'room': room,
        })
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


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
