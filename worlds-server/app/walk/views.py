from flask import jsonify, request
from walk.models.item import Item
from walk.parser import Parser
from walk.player import Player
from .. import app
from . import blueprint
from .utils import current_player, do_action

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


# Main routes

@blueprint.route('/error', methods=['GET'])
def fatal_error():
    @do_action
    def __action():
        player = Player.restore()
        player.remove()
        return {
            'errorCode': 255,
        }
    return jsonify(__action())


@blueprint.route('/disconnect', methods=['GET'])
def disconnect():
    @do_action
    def __action():
        player = Player.restore()
        return {
            'saved': player.on_quit(),  # "Saving {}".format(self.name) if self.remove() else "",
            'message': "Byeeeeeeeeee  ...........",
        }
    return jsonify(__action())


@blueprint.route('/start/<name>', methods=['GET'])
def start(name):
    @do_action
    def __action():
        player = Player.restore()
        player.restart(name)
        app.logger.info("GAME ENTRY: %s[%s]", player.name, request.remote_addr)
        return {
            'player': player.as_dict(),
            'messages': [
                # 'message': "Hello {}".format(player.name),
            ],
        }
    return jsonify(__action())


# Actions

@blueprint.route('/wait', methods=['GET'])
def wait():
    @do_action
    def __action():
        # Disable timer
        player = current_player()
        messages = player.wait()
        # Enable timer
        return {
            'player': player.as_dict(),
            'messages': messages,
        }
    return jsonify(__action())


@blueprint.route('/go/<direction>', methods=['GET'])
def go(direction):
    @do_action
    def __action():
        direction_id = Parser.get_direction_id(direction) - 2
        return current_player().go(direction_id)
    return jsonify(__action())


@blueprint.route('/quit', methods=['GET'])
def quit_system():
    @do_action
    def __action():
        return current_player().quit_game()
    return jsonify(__action())


@blueprint.route('/take/', methods=['GET'])
@blueprint.route('/take/<item>', methods=['GET'])
def take(item=None):
    if item is None:
        return jsonify({'error': "Get what?"})

    @do_action
    def __action():
        return current_player().take(next(Item.find(slug=item), None))
    return jsonify(__action())


@blueprint.route('/take/<item>/from/', methods=['GET'])
@blueprint.route('/take/<item>/from/<container>', methods=['GET'])
@blueprint.route('/take/<item>/out/<container>', methods=['GET'])
def take_from(item, container=None):
    if container is None:
        return jsonify({'error': "From what?"})

    @do_action
    def __action(item_name, container_name):
        player = current_player()
        c = player.find_item(slug=container_name, available_for=player.character)
        if c is None:
            return {'error': "You can't take things from that - it's not here"}
        return player.take(player.find_item(slug=item_name, container=c))
    return jsonify(__action(item, container))


@blueprint.route('/drop/', methods=['GET'])
@blueprint.route('/drop/<item>', methods=['GET'])
def drop(item=None):
    if item is None:
        return jsonify({'error': "Drop what?"})

    @do_action
    def __action():
        return current_player().drop(next(Item.find(slug=item), None))
    return jsonify(__action())


@blueprint.route('/look', methods=['GET'])
def look():
    @do_action
    def __action():
        return current_player().look()
    return jsonify(__action())


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


@blueprint.route('/inventory', methods=['GET'])
def inventory():
    @do_action
    def __action():
        return current_player().get_inventory()
    return jsonify(__action())


@blueprint.route('/who', methods=['GET'])
def who():
    @do_action
    def __action():
        return current_player().who()
    return jsonify(__action())


@blueprint.route('/wield', methods=['GET'])
@blueprint.route('/wield/<weapon>', methods=['GET'])
def wield(weapon=None):
    if weapon is None:
        return jsonify({'error': "Which weapon do you wish to select though"})
    player = current_player()

    @do_action
    def __action():
        return player.wield(
            player.find_item(slug=weapon, owner=player),
        )
    return jsonify(__action())


@blueprint.route('/break/<item>', methods=['GET'])
def break_item(item=None):
    if item is None:
        return jsonify({'error': "Kill who"})
    if item == "door":
        return jsonify({'error': "Who do you think you are, Moog?"})
    player = current_player()

    @do_action
    def __action():
        return player().break_item(
            player.find_item(slug=item, available_for=player),
        )
    return jsonify(__action())


@blueprint.route('/kill', methods=['GET'])
@blueprint.route('/kill/<victim>', methods=['GET'])
@blueprint.route('/kill/<victim>/with/<weapon>', methods=['GET'])
def kill(victim=None, weapon=None):
    if victim is None:
        return jsonify({'error': "Kill who"})
    player = current_player()

    @do_action
    def __action():
        return player.kill(
            player.find_character(name=victim),
            player.find_item(slug=weapon, owner=player),
        )
    return jsonify(__action())


@blueprint.route('/exits', methods=['GET'])
def exits():
    @do_action
    def __action():
        return current_player().list_exits()
    return jsonify(__action())


@blueprint.route('/jump', methods=['GET'])
def jump():
    @do_action
    def __action():
        return current_player().jump()
    return jsonify(__action())


@blueprint.route('/dig', methods=['GET'])
def dig():
    @do_action
    def __action():
        return current_player().dig()
    return jsonify(__action())
