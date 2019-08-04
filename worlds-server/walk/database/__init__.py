from ..exceptions import DatabaseError, StopGame
# Databases
from .exits import Exits
from .rooms import Rooms
from .world import WorldData
# Names
from . import names


__databases = {
    names.EXITS: Exits(),
    names.ROOMS: Rooms(),
    names.WORLD: WorldData(),
    names.ZONES: Rooms().ZONES,
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
            self.__data = connect(self.filename, "r+")
        except DatabaseError:
            raise StopGame("Cannot find World file")

        self.items, self.players = self.__data.all()  # ? objinfo[4 * numobs], ublock[16 * 48]

    def __write(self):
        self.__data.set(list(self.items.all()), list(self.players.all()))  # ? objinfo[4 * numobs], ublock[16 * 48]

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
