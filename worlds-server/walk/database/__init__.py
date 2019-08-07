from ..exceptions import DatabaseError, StopGame
from .logger import logger
# Databases
from .exits import Exits
from .reset_data import ResetData
from .rooms import Rooms
from .world import WorldData
# Names
from . import names


__databases = {
    names.EXAMINES: "EXAMINES",
    names.EXITS: Exits(),
    names.LOG: "LOG",
    names.RESET_DATA: ResetData(),
    names.RESET_N: "RESET_N",
    names.RESET_T: "RESET_T",
    names.ROOMS: Rooms(),
    names.SNOOP: "SNOOP",
    names.TEXTS: "TEXTS",
    names.USERS: "USERS",
    names.WORLD: WorldData(),
    names.ZONES: Rooms().ZONES,
}


def connect(database, permissions=None):
    logger.debug("Connect to '%s' mode: %s", database, permissions)
    data = __databases.get(database)
    if data is None:
        raise DatabaseError()
    return data


def disconnect(database):
    logger.debug("Disconnect from '%s'", database)


class World:
    filename = names.WORLD

    instance = None  # filrf

    def __init__(self):
        try:
            self.__data = connect(self.filename, "r+")
        except DatabaseError:
            raise StopGame("Cannot find World file")

        data = self.__data.all()
        self.items = data['items']  # ? objinfo[4 * numobs]
        self.players = data['players']  # ? ublock[16 * 48]

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
