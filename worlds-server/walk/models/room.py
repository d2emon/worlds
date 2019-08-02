from ..database import names
from ..globalVars import Globals
from .model import Model
from .room_exit import Exit
from .zone import Zone


def room_139(player):
    if any(iswornby(item_id, player.player_id) for item_id in (113, 114, 89)):
        return {'message': "The shield protects you from the worst of the lava stream's heat\n"}
    return {'error': "The intense heat drives you back"}


class Room(Model):
    database_name = names.ROOMS

    DEFAULT_ZONE = Zone()
    ZONES = Zone.all()

    def __init__(
        self,
        room_id,
        title=None,
        exits=(),
        description=None,
        death_room=False,
        no_brief=False,
        is_dark=False,
        # permissions="r"
    ):
        super().__init__()

        self.__room_id = room_id
        self.title = title
        self.__exits = exits
        self.__description = description
        self.death_room = death_room
        self.no_brief = no_brief
        self.is_dark = is_dark

        self.__zone = None

    @property
    def description(self):
        if self.__description is None:
            return "You are on channel {}\n".format(self.room_id)
        return self.__description

    @property
    def exits(self):
        return [Exit(**data) for data in self.__exits if data is not None]

    @property
    def in_zone(self):
        if self.zone is None:
            return 0
        return self.zone.room_id(self.room_id)

    @property
    def name(self):
        if self.zone is None:
            return None
        zone, in_zone = self.zone.name, self.in_zone
        Globals.wd_there = "{} {}".format(zone, in_zone)
        return "{}{}".format(zone, in_zone)

    @property
    def room_id(self):
        return self.__room_id

    @property
    def zone(self):
        if self.__zone is None:
            self.__zone = Zone.by_room_id(self.room_id)
        return self.__zone

    @property
    def on_enter(self):
        if self.room_id == -139:
            return room_139
        return lambda player: {}

    def go_direction(self, player, direction_id):
        return self.get(self.exits[direction_id].go(player))


# Not Implemented


def iswornby(*args):
    # raise NotImplementedError()
    print("iswornby({})".format(args))
    return False
