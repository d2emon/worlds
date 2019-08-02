import os
from config import Config
from .database import Database
from .exits import Exits
from .logger import logger


class Rooms(Database):
    __MAX_ROOM = 1500  # 99999
    __PATH = os.path.join(Config.MEDIA_FOLDER, 'rooms')

    @classmethod
    def __is_dark(cls, room_id):
        if room_id in (-1100, -1101):
            return False
        if -1123 <= room_id <= -1113:
            return True
        if room_id < -399 or room_id > -300:
            return False
        return True

    @classmethod
    def __room(cls, room_id):
        return {
            'room_id': room_id,
            'title': None,
            'exits': [],
            'description': None,
            'death_room': False,
            'no_brief': False,
            'is_dark': cls.__is_dark(room_id),
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
        filename = os.path.join(cls.__PATH, str(-room_id))
        if not os.path.isfile(filename):
            return cls.__room(room_id)
        logger.debug('Loading room: %s', room_id)
        with open(filename, "r") as file:
            return cls.__parse(room_id, file)

    def all(self):
        return (self.get(-item_id)() for item_id in range(self.__MAX_ROOM))

    def get(self, item_id):
        return lambda: self.__load_room(item_id)
