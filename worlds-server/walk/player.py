import random
from .exceptions import ActionError, DatabaseError, StopGame
from .database import World
from .globalVars import Globals
from .models.character import Character
from .models.item import Item
from .models.room import Room


class Player:
    __PLAYER = None

    MAX_PLAYER = 16

    WIZARD_LEVEL = 10
    GOD_LEVEL = 10000

    def __init__(self, name):
        self.character_id = 0  # mynum
        self.name = "The {}".format(name) if name == "Phantom" else name  # globme

        self.level = 10000  # my_lev
        self.__room_id = random.choice((
            -5,
            -183,
        ))  # curch

        self.__room = None

        Globals.tty = 0
        # if tty == 4:
        #     initbbc()
        #     initscr()
        #     topscr()

        # Talker
        makebfr()
        Globals.cms = -1
        putmeon(self.name)

        try:
            World.load()
        except DatabaseError:
            raise StopGame("Sorry AberMUD is currently unavailable")
        if self.character_id >= self.MAX_PLAYER:
            raise StopGame("\nSorry AberMUD is full at the moment\n")
        rte(self.name)
        World.save()

        Globals.cms = -1
        special(".g", self.name)
        Globals.i_setup = True

        self.__PLAYER = self

    @property
    def character(self):
        return Character.get(self.character_id)

    @property
    def is_dark(self):
        def is_light(item_id):
            if item_id != 32 and not otstbit(item_id, 13):
                return False
            if ishere(item_id):
                return True
            if ocarrf(item_id) == 0 or ocarrf(item_id) == 3:
                return False
            if Character.get(oloc(item_id)).room_id != self.room_id:
                return False
            return True

        if self.is_wizard:
            return False
        if not self.room.is_dark:
            return False
        if any(is_light(item_id) for item_id in range(Item.count())):
            return False

    @property
    def is_god(self):
        return self.level >= self.GOD_LEVEL

    @property
    def is_wizard(self):
        return self.level >= self.WIZARD_LEVEL

    @property
    def room(self):
        if self.__room is None:
            self.__room = Room.get(self.room_id)
        return self.__room

    @property
    def room_id(self):
        return self.__room_id

    @room_id.setter
    def room_id(self, value):
        self.__room = None
        self.__room_id = value

    @classmethod
    def player(cls, name="Name"):
        if cls.__PLAYER is None:
            cls.__PLAYER = cls(name)
        return cls.__PLAYER

    @classmethod
    def start(cls, name):
        cls.__PLAYER = cls(name)
        return {
            'player': {
                'name': cls.__PLAYER.name,
            },
            'message': "Hello {}".format(cls.__PLAYER.name),
        }

    def set_room(self, room_id=None):
        if room_id is None:
            room_id = self.room_id

        World.load()

        self.character.room_id = room_id
        return self.look()

    def check_help(self):
        def remove_helping(name=''):
            self.character.helping = None
            return {'message': "You can no longer help [c]{}[/c]\n".format(name)}

        helping = Character.get(self.character.helping)
        if not Globals.i_setup:
            return
        elif helping is None or not helping.is_created:
            return remove_helping()
        elif helping.room_id != self.room_id:
            return remove_helping(helping.name)

    def go(self, direction_id):
        if Globals.in_fight > 0:
            raise ActionError(
                "You can't just stroll out of a fight!\n"
                "If you wish to leave a fight, you must FLEE in a direction\n"
            )
        golem = Character.get(25)
        if iscarrby(32, self.character_id) and golem and golem.is_created and golem.room_id == self.room_id:
            raise ActionError("[c]The Golem[/c] bars the doorway!\n")
        if chkcrip():
            raise ActionError("ERROR")

        room = self.room.go_direction(self, direction_id)

        result = room.on_enter(self)
        if result.get('error'):
            return result

        sendsys(
            self.name,
            self.name,
            -10000,
            self.room_id,
            "[s name=\"{}\"]{} has gone {} {}.\n[/s]".format(
                self.character.name,
                self.name,
                Globals.exittxt.get(direction_id),
                Globals.out_ms,
            ),
        )

        sendsys(
            self.name,
            self.name,
            -10000,
            room.room_id,
            "[s name=\"{}\"]{} {}\n[/s]".format(
                self.name,
                self.name,
                Globals.in_ms,
            ),
        )

        self.room_id = room.room_id
        result.update({
            'result': not result.get('error'),
            'room': self.set_room(),
        })
        return result

    def quit_game(self):
        if Globals.is_forced:
            raise ActionError("You can\'t be forced to do that")

        rte(self.name)

        if Globals.in_fight:
            raise ActionError("Not in the middle of a fight!")

        World.load()
        sendsys(
            self.name,
            self.name,
            -10000,
            self.room_id,
            "{} has left the game\n".format(self.name),
        )
        sendsys(
            self.name,
            self.name,
            -10113,
            self.room_id,
            "[ Quitting Game : {} ]\n".format(self.name),
        )

        dumpitems()

        self.character.strength = -1
        self.character.name = ''
        World.save()

        Globals.curmode = 0
        self.room_id = 0

        saveme()
        raise StopGame('Goodbye')

    def look(self):
        World.save()

        if self.room.death_room:
            Globals.ail_blind = False
            if not self.is_wizard:
                loseme(self.name)
                raise StopGame("bye bye.....")

        World.load()

        response = {
            'no_brief': self.room.no_brief,
            'is_dark': self.room.is_dark,
            'death': self.room.death_room,
            'items': [],
            'characters': [],
        }
        if self.is_dark:
            response.update({'error': "It is dark"})
        elif Globals.ail_blind:
            response.update({'error': "You are blind... you can't see a thing!"})
        else:
            response.update({
                'title': self.room.title,
                'text': self.room.description,
                'items': list(Item.list_items()),
            })
            if Globals.curmode == 1:
                response.update({'characters': list(Character.list_characters(self))})

        on_look()

        if self.is_wizard:
            response.update({'name': self.room.name})
        if self.is_god:
            response.update({'room_id': self.room.room_id})
            # Secret
            response.update({'zone': self.room.zone.name})
            response.update({'in_zone': self.room.in_zone})
            response.update({'exits': [e.room_to for e in self.room.exits]})
        response.update({'result': not response.get('error')})

        # error
        # name
        # death
        # title
        # text
        # items

        return response

    def list_exits(self):
        exits = {}
        for e in self.room.exits:
            if not e.available:
                continue
            if not self.is_wizard:
                exits[e.direction] = True
                # result.append(e.direction)
            else:
                room = Room.get(e.room_to)
                exits[e.direction] = "{}{}".format(room.zone.name, room.in_zone)
                # result.append("{} : {}{}".format(e.direction, room.zone.name, room.in_zone))
        return {'exits': exits or None}

    # Events
    def on_look(self):
        check_fight(self, fpbns("shazareth"))
        if not iscarrby(45, self.character_id):
            check_fight(self, fpbns("wraith"))
        check_fight(self, fpbns("bomber"))
        check_fight(self, fpbns("owin"))
        check_fight(self, fpbns("glowin"))
        check_fight(self, fpbns("smythe"))
        check_fight(self, fpbns("dio"))
        if not iscarrby(45, self.character_id):
            check_fight(self, fpbns("zombie"))
        check_fight(self, fpbns("rat"))
        check_fight(self, fpbns("ghoul"))
        check_fight(self, fpbns("ogre"))
        check_fight(self, fpbns("riatha"))
        check_fight(self, fpbns("yeti"))
        check_fight(self, fpbns("guardian"))

        if iscarrby(32, self.character_id):
            dorune()

        if self.character.helping is not None:
            check_help()


def check_fight(player, mobile):
    if mobile is None:
        return  # No such being
    consid_move(mobile)  # Maybe move it
    if not mobile.is_created:
        return
    if mobile.room_id != player.room_id:
        return
    if player.character.visible:
        return  # Im invis
    if randperc() > 40:
        return
    if mobile.character_id == fpbns("yeti").character_id and ohany({13: True}):
        return
    mhitplayer(mobile, player.character_id)


def check_help():
    return Player.player().check_help()


def is_dark():
    return Player.player().is_dark


def list_exits():
    return Player.player().list_exits()


def on_look():
    return Player.player().on_look()


def set_room(room_id):
    return Player.player().set_room(room_id)


# Signals


def sig_ctrlc():
    if Globals.in_fight:
        raise ActionError("^C\n")
    loseme()
    raise StopGame("Byeeeeeeeeee  ...........")


def sig_oops():
    loseme()
    return {'code': 255}


def sig_hup():
    return sig_oops()


def sig_int():
    return sig_ctrlc()


def sig_term():
    return sig_ctrlc()


def sig_tstp():
    return None


def sig_quit():
    return None


def sig_cont():
    return sig_oops()


# TODO: Implement


def chkcrip(*args):
    # raise NotImplementedError()
    print("chkcrip({})".format(args))
    return False


def consid_move(*args):
    # raise NotImplementedError()
    print("consid_move({})".format(args))


def dorune(*args):
    # raise NotImplementedError()
    print("dorune({})".format(args))


def dumpitems(*args):
    # raise NotImplementedError()
    print("dumpitems({})".format(args))


def fpbns(*args):
    # raise NotImplementedError()
    print("fpbns({})".format(args))
    return None


def iscarrby(*args):
    # raise NotImplementedError()
    print("iscarrby({})".format(args))
    return False


def ishere(*args):
    # raise NotImplementedError()
    print("ishere({})".format(args))
    return False


def loseme(*args):
    raise NotImplementedError()


def makebfr(*args):
    # raise NotImplementedError()
    print("makebfr({})".format(args))


def mhitplayer(*args):
    # raise NotImplementedError()
    print("makebfr({})".format(args))


def ocarrf(*args):
    raise NotImplementedError()


def ohany(*args):
    raise NotImplementedError()


def oloc(*args):
    raise NotImplementedError()


def otstbit(*args):
    raise NotImplementedError()


def putmeon(*args):
    # raise NotImplementedError()
    print("putmeon({})".format(args))


def randperc(*args):
    # raise NotImplementedError()
    print("randperc({})".format(args))
    return 0


def rte(*args):
    # raise NotImplementedError()
    print("rte({})".format(args))


def saveme(*args):
    # raise NotImplementedError()
    print("saveme({})".format(args))


def sendsys(*args):
    # raise NotImplementedError()
    print("sendsys({})".format(args))


# def sig_aloff():
#     raise NotImplementedError()


def sig_init():
    return {
        'SIGHUP': sig_oops,
        'SIGINT': sig_ctrlc,
        'SIGTERM': sig_ctrlc,
        'SIGTSTP': None,
        'SIGQUIT': None,
        'SIGCONT': sig_oops,
    }


def special(*args):
    # raise NotImplementedError()
    print("special({})".format(args))
