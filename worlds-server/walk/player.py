import random
import time
from .exceptions import ActionError, StopGame
from .database import World
from .globalVars import Globals
from .messages import process
from .models.character import Character
from .models.item import Item
from .models.message import Message
from .models.room import Room


def special(action, player):
    if not action or action[0] != ".":
        return
    code = action[1:].lower()

    if code == "q":
        return
    elif code == "g":
        return player.start()
    else:
        raise ActionError("Unknown . option")


def turn(command=None):
    def wrapper(f):
        def wrapped(player, *args, **kwargs):
            messages = []

            messages += player.on_before_turn()

            player.add_command(command)
            result = f(player, *args, **kwargs) or {}
            player.add_messages(*result.get('messages', []))

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
        self.strength = 0
        self.sex = 0

        self.__room_id = -5  # curch

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

        self.start()
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
    def helping(self):
        if self.character.helping is None:
            return None
        return Character.get(self.character.helping)

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
    def restart(cls, name):
        cls.__PLAYER = cls(name)
        return {
            'player': {
                'name': cls.__PLAYER.name,
            },
            'message': "Hello {}".format(cls.__PLAYER.name),
        }

    @classmethod
    def set_pronoun(cls, character):
        """
        Assign Him her etc according to who it is

        :param character:
        :return:
        """
        if character is None:
            return

        if character.sex == 0:
            Globals.wd_him = character
        elif character.sex == 1:
            Globals.wd_her = character
        elif character.sex == 2:
            Globals.wd_it = character
            return

        Globals.wd_them = character

    def has_item(self, item_id):
        return self.character.has_item(item_id, include_destroyed=self.is_wizard)

    def set_room(self, room_id=None):
        if room_id is None:
            room_id = self.room_id

        World.load()

        self.character.room_id = room_id
        return self.look()

    def __stop_help(self, name=''):
        self.character.helping = None
        self.add_messages("You can no longer help [c]{}[/c]\n".format(name))

    def check_help(self):
        if self.character.helping is None:
            return
        if not Globals.i_setup:
            return

        helping = self.helping
        if helping is None or not helping.is_created:
            return self.__stop_help()
        elif helping.room_id != self.room_id:
            return self.__stop_help(helping.name)

    def read_messages(self, interrupt=False):
        World.load()

        for block in Message.read_from(self.message_id):
            mstoout(block, self)

        self.message_id = Message.last_message_id()
        self.on_after_messages(interrupt=interrupt)

        Globals.rdes = 0
        Globals.tdes = 0
        Globals.vdes = 0

    def __decode(self, dst=None, is_keyboard=False):
        return [process(self, message, dst, is_keyboard=is_keyboard) for message in self.__text_messages]

    def get_text(self):
        result = []

        World.save()

        if Globals.log_fl is not None:
            result += self.__decode(Globals.log_fl, is_keyboard=False)

        if Globals.snoopd is not None:
            fln = opensnoop(Globals.snoopd.name, "a")
            if fln is not None:
                result += self.__decode(fln, is_keyboard=False)
                # disconnect(fln)

        result += self.__decode(is_keyboard=True)

        self.__text_messages = []  # clear buffer

        if Globals.snoopt is not None:
            result.append(viewsnoop())

        return result

    def add_command(self, command):
        if not command:
            return

        self.add_messages("[l]{}\n[/l]".format(command))

        self.read_messages()
        World.save()

        command = command.lower()
        if Globals.curmode:
            return gamecom(command)
        else:
            return special(command, self)

    # Text Messages

    def add_messages(self, *messages):
        self.__text_messages += filter(None, messages)

    # Specials

    def start(self):
        self.__message_id = -1
        Globals.curmode = True

        initme()

        World.load()
        self.character.strength = self.strength
        self.character.level = self.level
        self.character.visible = 0 if self.level < 10000 else 10000
        self.character.weapon = None
        self.character.sex = self.sex
        self.character.helping = None
        self.character.save()

        sendsys(
            self.name,
            self.name,
            -10113,
            self.room_id,
            "[s name=\"{name}\"][ {name}  has entered the game ]\n[/s]".format(name=self.name),
        )
        self.read_messages()
        self.room_id = random.choice((
            # -5,
            # -183,

            -167,
        ))  # -5 if randperc() > 50 else -183
        self.set_room()
        sendsys(
            self.name,
            self.name,
            -10000,
            self.room_id,
            "[s name=\"{name}\"]{name}  has entered the game\n[/s]".format(name=self.name),
        )

    # Actions

    def wait(self):
        self.read_messages(interrupt=True)
        self.on_time()
        World.save()
        return {'messages': self.__text_messages}

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
        result.update({'result': not result.get('error')})
        result.update(self.set_room())
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
        def process_item(item):
            item.update({'description': process(self, item.get('description', ''))})
            return item

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

        if self.is_dark:
            error = "It is dark"
        elif Globals.ail_blind:
            error = "You are blind... you can't see a thing!"
        else:
            room_data.update({
                'title': self.room.title,
                'text': self.room.description,
            })
            items = self.room.list_items(self)
            print(items)
            room_data.update({
                'flannel': [process_item(item) for item in items.get('flannel', [])],
                'weather': process(self, items.get('weather', '')),
                'items': [process_item(item) for item in items.get('items', [])],
            })

            if Globals.curmode == 1:
                room_data.update({'characters': list(Character.list_characters(self))})

        self.on_look()

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

    @turn('dig')
    def dig(self):
        #
        World.load()
        #
        garlic = Item.get(100)
        hole = Item.get(176)
        slab = Item.get(186)
        print(garlic.name, garlic.room_id, self.room_id, garlic.is_destroyed)
        if garlic.room_id == self.room_id and garlic.is_destroyed:
            garlic.create()
            return {'message': "Вы что-то нашли!\n"}
        if slab.room_id == self.room_id and slab.is_destroyed:
            slab.create()
            return {'message': "You uncover a stone slab!\n"}
        if self.room_id in (-172, -192):
            if hole.state == 0:
                return {'message': "You widen the hole, but with little effect.\n"}
            hole.state = 0
            return {'message': "You rapidly dig through to another passage.\n"}
        return {'message': "You find nothing.\n"}

    # Events

    def on_error(self):
        loseme(self)
        return {'fatalError': 255}

    def on_look(self):
        turn_undead = self.has_item(45)
        for enemy in Character.find(aggressive=True):
            enemy.check_fight(self, undead=not turn_undead)

        for item in self.carry:
            self.add_messages(item.on_wait(self).get('message', ''))

        self.check_help()

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
            self.strength += 1
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
        return self.get_text()

    def on_time(self):
        if randperc() > 80:
            self.on_look()

    def on_before_turn(self):
        return self.get_text()

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


def is_dark():
    return Player.player().is_dark


def list_exits():
    return Player.player().list_exits()


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


def initme(*args):
    # raise NotImplementedError()
    print("initme({})".format(args))


def ishere(*args):
    # raise NotImplementedError()
    print("ishere({})".format(args))
    return False


def iswornby(*args):
    # raise NotImplementedError()
    print("iswornby({})".format(args))
    return False


def loseme(*args):
    raise NotImplementedError()


def mstoout(*args):
    # raise NotImplementedError()
    print("mstoout({})".format(args))


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


__MESSAGES = []


def sendsys(*args):
    # raise NotImplementedError()
    print("sendsys({})".format(args))
    __MESSAGES.append(args)
    for m in __MESSAGES:
        print(m)


def update(*args):
    # raise NotImplementedError()
    print("update({})".format(args))


def viewsnoop(*args):
    # raise NotImplementedError()
    print("viewsnoop({})".format(args))
