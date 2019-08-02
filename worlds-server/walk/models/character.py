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
            if not len(pname(character_id)) or ploc(character_id) == player.room_id or not seeplayer(character_id):
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


def plev(*args):
    # raise NotImplementedError()
    print("plev({})".format(args))
    return random.randrange(100)


def ploc(*args):
    # raise NotImplementedError()
    print("plev({})".format(args))
    return random.randrange(100)


def pname(*args):
    # raise NotImplementedError()
    print("pname({})".format(args))
    return "TEXT"


def psex(*args):
    # raise NotImplementedError()
    print("psex({})".format(args))
    return 1 if random.randrange(100) > 50 else 0


def seeplayer(*args):
    # raise NotImplementedError()
    print("seeplayer({})".format(args))
    return True
