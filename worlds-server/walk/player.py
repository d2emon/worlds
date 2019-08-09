import random
from .exceptions import ActionError, DatabaseError, StopGame
from .database import World
from .globalVars import Globals
from .models.character import Character
from .models.item import Item
from .models.message import Message
from .models.room import Room


def turn(f):
    def wrapper(player, *args, **kwargs):
        player.on_before_turn()
        result = f(player, *args, **kwargs)
        player.on_after_turn()
        return result
    return wrapper


class Player:
    __PLAYER = None

    MAX_PLAYER = 16

    def __init__(self, name):
        # Set Fields
        self.character_id = 0  # mynum
        self.name = "The {}".format(name) if name == "Phantom" else name  # globme
        self.message_id = -1  # cms

        self.level = 10000  # my_lev
        self.__room_id = random.choice((
            -5,
            -183,

            # -643,
        ))  # curch

        self.__room = None

        # Talker
        World.load()
        self.character_id = Character.add(self.name)
        self.read_messages()
        # for c in Character.all():
        #     print(c.serialized)
        World.save()

        self.message_id = -1
        special(".g", self.name)
        Globals.i_setup = True

        self.__PLAYER = self

    @property
    def character(self):
        #
        World.load()
        #
        return Character.get(self.character_id)

    @property
    def is_dark(self):
        def is_light(item_id):
            item = Item.get(item_id)
            if item_id != 32 and not item.is_light:
                return False
            if ishere(item_id):
                return True
            owner = item.owner
            if owner is None or owner.room_id != self.room_id:
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
        return self.level >= self.character.GOD_LEVEL

    @property
    def is_wizard(self):
        return self.level >= self.character.WIZARD_LEVEL

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

    @property
    def can_see(self):
        return not Globals.ail_blind and not self.is_dark

    @property
    def carry(self):
        if self.is_wizard:
            return self.character.carry
        return (item for item in self.character.carry if not item.is_destroyed)

    @property
    def available_characters(self):
        return Character.find(
            room_id=self.room_id,
            not_player=self.character,
            exists_only=True,
        )

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

    def has_item(self, item_id):
        return self.character.has_item(item_id, include_destroyed=self.is_wizard)

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

    def can_see_character(self, character):
        if character is None:
            return True
        if self.character_id == character.character_id:
            return True  # me

        if Globals.ail_blind:
            return False  # Cant see
        if self.character.level < character.visible:
            return False
        if self.room_id == character.room_id and self.room.is_dark:
            return False

        setname(character)
        return True

    def read_messages(self, interrupt=False):
        World.load()

        for block in Message.read_from(self.message_id):
            mstoout(block, self)

        self.message_id = Message.last_message_id()

        update(self)
        eorte()

        Globals.rdes = 0
        Globals.tdes = 0
        Globals.vdes = 0

    @turn
    def wait(self):
        if not Globals.sig_active:
            return None

        sig_aloff()
        self.read_messages(interrupt=True)
        World.save()
        key_reprint()
        sig_alon()
        return {}

    @turn
    def go(self, direction_id):
        if Globals.in_fight > 0:
            raise ActionError(
                "You can't just stroll out of a fight!\n"
                "If you wish to leave a fight, you must FLEE in a direction\n"
            )

        treasure = self.has_item(32)
        golem = Character.get(25)
        if not golem or not golem.is_created:
            golem = None
        elif golem.room_id != self.room_id:
            golem = None

        if treasure and golem:
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

    @turn
    def quit_game(self):
        if Globals.is_forced:
            raise ActionError("You can\'t be forced to do that")

        self.read_messages()

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

    @turn
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
        messages = []
        if self.is_dark:
            response.update({'error': "It is dark"})
        elif Globals.ail_blind:
            response.update({'error': "You are blind... you can't see a thing!"})
        else:
            response.update({
                'title': self.room.title,
                'text': self.room.description,
            })
            response.update(self.room.list_items(self))

            if Globals.curmode == 1:
                response.update({'characters': list(Character.list_characters(self))})

        messages += self.on_look().get('messages', [])

        response.update({'messages': messages})
        if self.is_wizard:
            response.update({'name': self.room.name})
        if self.is_god:
            response.update({'room_id': self.room.room_id})
            # Secret
            response.update({
                'zone': (self.room.zone.name, self.room.in_zone),
                'exits': [e.room_to for e in self.room.exits],
                'outdoors': self.room.outdoors,
            })
        response.update({'result': not response.get('error')})

        # error
        # messages
        # name
        # death
        # title
        # text
        # items
        return response

    @turn
    def jump(self):
        room_id = self.room.jump_to
        if room_id is None:
            return {'message': "Wheeeeee....\n"}

        #
        World.load()
        #
        umbrella = Item.get(1)
        if not self.is_wizard and (not self.has_item(umbrella.item_id) or umbrella.state == 0):
            self.__room_id = room_id
            loseme()
            return {
                'message': "Wheeeeeeeeeeeeeeeee  <<<<SPLAT>>>>\nYou seem to be splattered all over the place\n",
                'crapup': "I suppose you could be scraped up - with a spatula",
            }

        sendsys(
            self.name,
            self.name,
            -10000,
            self.room_id,
            "[s name=\"{}\"]{} has just left\n[/s]".format(self.name, self.name),
        )
        self.room_id = room_id
        self.set_room()
        sendsys(
            self.name,
            self.name,
            -10000,
            self.room_id,
            "[s name=\"{}\"]{} has just dropped in\n[/s]".format(self.name, self.name),
        )
        return {'result': True}

    @turn
    def list_exits(self):
        exits = {}
        for e in self.room.exits:
            if e.door_id:
                exits[e.direction] = "DOOR{}".format(e.door_id)
                continue
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

    def on_before_turn(self):
        pbfr()
        # sendmsg(name)

    def on_after_turn(self):
        if Globals.rd_qd:
            self.read_messages()
            Globals.rd_qd = False
        World.save()
        pbfr()

    def on_look(self):
        turn_undead = self.has_item(45)

        enemies = (
            "shazareth",
            "bomber",
            "owin",
            "glowin",
            "smythe",
            "dio",
            "rat",
            "ghoul",
            "ogre",
            "riatha",
            "yeti",
            "guardian",
        )
        for name in enemies:
            check_fight(self, next(Character.find(name=name)))

        undead = (
            "wraith",
            "zombie",
        )
        if not turn_undead:
            for name in undead:
                check_fight(self, next(Character.find(name=name)))

        messages = [item.on_wait(self).get('message', '') for item in self.carry]
        messages = filter(None, messages)

        if self.character.helping is not None:
            check_help()

        return {'messages': list(messages)}

    def on_stop_game(self):
        pbfr()
        Globals.pr_due = False  # So we dont get a prompt after the exit


def check_fight(player, mobile):
    if mobile is None:
        return  # No such being

    mobile.check_move()  # Maybe move it
    if not mobile.is_created:
        return
    if mobile.room_id != player.room_id:
        return
    if player.character.visible:
        return  # Im invisible
    if randperc() > 40:
        return

    yeti = next(Character.find(name="yeti"))
    if yeti and mobile.character_id == yeti.character_id and ohany({13: True}):
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


def dumpitems(*args):
    # raise NotImplementedError()
    print("dumpitems({})".format(args))


def eorte(*args):
    # raise NotImplementedError()
    print("eorte({})".format(args))


def ishere(*args):
    # raise NotImplementedError()
    print("ishere({})".format(args))
    return False


def loseme(*args):
    raise NotImplementedError()


def mhitplayer(*args):
    # raise NotImplementedError()
    print("makebfr({})".format(args))


def mstoout(*args):
    # raise NotImplementedError()
    print("mstoout({})".format(args))


def ohany(*args):
    # raise NotImplementedError()
    print("ohany({})".format(args))


def pbfr(*args):
    # raise NotImplementedError()
    print("pbfr({})".format(args))


def randperc(*args):
    # raise NotImplementedError()
    print("randperc({})".format(args))
    return 0


def saveme(*args):
    # raise NotImplementedError()
    print("saveme({})".format(args))


def sendsys(*args):
    # raise NotImplementedError()
    print("sendsys({})".format(args))


def setname(*args):
    # raise NotImplementedError()
    print("setname({})".format(args))


def sig_aloff():
    # raise NotImplementedError()
    print("sig_aloff")


def sig_alon():
    # raise NotImplementedError()
    print("sig_alon")


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


def update(*args):
    # raise NotImplementedError()
    print("update({})".format(args))
