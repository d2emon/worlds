class Globals:
    ail_blind = False
    my_lev = 0
    curch = 0
    curmode = 0
    globme = ""
    brmode = 0


class Room:
    ROOMS = "ROOMS"

    def __init__(self, room_id, permissions="r"):
        self.room_id = room_id
        self.title = None
        self.description = "You are on channel {}\n".format(self.room_id)
        self.death_room = False
        self.no_brief = False

        self.__permissions = None
        self.__data = None

        self.open(permissions)

    @property
    def __filename(self):
        return "{}{}".format(self.ROOMS, -self.room_id)

    def open(self, permissions):
        print("fopen({}, {})".format(self.__filename, permissions))
        self.__permissions = permissions
        # self.__data = []
        self.__data = None
        return self

    def close(self):
        self.__permissions = None
        self.__data = None

    def load(self):
        if self.__data is None:
            return

        lodex(self.__data)
        for s in self.__data:
            self.__parse(s)
        self.close()

    def __parse(self, s):
        if s == "#DIE":
            self.death_room = True
            return
        if s == "#NOBR":
            self.no_brief = True
            return
        if self.title is None:
            self.title = s
            return
        self.description += "{}\n".format(s)

    @property
    def text(self):
        if isdark():
            return "It is dark\n"
        title = self.title or ""
        return "{}\n{}".format(title, self.description)


def look_room(room_id=None, brief=None):
    if room_id is None:
        room_id = Globals.curch

    closeworld()

    # 1
    error = "You are blind... you can't see a thing!\n" if Globals.ail_blind else None

    room = Room(room_id)
    room.load()

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

    openworld()

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


def closeworld():
    # raise NotImplementedError()
    print("closeworld()")


def crapup(*args):
    raise NotImplementedError()


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


def lodex(*args):
    # raise NotImplementedError()
    print("lodex({})".format(args))


def loseme(*args):
    raise NotImplementedError()


def onlook(*args):
    # raise NotImplementedError()
    print("onlook({})".format(args))


def openworld(*args):
    # raise NotImplementedError()
    print("openworld()")
