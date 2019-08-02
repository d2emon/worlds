from ..database import names
from ..exceptions import ActionError
from .model import Model


def direction_2(player):
    figure = fpbns("figure")
    wizard = any(iswornby(item, player.player_id) for item in (101, 102, 103))
    if figure != -1 and figure != player.player_id and ploc(figure) == player.room_id and not wizard:
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
            self.door_id = room_to
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
    def room_to(self):
        if self.door_id is None:
            return self.__room_to

        door_id = self.door_id ^ 1
        return oloc(door_id)  # other door side

    @property
    def on_exit(self):
        if self.door_id and state(self.door_id):
            return self.__on_door_closed
        if self.direction_id == 2:
            return direction_2
        return lambda player: {}

    def __on_door_closed(self, player):
        if oname(self.door_id) != "door" or player.is_dark or not olongt(self.door_id, state(self.door_id)):
            raise ActionError("You can't go that way")  # Invisible doors
        else:
            raise ActionError("The door is not open")

    def go(self, player):

        room_id = self.room_to

        if room_id >= 0:
            raise ActionError("You can't go that way")

        self.on_exit(player)

        return room_id


# Not Implemented


def fpbns(*args):
    # raise NotImplementedError()
    print("fpbns({})".format(args))
    return -1


def iswornby(*args):
    # raise NotImplementedError()
    print("iswornby({})".format(args))
    return False


def oloc(*args):
    raise NotImplementedError()


def olongt(*args):
    raise NotImplementedError()


def oname(*args):
    raise NotImplementedError()


def ploc(*args):
    raise NotImplementedError()


def state(*args):
    raise NotImplementedError()
