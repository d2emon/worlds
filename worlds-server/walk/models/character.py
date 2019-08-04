import random
from ..database import World
from ..globalVars import Globals
from .model import Model


class Character(Model):
    def __init__(
        self,
        player_id,
    ):
        super().__init__()
        self.player_id = player_id

    @classmethod
    def database(cls):
        return World.instance.players

    @classmethod
    def list_characters(cls, player):
        for character_id in cls.database().all():
            if character_id == player.player_id:
                continue
            if not len(pname(character_id)) or ploc(character_id) != player.room_id or not seeplayer(character_id):
                continue
            if psex(character_id):
                Globals.wd_her = pname(character_id)
            else:
                Globals.wd_him = pname(character_id)
            yield {
                'character_id': character_id,
                'name': pname(character_id),
                'level': disl4(plev(character_id), psex(character_id)),
                'items': list(lobjsat(character_id)),
            }


def list_characters(player):
    return Character.list_characters(player)


# Not Implemented


def disl4(*args):
    # raise NotImplementedError()
    print("disl4({})".format(args))
    return "disl4({})".format(args)


def lobjsat(*args):
    # raise NotImplementedError()
    print("lobjsat({})".format(args))
    yield {}
    yield {}
    yield {}


def plev(character_id):
    # raise NotImplementedError()
    print("plev({})".format(character_id))
    character = Character.database().character(character_id)
    return character.get('level', 0)


def ploc(character_id):
    # raise NotImplementedError()
    print("ploc({})".format(character_id))
    character = Character.database().character(character_id)
    return character.get('room_id', 0)


def pname(character_id):
    # raise NotImplementedError()
    print("pname({})".format(character_id))
    character = Character.database().character(character_id)
    return character.get('name', '')


def psex(character_id):
    # raise NotImplementedError()
    print("psex({})".format(character_id))
    character = Character.database().character(character_id)
    return character.get('sex', 0)


def seeplayer(*args):
    # raise NotImplementedError()
    print("seeplayer({})".format(args))
    return True
