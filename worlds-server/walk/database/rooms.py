import os
from config import Config
from .database import Database
from .logger import logger


def parse_exits(data):
    return [int(next(data)) for _ in range(6)]


def parse(room_id, data):
    room = {
        'room_id': room_id,
        'title': None,
        'exits': parse_exits(data),
        'description': '',
        'death_room': False,
        'no_brief': False,
    }
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


max_room = 1500  # 99999
path = os.path.join(Config.MEDIA_FOLDER, 'rooms')


def room_loader():
    for room_id in range(max_room):
        filename = os.path.join(path, str(room_id))
        if not os.path.isfile(filename):
            continue
        logger.debug('Loading room: %s', room_id)
        with open(filename, "r") as file:
            yield room_id, file


class Rooms(Database):
    def __init__(self):
        super().__init__({room_id: parse(room_id, room) for room_id, room in room_loader()})

    def get(self, item_id):
        return self.all().get(item_id)
