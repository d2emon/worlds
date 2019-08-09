import random
import time
from .exceptions import ActionError, StopGame
from .database import World
from .globalVars import Globals
from .models.character import Character
from .models.item import Item
from .models.message import Message
from .models.room import Room


def turn(command=None):
    def wrapper(f):
        def wrapped(player, *args, **kwargs):
            messages = []

            messages += player.on_before_turn()

            if command is not None:
                player.add_command(command)
            result = f(player, *args, **kwargs) or {}

            messages += player.on_after_turn()

            result['messages'] = list(filter(None, messages))
            return result
        return wrapped
    return wrapper


class Player:
    __PLAYER = None

    MAX_PLAYER = 16

    def __init__(self, name):
        # Set Fields
        self.character_id = 0  # mynum
        self.name = "The {}".format(name) if name == "Phantom" else name  # globme
        self.__message_id = -1  # cms

        self.level = 10000  # my_lev
        self.__room_id = random.choice((
            -5,
            -183,

            # -643,
        ))  # curch

        self.__updated = 0  # lasup
        self.__interrupt = None  # last_io_interrupt
        self.__text_messages = []

        self.__room = None

        # Talker
        World.load()
        self.character_id = Character.add(self.name)
        self.read_messages()
        # for c in Character.all():
        #     print(c.serialized)
        World.save()

        self.__message_id = -1
        special(".g", self.name)
        Globals.i_setup = True

        self.__PLAYER = self

    @property
    def message_id(self):
        return self.__message_id

    @message_id.setter
    def message_id(self, value):
        self.__message_id = value

        if abs(self.__message_id - self.__updated):
            return

        World.load()
        self.character.message_id = self.message_id
        self.character.save()
        self.__updated = self.message_id

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
        self.on_after_messages(interrupt=interrupt)

        Globals.rdes = 0
        Globals.tdes = 0
        Globals.vdes = 0

    def __decode(self, dst=None, keyboard=False):
        return dcprnt(self.__text_messages, dst, iskb=keyboard)

    def get_text(self):
        result = []

        World.save()

        if len(self.__text_messages):
            Globals.pr_due = True
            if Globals.pr_qcr:
                result.append("\n")
        Globals.pr_qcr = False

        if Globals.log_fl is not None:
            result.append(self.__decode(Globals.log_fl, keyboard=False))

        if Globals.snoopd is not None:
            fln = opensnoop(Globals.snoopd.name, "a")
            if fln is not None:
                result.append(self.__decode(fln, keyboard=False))
                # disconnect(fln)

        result.append(self.__decode(keyboard=True))

        # self.__text_messages = []  # clear buffer

        if Globals.snoopt is not None:
            result.append(viewsnoop())

        return result

    def add_command(self, command):
        self.__text_messages.append("[l]{}\n[/l]".format(command))

        self.read_messages()
        World.save()

        command = command.lower()
        result = command and command != ".q"
        if Globals.curmode:
            gamecom(command)
        elif result:
            special(command, self.name)
        return result

    def wait(self):
        self.read_messages(interrupt=True)
        World.save()

        key_reprint()
        # return None
        return {
            'messages': self.__text_messages,
        }

    @turn()
    def go(self, direction_id):
        self.add_command("go {}".format(direction_id))

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

    @turn('quit')
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

    @turn('look')
    def look(self):
        World.save()

        if self.room.death_room:
            Globals.ail_blind = False
            if not self.is_wizard:
                loseme(self.name)
                raise StopGame("bye bye.....")

        World.load()

        error = False
        room_data = {
            'no_brief': self.room.no_brief,
            'is_dark': self.room.is_dark,
            'death': self.room.death_room,
            'items': [],
            'characters': [],
        }
        messages = []
        if self.is_dark:
            error = "It is dark"
        elif Globals.ail_blind:
            error = "You are blind... you can't see a thing!"
        else:
            room_data.update({
                'title': self.room.title,
                'text': self.room.description,
            })
            room_data.update(self.room.list_items(self))

            if Globals.curmode == 1:
                room_data.update({'characters': list(Character.list_characters(self))})

        messages += self.on_look().get('messages', [])

        room_data.update({'messages': messages})
        if self.is_wizard:
            room_data.update({'name': self.room.name})
        if self.is_god:
            room_data.update({'room_id': self.room.room_id})
            # Secret
            room_data.update({
                'zone': (self.room.zone.name, self.room.in_zone),
                'exits': [e.room_to for e in self.room.exits],
                'outdoors': self.room.outdoors,
            })

        # error
        # messages
        # name
        # death
        # title
        # text
        # items
        response = {'room':  room_data}
        if error:
            response.update({'error': error})
        return response

    @turn('jump')
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

    @turn('exits')
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

    def on_error(self):
        loseme(self)
        return {'fatalError': 255}

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

    def on_after_messages(self, interrupt=True):
        def check_invisibility():
            if not Globals.me_ivct:
                return

            Globals.me_ivct -= 1

            if Globals.me_ivct != 1:
                return

            self.character.visible = 0
            self.character.save()

        def check_calibrate():
            if not Globals.me_cal:
                return

            Globals.me_cal = False
            calibme()

        def check_summon():
            if not Globals.tdes:
                return
            dosumm(Globals.ades)

        def check_in_fight():
            if not Globals.in_fight:
                return
            if Globals.fighting.room_id != self.room_id:
                Globals.in_fight = 0
                Globals.fighting = None
            if not Globals.fighting.is_created:
                Globals.in_fight = 0
                Globals.fighting = None
            if interrupt and Globals.in_fight:
                Globals.in_fight = 0
                hitplayer(Globals.fighting, Globals.wpnheld)

        def check_magic_item():
            if not iswornby(18, self.character_id) and randperc() >= 10:
                return
            Globals.my_str += 1
            if Globals.i_setup:
                calibme()

        def check_drink():
            if Globals.me_drunk <= 0:
                return
            Globals.me_drunk -= 1
            if Globals.ail_dumb:
                return
            parse("hiccup")

        current_time = time.time()
        interrupt = interrupt or not self.__interrupt or (current_time - self.__interrupt) > 2
        if interrupt:
            self.__interrupt = current_time

        check_invisibility()
        check_calibrate()
        check_summon()
        check_in_fight()
        check_magic_item()
        forchk()
        check_drink()

    def on_quit(self):
        if Globals.in_fight:
            raise ActionError("^C\n")
        loseme(self)
        raise StopGame("Byeeeeeeeeee  ...........")

    def on_stop_game(self):
        result = self.get_text()
        Globals.pr_due = False  # So we dont get a prompt after the exit
        return result

    def on_before_turn(self):
        result = self.get_text()
        sendmsg(self)
        return result

    def on_after_turn(self):
        # Check Fight
        if Globals.fighting:
            if not Globals.fighting.is_created or Globals.fighting.room_id != self.room_id:
                Globals.in_fight = 0
                Globals.fighting = None

        if Globals.in_fight:
            Globals.in_fight -= 1

        # Read messages
        if Globals.rd_qd:
            self.read_messages()
            Globals.rd_qd = False

        # Save
        World.save()
        return self.get_text()


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


# TODO: Implement


def calibme(*args):
    # raise NotImplementedError()
    print("calibme({})".format(args))


def chkcrip(*args):
    # raise NotImplementedError()
    print("chkcrip({})".format(args))
    return False


def dcprnt(source, dest, **kwargs):
    # raise NotImplementedError()
    print("dcprnt({}, {}, {})".format(source, dest, kwargs))
    if not source:
        return None
    if dest is None:
        return "dcprnt({}, {}, {})".format(source, dest, kwargs)
    return None


def dosumm(*args):
    # raise NotImplementedError()
    print("dosumm({})".format(args))


def dumpitems(*args):
    # raise NotImplementedError()
    print("dumpitems({})".format(args))


def forchk(*args):
    # raise NotImplementedError()
    print("forchk({})".format(args))


def gamecom(*args):
    # raise NotImplementedError()
    print("gamecom({})".format(args))


def hitplayer(*args):
    # raise NotImplementedError()
    print("hitplayer({})".format(args))


def ishere(*args):
    # raise NotImplementedError()
    print("ishere({})".format(args))
    return False


def iswornby(*args):
    # raise NotImplementedError()
    print("iswornby({})".format(args))
    return False


def key_reprint(*args):
    # raise NotImplementedError()
    print("key_reprint({})".format(args))


def loseme(*args):
    raise NotImplementedError()


def mhitplayer(*args):
    # raise NotImplementedError()
    print("mhitplayer({})".format(args))


def mstoout(*args):
    # raise NotImplementedError()
    print("mstoout({})".format(args))


def ohany(*args):
    # raise NotImplementedError()
    print("ohany({})".format(args))


def opensnoop(*args):
    # raise NotImplementedError()
    print("opensnoop({})".format(args))
    return None


def parse(*args):
    # raise NotImplementedError()
    print("parse({})".format(args))


def randperc(*args):
    # raise NotImplementedError()
    print("randperc({})".format(args))
    return 0


def saveme(*args):
    # raise NotImplementedError()
    print("saveme({})".format(args))


def sendmsg(*args):
    # raise NotImplementedError()
    print("sendmsg({})".format(args))


def sendsys(*args):
    # raise NotImplementedError()
    print("sendsys({})".format(args))


def setname(*args):
    # raise NotImplementedError()
    print("setname({})".format(args))


def special(*args):
    # raise NotImplementedError()
    print("special({})".format(args))


def update(*args):
    # raise NotImplementedError()
    print("update({})".format(args))


def viewsnoop(*args):
    # raise NotImplementedError()
    print("viewsnoop({})".format(args))
