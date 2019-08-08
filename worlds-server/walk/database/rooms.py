import os
from config import Config
from .database import Database
from .exits import Exits
from .logger import logger
from .zones import Zones


class Rooms(Database):
    ZONES = Zones()

    __MAX_ROOM = 1500  # 99999
    __PATH = os.path.join(Config.MEDIA_FOLDER, 'rooms')

    @classmethod
    def __is_dark(cls, room_id):
        if room_id in (-1100, -1101):
            return False
        if -1113 >= room_id >= -1123:
            return True
        if room_id < -399 or room_id > -300:
            return False
        return True

    @classmethod
    def __outdoors(cls, room_id):
        if room_id in (-100, -101, -102):
            return True
        elif room_id == -183:
            return False
        elif room_id == -170:
            return False
        elif -168 > room_id > -191:
            return True
        elif -181 > room_id > -172:
            return True
        else:
            return False

    @classmethod
    def __climate_id(cls, room_id):
        if -199 >= room_id >= -179:
            return 1
        elif -100 >= room_id >= -178:
            return 2
        elif -178 > room_id > -199:
            return 3
        return 0

    @classmethod
    def __jump_to(cls, room_id):
        return {
            -643: -633,
            -1050: -662,
            -1082: -1053,
        }.get(room_id)

    @classmethod
    def __zone(cls, room_id):
        return cls.ZONES.by_room_id(room_id)

    @classmethod
    def __room(cls, room_id):
        return {
            'room_id': room_id,
            'zone': cls.__zone(room_id).get('name'),
            'title': None,
            'exits': [],
            'jump_to': cls.__jump_to(room_id),
            'description': None,
            'death_room': False,
            'no_brief': False,
            'is_dark': cls.__is_dark(room_id),
            'outdoors': cls.__outdoors(room_id),
            'climate_id': cls.__climate_id(room_id),
        }

    @classmethod
    def __parse(cls, room_id, data):
        room = cls.__room(room_id)
        room['exits'] = list(Exits.parse(room_id, data))
        room['description'] = ""
        for s in data:
            s = s.rstrip()
            if s.strip() == "#DIE":
                room['death_room'] = True
            elif s.strip() == "#NOBR":
                room['no_brief'] = True
            elif room['title'] is None:
                room['title'] = s
            else:
                s = s.replace("    ", "\n")
                room['description'] += "{}\n".format(s)
        return room

    @classmethod
    def __load_room(cls, room_id):
        zone = cls.__zone(room_id).get('name')
        filename = os.path.join(cls.__PATH, zone, str(-room_id))
        if not os.path.isfile(filename):
            return cls.__room(room_id)
        logger.debug('Loading room: %s', room_id)
        with open(filename, "r") as file:
            return cls.__parse(room_id, file)

    def all(self):
        return (self.get(-item_id)() for item_id in range(self.__MAX_ROOM))

    def get(self, item_id):
        return lambda: self.__load_room(item_id)
