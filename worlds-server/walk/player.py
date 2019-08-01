import random
from .exceptions import crapup, ActionError
from .database import World
from .globalVars import Globals
from .room import Room


class Player:
    WIZARD_LEVEL = 10
    GOD_LEVEL = 10000

    def __init__(self):
        self.level = 10000  # my_lev
        self.room_id = random.choice([
            -5,
            -183,
        ])  # curch

    @property
    def is_dark(self):
        def is_light(item_id):
            if item_id != 32 and not otstbit(item_id, 13):
                return False
            if ishere(item_id):
                return True
            if ocarrf(item_id) == 0 or ocarrf(item_id) == 3:
                return False
            if ploc(oloc(item_id)) != self.room_id:
                return False
            return True

        if self.is_wizard:
            return False
        if not self.room.is_dark:
            return False
        if any(is_light(item_id) for item_id in range(Globals.numobs)):
            return False

    @property
    def is_god(self):
        return self.level >= self.GOD_LEVEL

    @property
    def is_wizard(self):
        return self.level >= self.WIZARD_LEVEL

    @property
    def room(self):
        return Room(self.room_id)

    def set_room(self, room_id=None):
        if room_id is None:
            room_id = self.room_id

        World.load()
        setploc(Globals.mynum, room_id)
        return self.look()

    def look(self):
        World.save()

        if self.room.death_room:
            Globals.ail_blind = False
            if not self.is_wizard:
                loseme(Globals.globme)
                crapup("bye bye.....")

        World.load()

        response = {
            'no_brief': self.room.no_brief,
            'is_dark': self.room.is_dark,
            'death': self.room.death_room,
        }
        if self.is_dark:
            response.update({'error': "It is dark"})
        elif Globals.ail_blind:
            response.update({'error': "You are blind... you can't see a thing!"})
        else:
            lisobs()
            if Globals.curmode == 1:
                lispeople()
            # 5
            response.update({
                'title': self.room.title,
                'text': self.room.description,
                'additional': "\n",
            })

        onlook()

        if self.is_wizard:
            response.update({'name': self.room.show_name()})
        if self.is_god:
            response.update({'room_id': self.room.room_id})
            # Secret
            response.update({'zone': self.room.zone.name})
            response.update({'in_zone': self.room.in_zone})
        response.update({'result': not response.get('error')})

        # error
        # name
        # death
        # title
        # text
        # additional

        return response

    def go(self, direction_id):
        if Globals.in_fight > 0:
            raise ActionError(
                "You can't just stroll out of a fight!\n"
                "If you wish to leave a fight, you must FLEE in a direction\n"
            )
        if iscarrby(32, Globals.mynum) and ploc(25) == self.room_id and len(pname(25)):
            raise ActionError("[c]The Golem[/c] bars the doorway!\n")
        if chkcrip():
            raise ActionError("ERROR")

        room_id = self.room.exits[direction_id].go(self)
        room = Room(room_id)
        result = room.on_enter()

        if result.get('error'):
            return result

        sendsys(
            Globals.globme,
            Globals.globme,
            -10000,
            self.room_id,
            "[s name=\"{}\"]{} has gone {} {}.\n[/s]".format(
                pname(Globals.mynum),
                Globals.globme,
                Globals.exittxt.get(direction_id),
                Globals.out_ms,
            ),
        )

        sendsys(
            Globals.globme,
            Globals.globme,
            -10000,
            room.room_id,
            "[s name=\"{}\"]{} {}\n[/s]".format(
                Globals.globme,
                Globals.globme,
                Globals.in_ms,
            ),
        )

        self.room_id = room.room_id
        result.update({
            'result': not result.get('error'),
            'room': self.set_room(),
        })
        return result


PLAYER = Player()


def is_dark():
    return PLAYER.is_dark


def set_room(room_id):
    return PLAYER.set_room(room_id)


# TODO: Implement


def chkcrip(*args):
    # raise NotImplementedError()
    print("chkcrip({})".format(args))
    return False


def iscarrby(*args):
    # raise NotImplementedError()
    print("iscarrby({})".format(args))
    return False


def ishere(*args):
    # raise NotImplementedError()
    print("ishere({})".format(args))
    return False


def lisobs(*args):
    # raise NotImplementedError()
    print("lisobs({})".format(args))


def lispeople(*args):
    # raise NotImplementedError()
    print("lispeople({})".format(args))


def loseme(*args):
    raise NotImplementedError()


def ocarrf(*args):
    raise NotImplementedError()


def oloc(*args):
    raise NotImplementedError()


def onlook(*args):
    # raise NotImplementedError()
    print("onlook({})".format(args))


def otstbit(*args):
    raise NotImplementedError()


def ploc(*args):
    raise NotImplementedError()


def pname(*args):
    # raise NotImplementedError()
    print("pname({})".format(args))
    return ''


def sendsys(*args):
    # raise NotImplementedError()
    print("sendsys({})".format(args))


def setploc(*args):
    # raise NotImplementedError()
    print("setploc({})".format(args))
