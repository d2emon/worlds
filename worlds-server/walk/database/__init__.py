from ..exceptions import DatabaseError, StopGame
# Databases
from .rooms import Rooms
from .world import WorldData
from .zones import Zones
from . import names


__databases = {
    names.ROOMS: Rooms(),
    names.WORLD: WorldData(),
    names.ZONES: Zones(),
}


def connect(database, permissions=None):
    print("Connect to \'{}\' mode: {}".format(database, permissions))
    data = __databases.get(database)
    if data is None:
        raise DatabaseError()
    return data


def disconnect(database):
    print("Disconnect from \'{}\'".format(database))


class World:
    filename = names.WORLD

    instance = None  # filrf

    def __init__(self):
        try:
            self.__data = connect(self.filename, "r+").all()
        except DatabaseError:
            raise StopGame("Cannot find World file")

        self.items = self.__data['items']  # ? objinfo[4 * numobs]
        self.players = self.__data['players']  # ? ublock[16 * 48]

    def __write(self):
        self.__data['items'] = self.items  # ? objinfo[4 * numobs]
        self.__data['players'] = self.players  # ? ublock[16 * 48]

        disconnect(self)

    @classmethod
    def load(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    @classmethod
    def save(cls):
        if cls.instance is None:
            return
        cls.instance.__write()
        cls.instance = None


def load():
    return World.load()


def save():
    return World.save()
