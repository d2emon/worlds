import random
from ..database import World
from ..globalVars import Globals
from .model import Model
from .item import Item


class Character(Model):
    WIZARD_LEVEL = 10
    GOD_LEVEL = 10000

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
        for character in cls.find(player=player):
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

    @property
    def is_wizard(self):
        return self.level >= self.WIZARD_LEVEL

    @property
    def is_god(self):
        return self.level >= self.GOD_LEVEL

    @property
    def carry(self):
        def items_filter(i):
            if i is None:
                return False
            owner = i.carried_by
            if owner is None:
                return False
            return owner == self.character_id
        return filter(items_filter, Item.all())

    def check_move(self):
        pass

    def has_items(self, include_destroyed=False):
        if include_destroyed:
            return self.carry
        return (item for item in self.carry if not is_dest(item.item_id))

    def has_item(self, item_id, include_destroyed=False):
        return any(item for item in self.has_items(include_destroyed) if item.item_id == item_id)

    # Search
    @classmethod
    def __by_name(cls, name):
        def get_name(n):
            n = n.lower()
            return n[4:] if n[:4] == "the " else n

        def f(character):
            if not character.name:
                return False
            return get_name(name) == get_name(character.name)
        return f

    @classmethod
    def __by_player_can_see(cls, player):
        def f(character):
            if Globals.ail_blind:
                return False  # Cant see
            if player.room.is_dark:
                return False
            return character.visible > player.character.level
        return f

    @classmethod
    def __by_not_player(cls, player):
        def f(character):
            return character.character_id != player.character_id
        return f

    @classmethod
    def __by_room_id(cls, room_id):
        def f(character):
            return character.room_id == room_id
        return f

    @classmethod
    def filters(
        cls,
        player=None,
        not_player=None,
        name=None,
        room_id=None,
        wizard=None,
        exists_only=False,
        player_only=False,
        **kwargs,
    ):
        if player is not None:
            not_player = player
            room_id = player.room_id
            exists_only = True
            yield cls.__by_player_can_see(player)
        if not_player is not None:
            yield cls.__by_not_player(not_player)
        if name is not None:
            yield cls.__by_name(name)
        if room_id is not None:
            yield cls.__by_room_id(room_id)
        if wizard is not None:
            yield lambda character: character.is_wizard == wizard
        if exists_only:
            yield lambda character: character.is_created
        if player_only:
            yield lambda character: character.character_id < 32


def list_characters(player):
    return Character.list_characters(player)


# TODO: Implement


def disl4(*args):
    # raise NotImplementedError()
    print("disl4({})".format(args))
    return "disl4({})".format(args)


def is_dest(*args):
    # raise NotImplementedError()
    print("is_dest({})".format(args))
    return False


def lobjsat(*args):
    # raise NotImplementedError()
    print("lobjsat({})".format(args))
    yield {}
    yield {}
    yield {}
