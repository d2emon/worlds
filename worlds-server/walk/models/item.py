import random
from ..database import World
from ..exceptions import ActionError
from ..globalVars import Globals
from .model import Model


def attack_rune(player, victim):
    item_16 = Item.get(16)
    if victim is not None and victim.has_item(item_16):
        raise ActionError("The runesword flashes back away from its target, growling in anger!")
    return {}


def drop_rune(player):
    if not player.is_wizard:
        raise ActionError("You can't let go of it!")
    return {}


def take_rune(item):
    def f(player):
        if item.state != 1:
            return {}
        if player.character.helper is not None:
            return {}
        raise ActionError("Its too well embedded to shift alone.\n")
    return f


def take_treasure(player):
    door = Item.get(20)
    door.state = 1
    return {'message': "The door clicks shut....\n"}


def rune(player):
    if player.in_fight:
        return {}

    character = player.find_character(
        items=player.available_characters,
        # wizard=True,
        player_only=True,
    )
    if character is None:
        return {}
    if randperc() < 9 * player.level:
        return {}
    if player.find_character(name=character.name) is None:
        return {}

    messages = ["The runesword twists in your hands lashing out savagely"]
    result = player.hit_player(character, Item.get(32))
    messages.append(result.get('message', ''))
    result.update({
        'message': None,
        'messages': messages,
    })
    return result


class Item(Model):
    def __init__(
        self,
        item_id,
        name='',
        slug='',
        description=(),
        max_state=0,
        flannel=False,
        base_value=0,
        location=0,
        carry_flag=0,
        state=0,
        # Flags
        is_destroyed=False,
        has_connected=False,
        change_on_take=False,
        is_light=False,
        is_weapon=False,
    ):
        super().__init__()
        self.item_id = item_id

        self.__name = name
        self.__slug = slug
        self.__description = description
        self.__max_state = max_state
        self.__flannel = flannel
        self.__base_value = base_value

        self.__location = location
        self.__carry_flag = carry_flag
        self.__state = state

        # Flags
        self.is_destroyed = is_destroyed
        self.__has_connected = has_connected
        self.__change_on_take = change_on_take
        self.is_light = is_light
        self.is_weapon = is_weapon

    @classmethod
    def database(cls):
        #
        World.load()
        #
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
    def slug(self):
        return self.__slug

    @property
    def state(self):
        # return self.__state
        return random.randrange(self.__max_state + 1)

    @state.setter
    def state(self, value):
        self.__state = min(value, self.__max_state)
        connected = self.connected
        if self.__has_connected and connected is not None:
            connected.state = value

    @property
    def value(self):
        return (tscale() * self.__base_value) / 5

    @property
    def connected(self):
        return self.get(self.item_id ^ 1)

    @property
    def location(self):
        return self.__location

    @property
    def contained_in(self):
        if self.__carry_flag != 3:
            return None
        return self.location

    @property
    def room_id(self):
        if self.__carry_flag != 0:
            return None
        return self.location

    @property
    def owner(self):
        if self.__carry_flag not in (1, 2):
            return None
        return self.location or None

    @property
    def __serialized(self):
        return {
            'item_id': self.item_id,
            'slug': self.slug,
            'name': self.name,
            'worn': False,  # item.worn_by and carrier and item.worn_by.character_id == carrier.charater_id
            'is_destroyed': self.is_destroyed,
        }

    @property
    def serialized(self):
        return {
            'item_id': self.item_id,
            'name': self.__name,
            'slug': self.__slug,
            'description': self.__description,
            'max_state': self.__max_state,
            'flannel': self.__flannel,
            'base_value': self.__base_value,
            'location': self.__location,
            'carry_flag': self.__carry_flag,
            'state': self.state,
            # TODO: Remove It
            'is_destroyed': self.is_destroyed,
            'has_connected': self.__has_connected,
            'change_on_take': self.__change_on_take,
            'is_light': self.is_light,
            'is_weapon': self.is_weapon,
        }

    @classmethod
    def list_by_owner(cls, owner):
        """
        Carried Loc!
        :return:
        """
        for item in owner.carry:
            yield item.__serialized

    @classmethod
    def list_by_container(cls, container):
        """
        Carried Loc!
        :return:
        """
        for item in cls.find(container=container):
            yield item.__serialized

    @classmethod
    def list_by_flannel(cls, items, flannel):
        for item in cls.find(
            items=items,
            flannel=flannel,
        ):
            # OLONGT NOTE TO BE ADDED
            Globals.wd_it = item.name
            yield item

    def save(self):
        self.database().set(self.item_id, **self.serialized)

    def create(self):
        self.is_destroyed = False
        self.save()

    def set_location(self, location, carry_flag):
        self.__location = location
        self.__carry_flag = carry_flag
        self.save()

    # Events
    @property
    def on_attack(self):
        if self.item_id == 32:
            return attack_rune
        return lambda player, victim: {}

    @property
    def on_break(self):
        if self.item_id == 171:
            return sys_reset
        return lambda player: {'error': "You can't do that"}

    @property
    def on_drop(self):
        if self.item_id == 32:
            return drop_rune
        return lambda player: {}

    @property
    def on_before_take(self):
        if self.item_id == 32:
            return take_rune(self)
        return lambda player: {}

    def on_after_take(self, player):
        if self.__change_on_take:
            self.state = 0

        if self.room_id == -1081:
            return take_treasure(player)
        return {}

    @property
    def on_wait(self):
        if self.item_id == 32:
            return rune
        return lambda player: {}

    # Search
    @classmethod
    def __by_description(cls):
        return lambda item: len(item.description) > 0

    @classmethod
    def __by_destroyed(cls, destroyed=True):
        # if((my_lev<10)&&(isdest(item)))return(0);
        return lambda item: item.is_destroyed == destroyed

    @classmethod
    def __by_flannel(cls, flannel):
        return lambda item: item.flannel == flannel

    @classmethod
    def __by_max_state(cls, max_state):
        return lambda item: item.state <= max_state

    @classmethod
    def __by_slug(cls, slug):
        # if name.lower() == "red":
        #     next(word)
        #     return 4
        # if name.lower() == "blue":
        #     next(word)
        #    return 5
        # if name.lower() == "green":
        #     next(word)
        #     return 6

        def f(item):
            if item.slug.lower() != slug.lower():
                return False
            Globals.wd_it = slug
            return True
        return f

    # 1
    @classmethod
    def __by_available(cls, character):
        # Patch for shields
        # if item.item_id == 112 and player.carry(113):
        #     return 113
        # if item.item_id == 112 and player.carry(114):
        #     return 114
        return lambda item: cls.__by_room_id(character.room_id) or item.owner == character.character_id

    # 2-3
    @classmethod
    def __by_owner(cls, character):
        return lambda item: character and item.owner == character.character_id

    # 4
    @classmethod
    def __by_room_id(cls, room_id):
        return lambda item: item.room_id == room_id

    # 5
    @classmethod
    def __by_container(cls, container):
        return lambda item: container and item.contained_in == container.item_id

    @classmethod
    def filters(
        cls,
        wizard=True,
        description=None,
        flannel=None,
        max_state=None,

        slug=None,
        available_for=None,  # fobna
        container=None,  # fobnin
        owner=None,  # fobnc
        room_id=None,  # fobnh
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

        if available_for is not None:
            yield cls.__by_available(available_for)
        if container is not None:
            yield cls.__by_container(container)
        if owner is not None:
            yield cls.__by_owner(owner)
        if room_id is not None:
            yield cls.__by_room_id(room_id)
        if slug is not None:
            yield cls.__by_slug(slug)


def by_flannel(flannel):
    return Item.list_by_flannel(Item.all(), flannel)


def list_items(player):
    return Item.list_items(player)


# TODO: Implement


def randperc(*args):
    # raise NotImplementedError()
    print("randperc({})".format(args))
    return 0


def sys_reset(*args):
    # raise NotImplementedError()
    print("sys_reset({})".format(args))


def tscale(*args):
    # raise NotImplementedError()
    print("tscale({})".format(args))
    return 1
