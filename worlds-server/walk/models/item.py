import random
from ..database import World
from ..globalVars import Globals
from .model import Model


def rune(player):
    if Globals.in_fight:
        return {}

    character = next(player.character.find(
        items=player.available_characters,
        wizard=True,
        player_only=True,
    ), None)
    if character is None:
        return {}
    if randperc() < 9 * player.level:
        return {}
    if fpbns(character.name) is None:
        return {}
    hitplayer(character.character_id, 32)
    return {'message': "The runesword twists in your hands lashing out savagely\n"}


class Item(Model):
    def __init__(
        self,
        item_id,
        name='',
        description=(),
        max_state=0,
        flannel=False,
        base_value=0,
        location=0,
        carry_flag=0,
        state=0,
    ):
        super().__init__()
        self.item_id = item_id

        self.__name = name
        self.__description = description
        self.__max_state = max_state
        self.__flannel = flannel
        self.__base_value = base_value

        self.__location = location
        self.__carry_flag = carry_flag
        self.__state = state

    @classmethod
    def database(cls):
        return World.instance.items

    @classmethod
    def count(cls):
        return cls.database().ITEMS

    @property
    def description(self):
        return self.__description[self.state]

    @property
    def flannel(self):
        return self.__flannel

    @property
    def name(self):
        return self.__name

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = min(value, self.__max_state)
        connected = self.connected()
        if otstbit(self, 1) and connected is not None:
            connected.state = value

    @property
    def connected(self):
        return self.get(self.item_id ^ 1)

    @classmethod
    def list_by_flannel(cls, items, flannel):
        for item in cls.find(
            items=items,
            flannel=flannel,
        ):
            # OLONGT NOTE TO BE ADDED
            Globals.wd_it = item.name
            yield item

    @classmethod
    def list_items(cls, player):
        items = list(cls.find(
            wizard=player.is_wizard,
            room_id=player.room_id,
            max_state=3,
            description=True,
        ))

        yield from cls.list_by_flannel(items, True)
        yield showwthr()
        yield from cls.list_by_flannel(items, False)

    @property
    def location(self):
        return self.__location

    @property
    def carried_by(self):
        if self.__carry_flag not in (1, 2):
            return None
        return self.location

    @property
    def room_id(self):
        if self.__carry_flag != 1:
            return None
        return self.location

    @property
    def owner(self):
        if self.__carry_flag not in (0, 3):
            return None
        return self.location

    @property
    def serialized(self):
        return {
            'item_id': self.item_id,
            'text': self.description,
            'destroyed': isdest(self.item_id),
        }

    def set_location(self, location, carry_flag):
        self.__location = location
        self.__carry_flag = carry_flag

    # Search
    @classmethod
    def __by_description(cls):
        return lambda item: len(item.description) > 0

    @classmethod
    def __by_destroyed(cls, destroyed=True):
        def f(i):
            # if((my_lev<10)&&(isdest(item)))return(0);
            return isdest(i)

        return f

    @classmethod
    def __by_flannel(cls, flannel):
        return lambda item: item.flannel == flannel

    @classmethod
    def __by_max_state(cls, max_state):
        return lambda item: item.state <= max_state

    @classmethod
    def __by_room_id(cls, room_id):
        return lambda item: item.room_id == room_id

    @classmethod
    def filters(
        cls,
        wizard=True,
        description=None,
        flannel=None,
        max_state=None,
        room_id=None,
        **kwargs,
    ):
        if not wizard:
            yield cls.__by_destroyed(False)
        if description is not None:
            yield cls.__by_description()
        if flannel is not None:
            yield cls.__by_flannel(flannel)
        if max_state is not None:
            yield cls.__by_max_state(max_state)
        if room_id is not None:
            yield cls.__by_room_id(room_id)

    # Events

    @property
    def on_wait(self):
        if self.item_id == 32:
            return rune
        return lambda player: {}


def by_flannel(flannel):
    return Item.list_by_flannel(Item.all(), flannel)


def list_items(player):
    return Item.list_items(player)


# TODO: Implement


def fpbns(*args):
    # raise NotImplementedError()
    print("fpbns({})".format(args))
    return None


def hitplayer(*args):
    # raise NotImplementedError()
    print("hitplayer({})".format(args))


def isdest(*args):
    # raise NotImplementedError()
    print("isdest({})".format(args))
    return random.randrange(100) > 50


def ishere(*args):
    # raise NotImplementedError()
    print("ishere({})".format(args))
    return True


def otstbit(*args):
    # raise NotImplementedError()
    print("otstbit({})".format(args))
    return False


def randperc(*args):
    # raise NotImplementedError()
    print("randperc({})".format(args))
    return 0


def showwthr(*args):
    # raise NotImplementedError()
    print("showwthr({})".format(args))
    return None
