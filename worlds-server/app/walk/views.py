from flask import jsonify, request
from walk.exceptions import ActionError, StopGame
from walk.parser import Parser
from walk.player import Player
from .. import app
from . import blueprint

# from walk.models.room import Room
# from walk.models.room_exit import Exit
# from walk.models.zone import Zone


# print([[
#     item.room_id,
#     item.name,
#     item.title,
#     [e.door_id for e in item.exits if e.door_id is not None],
# ] for item in Room.all()])
# print(list(Exit.all()))
# print([item.name for item in Zone.all()])


def on_error(message):
    return jsonify({'error': str(message)})


def on_stop(message):
    return jsonify({
        'messages': Player.player().on_stop_game(),
        'crapup': str(message),
    })


@blueprint.route('/oops', methods=['GET'])
def oops():
    try:
        return jsonify(Player.player().on_error() or {})
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


@blueprint.route('/ctrlc', methods=['GET'])
def ctrlc():
    try:
        return jsonify(Player.player().on_quit() or {})
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


@blueprint.route('/start/<name>', methods=['GET'])
def start(name):
    response = Player.restart(name)
    app.logger.info("GAME ENTRY: %s[%s]", Player.player().name, request.remote_addr)
    return jsonify(response)


@blueprint.route('/wait', methods=['GET'])
def wait():
    try:
        return jsonify(Player.player().wait() or {})
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


@blueprint.route('/go/<direction>', methods=['GET'])
def go(direction):
    try:
        direction_id = Parser.get_direction_id(direction) - 2
        return jsonify(Player.player().go(direction_id))
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


@blueprint.route('/quit', methods=['GET'])
def quit_system():
    try:
        return jsonify(Player.player().quit_game())
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


@blueprint.route('/take/', methods=['GET'])
@blueprint.route('/take/<item>', methods=['GET'])
def take(item=None):
    if item is None:
        return jsonify({'error': "Get what?"})

    player = Player.player()
    item = player.find_item(slug=item, room_id=player.room_id)

    try:
        return jsonify(player.take(item))
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


@blueprint.route('/take/<item>/from/', methods=['GET'])
@blueprint.route('/take/<item>/from/<container>', methods=['GET'])
@blueprint.route('/take/<item>/out/<container>', methods=['GET'])
def take_from(item, container=None):
    if container is None:
        return jsonify({'error': "From what?"})

    player = Player.player()
    container = player.find_item(slug=container, available_for=player.character)
    if container is None:
        return jsonify({'error': "You can't take things from that - it's not here"})
    item = player.find_item(slug=item, container=container)

    try:
        return jsonify(player.take(item))
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


@blueprint.route('/look', methods=['GET'])
def look():
    try:
        return jsonify(Player.player().look())
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


@blueprint.route('/exits', methods=['GET'])
def exits():
    try:
        return jsonify(Player.player().list_exits())
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


@blueprint.route('/jump', methods=['GET'])
def jump():
    try:
        return jsonify(Player.player().jump())
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


@blueprint.route('/dig', methods=['GET'])
def dig():
    try:
        return jsonify(Player.player().dig())
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)
