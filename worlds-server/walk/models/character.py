from flask import current_app
import random
import requests
from ..exceptions import StopGame
from ..database import World
from ..globalVars import Globals
from .model import Model
from .item import Item


def wraith_hit(player, damage):
    player.score -= 100 * damage
    if player.score < 0:
        player.character.set_dead()
    return {'message': "You feel weaker, as the wraiths icy touch seems to drain your very life force\n"}


class Character(Model):
    MAX_USER = 16

    WIZARD_LEVEL = 10
    GOD_LEVEL = 10000

    __URL = "http://worlds_walker_1:5000/api/character"

    def __init__(
        self,
        character_id,
        name="",
        channel_id=0,
        event_id=-1,
        strength=-1,
        visible=0,
        level=1,
        weapon=None,
        helping=None,  # ?
        sex=0,
        is_aggressive=False,
        is_undead=False,
    ):
        super().__init__()
        self.character_id = character_id
        self.name = name
        self.room_id = channel_id
        self.event_id = event_id
        self.strength = strength
        self.visible = visible
        self.level = level
        self.weapon = weapon
        self.helping = helping
        self.sex = sex
        self.is_aggressive = is_aggressive
        self.is_undead = is_undead

    @classmethod
    def __log_request(cls, url, request):
        response = request()
        current_app.logger.debug("Response from '%s' - %s", url, response.status_code)
        data = response.json()
        current_app.logger.debug(data)
        if response.status_code != 200:
            raise StopGame(data.get('error', "Unknown exception: {}".format(response.status_code)))
        return data

    @classmethod
    def __post(cls, url, json):
        current_app.logger.debug("POST %s: %s", url, json)
        data = cls.__log_request(url, lambda: requests.post(url, json=json))
        return data.get('character')

    @classmethod
    def __get(cls, url):
        current_app.logger.debug("GET %s", url)
        data = cls.__log_request(url, lambda: requests.get(url))
        return data.get('character')

    @classmethod
    def __put(cls, url, values):
        current_app.logger.debug("PUT %s: %s", url, values)
        data = cls.__log_request(url, lambda: requests.put(url, values))
        return data.get('character')

    @classmethod
    def database(cls):
        #
        # World.load()
        #
        return World.instance.players

    @classmethod
    def get(cls, item_id):
        character = cls.__get("{}/character/{}".format(cls.__URL, item_id))
        return cls(**character) if character is not None else None

    @classmethod
    def find(cls, items=None, **kwargs):
        current_app.logger.debug(kwargs)
        yield from []

    @classmethod
    def find_by_name(cls, name=None):
        character = cls.__get("{}/character/find/{}".format(cls.__URL, name))
        return cls(character) if character is not None else None

    @property
    def is_created(self):
        return len(self.name) > 0

    @property
    def is_dead(self):
        return self.strength < 0

    @property
    def is_wizard(self):
        return self.level >= self.WIZARD_LEVEL

    @property
    def is_god(self):
        return self.level >= self.GOD_LEVEL

    @property
    def items(self):
        return Item.list_by_owner(self)

    @property
    def carry(self):
        return Item.find(owner=self)

    @property
    def can_carry(self):
        if self.is_wizard:
            return True
        if self.level < 0:
            return True
        return len([item for item in self.carry if not item.is_destroyed]) < self.level + 5

    @property
    def helper(self):
        return next((c for c in Character.all() if c.helping == self.character_id and c.room_id == self.room_id), None)

    @property
    def armor(self):
        armor = [Item.get(item_id) for item_id in (89, 113, 114)]
        if any(a for a in armor if a.worn_by(self)):
            return 10
        return 0

    @property
    def xp_value(self):
        if self.character_id < 16:
            return self.level * self.level * 100
        return 10 * damof(self)

    @property
    def serialize(self):
        return {
            'character_id': self.character_id,
            'name': self.name,
            'level': disl4(self.level, self.sex),
            'invisible': self.visible > 0,
            'absent': self.event_id == -2,
        }

    @property
    def serialized(self):
        return {
            'character_id': self.character_id,
            'name': self.name,
            'room_id': self.room_id,
            'message_id': self.event_id,
            'strength': self.strength,
            'visible': self.visible,
            'level': self.level,
            'weapon': self.weapon,
            'helping': self.helping,
            'sex': self.sex,
            # TODO: Remove It
            'is_aggressive': self.is_aggressive,
            'is_undead': self.is_undead,
        }

    @classmethod
    def list_characters(cls, player):
        for character in cls.find(
            not_player=player,
            channel_id=player.room_id,
            is_created=True,
            visible_for=player,
        ):
            result = character.serialize
            result.update({'items': list(character.items)})
            yield result

    @classmethod
    def add(cls, name):
        character = cls.__post("{}/character".format(cls.__URL), {'name': name})
        return character.get('character_id')

    def save(self):
        return self.__put("{}/character/{}".format(self.__URL, self.character_id), {'event_id': self.event_id})

    def check_move(self):
        pass

    def has_items(self, include_destroyed=False):
        if include_destroyed:
            return self.carry
        return (item for item in self.carry if not is_dest(item.item_id))

    def has_item(self, item_id, include_destroyed=False):
        return any(item for item in self.has_items(include_destroyed) if item.item_id == item_id)

    def check_fight(self, player, undead=True):
        if self.is_undead and not undead:
            return

        self.check_move()  # Maybe move it

        if not self.is_created:
            return
        if self.room_id != player.room_id:
            return
        if player.character.visible:
            return  # Im invisible
        if randperc() > 40:
            return

        yeti = Character.find_by_name("yeti")
        if yeti and self.character_id == yeti.character_id and ohany({13: True}):
            return

        mhitplayer(self, player.character_id)

    def set_dead(self):
        # MARK ALREADY DEAD
        self.strength = -1

    def hit_player(self, player, damage):
        player.strength -= damage
        self.on_hit_player(player, damage)

    # Events
    @property
    def on_hit_player(self):
        if self.character_id == 16:
            return wraith_hit
        return lambda player, damage: {}

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
            if character is None:
                return True
            if character.character_id == player.character_id:
                return True  # me
            if Globals.ail_blind:
                return False  # Cant see
            if player.room_id == character.room_id and player.is_dark:
                return False
            # if not player.can_see:
            #     return False  # Cant see
            if character.visible > player.character.level:
                return False

            player.set_pronoun(character)
            return True
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
        visible_for=None,
        not_player=None,
        name=None,
        room_id=None,
        wizard=None,
        exists_only=False,
        player_only=False,
        aggressive=False,
        **kwargs,
    ):
        if visible_for is not None:
            yield cls.__by_player_can_see(visible_for)
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
        if aggressive:
            yield lambda character: character.is_aggressive


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


def mhitplayer(*args):
    # raise NotImplementedError()
    print("mhitplayer({})".format(args))


def ohany(*args):
    # raise NotImplementedError()
    print("ohany({})".format(args))


def randperc(*args):
    # raise NotImplementedError()
    print("randperc({})".format(args))
    return 0
