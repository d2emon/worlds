from flask import current_app
import uuid


class Character:
    MAX_USER = 16

    def __init__(
        self,
        character_id,
        name="",
        channel_id=0,
        event_id=-1,
        level=1,
        visible=0,
        strength=-1,
        weapon=-1,
        sex=0,

        is_player=False,
    ):
        self.character_id = character_id
        self.name = name
        self.channel_id = channel_id
        self.event_id = event_id
        self.level = level
        self.visible = visible
        self.strength = strength
        self.weapon = weapon
        self.sex = sex

        self.is_player = is_player

    @property
    def __item(self):
        return next((item for item in DATA if item.get('character_id') == self.character_id), None)

    @property
    def is_created(self):
        return len(self.name) > 0

    def save(self):
        self.__item.update(self.serialize())

    def reset(self, name):
        if name is None:
            raise AssertionError("Can't start unnamed player")

        self.name = name
        self.channel_id = 0
        self.event_id = -1
        self.level = 1
        self.visible = 0
        self.strength = -1
        self.weapon = -1
        self.sex = 0

        self.save()

    def serialize(self):
        return {
            'character_id': self.character_id,
            'name': self.name,
            'channel_id': self.channel_id,
            'event_id': self.event_id,
            'level': self.level,
            'visible': self.visible,
            'strength': self.strength,
            'weapon': self.weapon,
            'sex': self.sex,
        }

    @classmethod
    def all(cls):
        return (cls(**item) for item in DATA)

    @classmethod
    def players(cls):
        return (player for player in cls.all() if player.is_player)

    @classmethod
    def get(cls, character_id):
        return (character for character in cls.all() if character.character_id == character_id)

    @classmethod
    def find(cls, name):
        return (character for character in cls.all() if character.name == name)

    @classmethod
    def start(cls, name):
        # if next(cls.find(name), None):
        #     raise AssertionError("You are already on the system - you may only be on once at a time")

        #
        character = next(cls.find(name), None)
        if character is not None:
            character.reset(name)
            return character
        #

        character = next((character for character in cls.players() if not character.is_created), None)
        if character is None:
            raise OverflowError("Sorry AberMUD is full at the moment")

        character.reset(name)
        return character


DATA = [{
    'character_id': str(uuid.uuid4()),
    'is_player': character_id < Character.MAX_USER,
} for character_id in range(Character.MAX_USER)]
