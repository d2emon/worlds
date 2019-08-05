import random
from ..database import World
from ..globalVars import Globals
from .model import Model


class Character(Model):
    def __init__(
        self,
        character_id,
        name="",
        room_id=0,
        message_id=-1,
        strength=0,
        visible=0,
        level=0,
        weapon=None,
        helping=None,
        sex=0,
        is_aggressive=False,
        is_undead=False,
    ):
        super().__init__()
        self.character_id = character_id
        self.name = name
        self.room_id = room_id
        self.message_id = message_id
        self.strength = strength
        self.visible = visible
        self.level = level
        self.weapon = weapon
        self.helping = helping
        self.sex = sex
        self.is_aggressive = is_aggressive
        self.is_undead = is_undead

    @classmethod
    def database(cls):
        return World.instance.players

    @classmethod
    def list_characters(cls, player):
        def characters_filter(c):
            if c.character_id == player.character_id:
                return False
            if not c.is_created:
                return False
            if c.room_id != player.room_id:
                return False
            return seeplayer(c.character_id)

        for character in filter(characters_filter, cls.all()):
            if character.sex:
                Globals.wd_her = character.name
            else:
                Globals.wd_him = character.name
            yield {
                'character_id': character.character_id,
                'name': character.name,
                'level': disl4(character.level, character.sex),
                'items': list(lobjsat(character.character_id)),
            }

    @property
    def is_created(self):
        return len(self.name) > 0


def list_characters(player):
    return Character.list_characters(player)


# TODO: Implement


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


def seeplayer(*args):
    # raise NotImplementedError()
    print("seeplayer({})".format(args))
    return True
