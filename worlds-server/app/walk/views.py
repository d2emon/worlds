from flask import jsonify, request
from walk.exceptions import ActionError, StopGame
from walk.models.item import Item
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


def do_action(action, *args, **kwargs):
    try:
        return jsonify(action(*args, **kwargs) or {})
    except ActionError as e:
        return on_error(e)
    except StopGame as e:
        return on_stop(e)


@blueprint.route('/oops', methods=['GET'])
def oops():
    return do_action(Player.player().on_error)


@blueprint.route('/ctrlc', methods=['GET'])
def ctrlc():
    return do_action(Player.player().on_quit)


@blueprint.route('/start/<name>', methods=['GET'])
def start(name):
    response = Player.restart(name)
    app.logger.info("GAME ENTRY: %s[%s]", Player.player().name, request.remote_addr)
    return jsonify(response)


@blueprint.route('/wait', methods=['GET'])
def wait():
    return do_action(Player.player().wait)


@blueprint.route('/go/<direction>', methods=['GET'])
def go(direction):
    def action():
        direction_id = Parser.get_direction_id(direction) - 2
        return Player.player().go(direction_id)
    return do_action(action)


@blueprint.route('/quit', methods=['GET'])
def quit_system():
    return do_action(Player.player().quit_game)


@blueprint.route('/take/', methods=['GET'])
@blueprint.route('/take/<item>', methods=['GET'])
def take(item=None):
    if item is None:
        return jsonify({'error': "Get what?"})
    return do_action(Player.player().take, next(Item.find(slug=item), None))


@blueprint.route('/take/<item>/from/', methods=['GET'])
@blueprint.route('/take/<item>/from/<container>', methods=['GET'])
@blueprint.route('/take/<item>/out/<container>', methods=['GET'])
def take_from(item, container=None):
    if container is None:
        return jsonify({'error': "From what?"})

    def action(item_name, container_name):
        player = Player.player()
        c = player.find_item(slug=container_name, available_for=player.character)
        if c is None:
            return {'error': "You can't take things from that - it's not here"}
        return player.take(player.find_item(slug=item_name, container=c))
    return do_action(action, item, container)


@blueprint.route('/drop/', methods=['GET'])
@blueprint.route('/drop/<item>', methods=['GET'])
def drop(item=None):
    if item is None:
        return jsonify({'error': "Drop what?"})
    return do_action(Player.player().drop, next(Item.find(slug=item), None))


@blueprint.route('/inventory', methods=['GET'])
def inventory():
    return do_action(Player.player().get_inventory)


@blueprint.route('/who', methods=['GET'])
def who():
    return do_action(Player.player().who)


@blueprint.route('/look', methods=['GET'])
def look():
    return do_action(Player.player().look)


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
    return do_action(Player.player().list_exits)


@blueprint.route('/jump', methods=['GET'])
def jump():
    return do_action(Player.player().jump)


@blueprint.route('/dig', methods=['GET'])
def dig():
    return do_action(Player.player().dig)
