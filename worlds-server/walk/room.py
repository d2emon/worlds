from .database import World, connect, disconnect, names
from .exceptions import crapup, ActionError
from .player import Player


def apply_events(events, key):
    event = events.get(key)
    return event() if event is not None else {}


class Globals:
    ail_blind = False
    my_lev = 10000
    curch = 0
    curmode = 0
    globme = ""
    wd_there = ""
    mynum = 0
    exittxt = {}
    in_ms = ""
    out_ms = ""
    in_fight = False


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
        self.exits = [0] * 7
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

    def on_enter(self):
        def room_139():
            if any(iswornby(item_id, Globals.mynum) for item_id in (113, 114, 89)):
                return {'message': "The shield protects you from the worst of the lava stream's heat\n"}
            return {'error': "The intense heat drives you back"}

        return apply_events(
            {
                -139: room_139,
            },
            self.room_id,
        )

    @classmethod
    def on_leave(cls, direction_id):
        def direction_2():
            figure = fpbns("figure")
            wizard = any(iswornby(item, Globals.mynum) for item in (101, 102, 103))
            if figure != -1 and figure != Globals.mynum and ploc(figure) == Player.room_id and not wizard:
                return {
                    'error': "[p]The Figure[/p] holds you back\n"
                             "[p]The Figure[/p] says 'Only true sorcerors may pass'\n",
                }
            return {}

        return apply_events(
            {
                2: direction_2,
            },
            direction_id,
        )


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


def go_direction(direction_id):
    def get_door(door_id):
        door_other = door_id ^ 1  # other door side
        if not state(door_id):
            return oloc(door_other)

        if oname(door_id) != "door" or isdark() or not olongt(door_id, state(door_id)):
            raise ActionError("You can't go that way")  # Invisible doors
        else:
            raise ActionError("The door is not open")

    if Globals.in_fight > 0:
        return {
            'error': "You can't just stroll out of a fight!\n"
                     "If you wish to leave a fight, you must FLEE in a direction\n",
        }
    if iscarrby(32, Globals.mynum) and ploc(25) == Player.room_id and len(pname(25)):
        return {'error': "[c]The Golem[/c] bars the doorway!\n"}
    if chkcrip():
        return {'error': True}

    direction_id -= 2
    room_id = Room(Player.room_id).exits[direction_id]
    if 999 < room_id < 2000:
        try:
            room_id = get_door(room_id - 1000)
        except ActionError as e:
            return {'error': e}
    if room_id >= 0:
        return {'error': "You can't go that way"}

    result = {}

    room = Room(Player.room_id)
    result.update(room.on_leave(direction_id))

    room = Room(room_id)
    result.update(room.on_enter())

    sendsys(
        Globals.globme,
        Globals.globme,
        -10000,
        Player.room_id,
        "[s name=\"{}\"]{} has gone {} {}.\n[/s]".format(
            pname(Globals.mynum),
            Globals.globme,
            Globals.exittxt.get(direction_id),
            Globals.out_ms,
        ),
    )

    Player.room_id = room.room_id

    sendsys(
        Globals.globme,
        Globals.globme,
        -10000,
        Player.room_id,
        "[s name=\"{}\"]{} {}\n[/s]".format(
            Globals.globme,
            Globals.globme,
            Globals.in_ms,
        ),
    )

    trapch(Player.room_id)
    result.update({
        'room_id': room_id,
        'room': look_room(room_id),
    })
    return result


def find_zone(room_id):
    room = Room(room_id)
    return room.zone, room.in_zone


def open_room(room_id, permissions):
    return Room(room_id, permissions)


def show_name(room_id):
    return Room(room_id).show_name()


def chkcrip(*args):
    # raise NotImplementedError()
    print("chkcrip({})".format(args))
    return False


def fpbns(*args):
    # raise NotImplementedError()
    print("fpbns({})".format(args))
    return -1


def is_dark(*args):
    def dark():
        for c in range(Globals.numobs):
            if c != 32 and not otstbit(c, 13):
                continue
            if ishere(c):
                return False
            if ocarrf(c) == 0 or ocarrf(c) == 3:
                continue
            if ploc(olo(c)) != Player.room_id:
                continue
            return False
        return True

    if Globals.my_lev > 9:
        return False
    if Player.room_id in (-1100, -1101):
        return False
    if -1123 <= Player.room_id <= -1113:
        return dark()
    if Player.room_id < -399 or Player.room_id > -300:
        return False
    return dark()


def iscarrby(*args):
    # raise NotImplementedError()
    print("iscarrby({})".format(args))
    return False


def iswornby(*args):
    # raise NotImplementedError()
    print("iswornby({})".format(args))
    return False


def lisobs(*args):
    # raise NotImplementedError()
    print("lisobs({})".format(args))


def lispeople(*args):
    # raise NotImplementedError()
    print("lispeople({})".format(args))


def loseme(*args):
    raise NotImplementedError()


def oloc(*args):
    raise NotImplementedError()


def olongt(*args):
    raise NotImplementedError()


def oname(*args):
    raise NotImplementedError()


def onlook(*args):
    # raise NotImplementedError()
    print("onlook({})".format(args))


def ploc(*args):
    raise NotImplementedError()


def pname(*args):
    # raise NotImplementedError()
    print("pname({})".format(args))
    return ''


def sendsys(*args):
    # raise NotImplementedError()
    print("sendsys({})".format(args))


def state(*args):
    raise NotImplementedError()


def trapch(*args):
    # raise NotImplementedError()
    print("trapch({})".format(args))
