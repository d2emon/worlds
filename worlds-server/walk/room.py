from .database import World, connect, disconnect
from .exceptions import crapup
from .player import Player


class Globals:
    ail_blind = False
    my_lev = 0
    curmode = 0
    globme = ""


class Zone:
    def __init__(self, name, first, last):
        self.name = name
        self.first = first
        self.last = last


__ZONES = {
    1: "LIMBO",
    2: "WSTORE",
    4: "HOME",
    5: "START",
    6: "PIT",
    19: "WIZROOM",
    99: "DEAD",
    299: "BLIZZARD",
    399: "CAVE",
    499: "LABRNTH",
    599: "FOREST",
    699: "VALLEY",
    799: "MOOR",
    899: "ISLAND",
    999: "SEA",
    1049: "RIVER",
    1069: "CASTLE",
    1099: "TOWER",
    1101: "HUT",
    1105: "TREEHOUSE",
    2199: "QUARRY",
    2299: "LEDGE",
    2499: "INTREE",
    99999: "WASTE",
}
__names = list(__ZONES.keys())
__names.sort()
ZONES = [Zone(__names[zone_id, ]) for zone_id in __names]

ZONES = [
    Zone('LIMBO', 0, 1),
]


class Room:
    database = "ROOMS"

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
        self.__data = connect(self.database, permissions, item_id=self.room_id)
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

    def show_name(self):
        a, b = findzone(self.room_id)
        text = "{}{}".format(a, b)
        if Globals.my_lev > 9999:
            text += "[ {} ]".format(self.room_id)
        Globals.wd_there = "{} {}".format(a, b)
        text += "\n"
        return text


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
    }


def find_zone(room_id):
    first = 0
    last = 0
    zone = "TCHAN"
    zone_id = 0

    room_id = -room_id
    if room_id <= 0:
        return "TCHAN", 0

    while last < room_id:
        first, last, zone = last, zoname[zone_id].loc, zoname[zone_id].name
        zone_id += 1

    return zone, (room_id - first)


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
