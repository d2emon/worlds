from ..database import names
from ..exceptions import ActionError
from .model import Model
from .item import Item
from .character import Character


def direction_2(player):
    wizard = any(iswornby(item, player.character_id) for item in (101, 102, 103))
    if wizard:
        return None
    figure = next(Character.find(name="figure"))
    if figure is None:
        return None
    if figure.character_id == player.character_id:
        return None
    if figure.room_id == player.room_id:
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
        room_to=0,
        door_id=None,
    ):
        super().__init__()
        self.direction_id = direction_id
        self.room_from = room_from
        if room_to and (self.DOOR_MIN <= room_to < self.DOOR_MAX):
            self.door_id = room_to - 1000
            self.room_to = 0
        else:
            self.door_id = door_id
            self.room_to = room_to

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
        print(self.door_id, Item.get(self.door_id).name, Item.get(self.door_id).connected.name)
        return Item.get(self.door_id)

    @property
    def on_exit(self):
        if self.door_id and state(self.door_id):
            return self.__on_door_closed
        if self.direction_id == 2:
            return direction_2
        return lambda player: None

    def __on_door_closed(self, player):
        if self.door.name != "door" or player.is_dark or not self.door.description:
            raise ActionError("You can't go that way")  # Invisible doors
        else:
            raise ActionError("The door is not open")

    def go(self, player):
        room_id = self.room_to if self.door is None else self.door.connected.location  # other door side

        print(room_id)

        if room_id >= 0:
            raise ActionError("You can't go that way")

        self.on_exit(player)

        return room_id


# TODO: Implement


def iswornby(*args):
    # raise NotImplementedError()
    print("iswornby({})".format(args))
    return False


def state(*args):
    # raise NotImplementedError()
    print("state({})".format(args))
    return 0
