from .database import connect, disconnect, names
from .exceptions import ActionError
from .globalVars import Globals


def apply_events(events, key):
    event = events.get(key)
    return event() if event is not None else {}


class Exit:
    DOOR_MIN = 1000
    DOOR_MAX = 2000

    def __init__(
        self,
        direction=None,
        from_room=None,
        to_room=None
    ):
        self.direction = direction
        self.from_room = from_room
        self.room_to = to_room

    def go(self, player):
        if self.DOOR_MIN <= self.room_to < self.DOOR_MAX:
            room_id = self.__go_door(player)
        else:
            room_id = self.room_to

        if room_id >= 0:
            raise ActionError("You can't go that way")

        self.on_exit(player)

        return room_id

    def __go_door(self, player):
        if not state(self.room_to):
            door_id = self.room_to ^ 1  # other door side
            return oloc(door_id)
        elif oname(self.room_to) != "door" or player.is_dark or not olongt(self.room_to, state(self.room_to)):
            raise ActionError("You can't go that way")  # Invisible doors
        else:
            raise ActionError("The door is not open")

    def on_exit(self, player):
        def direction_2():
            figure = fpbns("figure")
            wizard = any(iswornby(item, player.player.id) for item in (101, 102, 103))
            if figure != -1 and figure != player.player.id and ploc(figure) == self.from_room and not wizard:
                raise ActionError(
                    "[p]The Figure[/p] holds you back\n"
                    "[p]The Figure[/p] says 'Only true sorcerors may pass'\n",
                )
            return {}

        return apply_events(
            {
                2: direction_2,
            },
            self.direction,
        )


class Zone:
    database = names.ZONES

    def __init__(self, name="TCHAN", begin=None, end=0):
        self.name = name
        self.begin = begin
        self.end = end + 1

    @classmethod
    def zones(cls):
        return [cls(**data) for data in connect(cls.database).all()]

    @classmethod
    def by_room_id(cls, room_id):
        if room_id > 0:
            return None
        return next((zone for zone in cls.zones() if zone.begin <= -room_id < zone.end), None)

    def room_id(self, room_id):
        return 0 if self.begin is None else (-room_id) - self.begin


class Room:
    database = names.ROOMS

    DEFAULT_ZONE = Zone()
    ZONES = Zone.zones()

    def __init__(self, room_id, permissions="r"):
        self.room_id = room_id
        self.title = None
        self.__exits = [0] * 7
        self.description = "You are on channel {}\n".format(self.room_id)
        self.death_room = False
        self.no_brief = False

        self.__data = None

        self.open(permissions).load()

    @property
    def exits(self):
        return [Exit(
            direction=direction_id,
            from_room=self.room_id,
            to_room=room_id,
        ) for direction_id, room_id in enumerate(self.__exits)]

    def open(self, permissions):
        self.__data = connect(self.database, permissions).get(-self.room_id)
        return self

    def close(self):
        self.__data = disconnect(self.database)

    def load(self):
        if self.__data is None:
            return

        self.title = self.__data.get('title')
        self.__exits = self.__data.get('exits')
        self.description = self.__data.get('description')
        self.death_room = self.__data.get('death_room')
        self.no_brief = self.__data.get('no_brief')

        self.close()

    @property
    def zone(self):
        return Zone.by_room_id(self.room_id) or self.DEFAULT_ZONE

    @property
    def in_zone(self):
        return self.zone.room_id(self.room_id)

    @property
    def is_dark(self):
        if self.room_id in (-1100, -1101):
            return False
        if -1123 <= self.room_id <= -1113:
            return True
        if self.room_id < -399 or self.room_id > -300:
            return False
        return True

    def show_name(self):
        zone, in_zone = self.zone.name, self.in_zone
        Globals.wd_there = "{} {}".format(zone, in_zone)
        return "{}{}".format(zone, in_zone)

    def on_enter(self, player):
        def room_139():
            if any(iswornby(item_id, player.player_id) for item_id in (113, 114, 89)):
                return {'message': "The shield protects you from the worst of the lava stream's heat\n"}
            return {'error': "The intense heat drives you back"}

        return apply_events(
            {
                -139: room_139,
            },
            self.room_id,
        )

    def go_direction(self, player, direction_id):
        return Room(self.exits[direction_id].go(player))


def find_zone(room_id):
    room = Room(room_id)
    return room.zone, room.in_zone


def open_room(room_id, permissions):
    return Room(room_id, permissions)


def show_name(room_id):
    return Room(room_id).show_name()


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
