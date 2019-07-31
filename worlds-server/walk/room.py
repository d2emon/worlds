from .database import World, connect, disconnect, names
from .exceptions import crapup
from .player import Player


class Globals:
    ail_blind = False
    my_lev = 10000
    curmode = 0
    globme = ""
    wd_there = ""


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
        self.exits = [None] * 7
        self.description = "You are on channel {}\n".format(self.room_id)
        self.death_room = False
        self.no_brief = False

        self.__data = None

        self.open(permissions).load()

    def open(self, permissions):
        self.__data = connect(self.database, permissions).get(-self.room_id)
        return self

    def close(self):
        self.__data = disconnect(self.database)

    def load(self):
        if self.__data is None:
            return

        self.title = self.__data.get('title')
        self.exits = self.__data.get('exits')
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

    def show_name(self):
        zone, in_zone = self.zone.name, self.in_zone
        Globals.wd_there = "{} {}".format(zone, in_zone)
        if Globals.my_lev > 9999:
            return "{}{}[ {} ]".format(zone, in_zone, self.room_id)
        return "{}{}".format(zone, in_zone)


def look_room(room_id=None):
    if room_id is None:
        room_id = Player.room_id

    World.save()

    room = Room(room_id)

    if room.death_room:
        Globals.ail_blind = False
        if Globals.my_lev <= 9:
            loseme(Globals.globme)
            crapup("bye bye.....")

    if isdark():
        text = "It is dark\n"
    elif Globals.ail_blind:
        text = None
    else:
        text = room.description

    World.load()

    if not isdark() and not Globals.ail_blind:
        lisobs()
        if Globals.curmode == 1:
            lispeople()

        # 5
    onlook()
    return {
        'result': True,
        'room_id': room.room_id,
        'no_brief': room.no_brief,

        'error': "You are blind... you can't see a thing!" if Globals.ail_blind else None,
        'name': room.show_name() if Globals.my_lev > 9 else None,
        'death': room.death_room and "<DEATH ROOM>\n",
        'title': room.title if not isdark() else None,
        'text': text,
        '5': not isdark() and not Globals.ail_blind and "\n",

        # Secret
        'zone': room.zone.name,
        'in_zone': room.in_zone,
    }


def find_zone(room_id):
    room = Room(room_id)
    return room.zone, room.in_zone


def open_room(room_id, permissions):
    return Room(room_id, permissions)


def show_name(room_id):
    return Room(room_id).show_name()


def isdark(*args):
    # raise NotImplementedError()
    print("isdark({})".format(args))
    return False


def lisobs(*args):
    # raise NotImplementedError()
    print("lisobs({})".format(args))


def lispeople(*args):
    # raise NotImplementedError()
    print("lispeople({})".format(args))


def loseme(*args):
    raise NotImplementedError()


def onlook(*args):
    # raise NotImplementedError()
    print("onlook({})".format(args))
