from .database import World, connect, disconnect
from .exceptions import crapup


class Globals:
    ail_blind = False
    my_lev = 0
    curch = 0
    curmode = 0
    globme = ""
    brmode = 0


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

    @property
    def text(self):
        if isdark():
            return "It is dark\n"
        title = self.title or ""
        return "{}\n{}".format(title, self.description)


def look_room(room_id=None, brief=None):
    if room_id is None:
        room_id = Globals.curch

    World.save()

    # 1
    error = "You are blind... you can't see a thing!\n" if Globals.ail_blind else None

    room = Room(room_id)

    if Globals.my_lev > 9:
        showname(room_id)

    if room.no_brief:
        brief = False
    elif brief is None:
        brief = Globals.brmode

    if room.death_room:
        Globals.ail_blind = False
        # 2
        if Globals.my_lev <= 9:
            loseme(Globals.globme)
            crapup("bye bye.....")

    # 3
    if isdark():
        text = "It is dark\n"
    elif Globals.ail_blind:
        text = None
    elif brief:
        text = room.title
    else:
        text = room.text

    World.load()

    if not isdark() and not Globals.ail_blind:
        lisobs()
        if Globals.curmode == 1:
            lispeople()

        # 4
        # text += "\n"
    onlook()
    return {
        'result': True,

        'error': error,
        'death': room.death_room and "<DEATH ROOM>\n",
        'text': text,
        '4': not isdark() and not Globals.ail_blind and "\n",
    }


def open_room(room_id, permissions):
    return Room(room_id, permissions)


def showname(*args):
    raise NotImplementedError()


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
