from ..database import names
from ..exceptions import ActionError
from .model import Model
from .item import Item


def direction_2(player):
    wizard = any(iswornby(item, player.character_id) for item in (101, 102, 103))
    figure = fpbns("figure")
    if figure is not None\
            and figure.character_id != player.character_id \
            and figure.room_id == player.room_id \
            and not wizard:
        raise ActionError(
            "[p]The Figure[/p] holds you back\n"
            "[p]The Figure[/p] says 'Only true sorcerors may pass'\n",
        )
    return {}


class Exit(Model):
    database_name = names.EXITS

    DOOR_MIN = 1000
    DOOR_MAX = 2000
    # DIRECTIONS = [
    #     "North",
    #     "East ",
    #     "South",
    #     "West ",
    #     "Up   ",
    #     "Down ",
    # ]
    DIRECTIONS = "n", "e", "s", "w", "u", "d",

    def __init__(
        self,
        direction_id,
        room_from,
        room_to=None,
        door_id=None,
    ):
        super().__init__()
        self.direction_id = direction_id
        self.room_from = room_from
        if room_to and (self.DOOR_MIN <= room_to < self.DOOR_MAX):
            self.door_id = room_to - 1000
            self.__room_to = None
        else:
            self.door_id = door_id
            self.__room_to = room_to

    @property
    def available(self):
        return self.room_to < 0

    @property
    def direction(self):
        return self.DIRECTIONS[self.direction_id]

    @property
    def door(self):
        if self.door_id is None:
            return None
        return Item.get(self.door_id)

    @property
    def room_to(self):
        if self.door is None:
            return self.__room_to

        door_id = self.door_id ^ 1
        return Item.get(door_id).location  # other door side

    @property
    def on_exit(self):
        if self.door_id and state(self.door_id):
            return self.__on_door_closed
        if self.direction_id == 2:
            return direction_2
        return lambda player: {}

    def __on_door_closed(self, player):
        if self.door.name != "door" or player.is_dark or not self.door.description:
            raise ActionError("You can't go that way")  # Invisible doors
        else:
            raise ActionError("The door is not open")

    def go(self, player):

        room_id = self.room_to

        if room_id >= 0:
            raise ActionError("You can't go that way")

        self.on_exit(player)

        return room_id


# TODO: Implement


def fpbns(*args):
    # raise NotImplementedError()
    print("fpbns({})".format(args))
    return None


def iswornby(*args):
    # raise NotImplementedError()
    print("iswornby({})".format(args))
    return False


def state(*args):
    raise NotImplementedError()
