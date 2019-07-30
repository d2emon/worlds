from ..exceptions import crapup, DatabaseError
from .rooms import Rooms
from .world import WorldData


class World:
    filename = "/usr/tmp/-iy7AM"

    instance = None  # filrf

    def __init__(self):
        try:
            self.__data = connect(self.filename, "r+")
        except DatabaseError:
            crapup("Cannot find World file")

        self.items = self.__data['items']  # ? objinfo[4 * numobs]
        self.players = self.__data['players']  # ? ublock[16 * 48]

    def write(self):
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
        cls.instance.write()
        cls.instance = None


def load():
    return World.load()


def save():
    return World.save()


__databases = {
    'ROOMS': Rooms(),
    World.filename: WorldData(),
}


def connect(database, permissions, item_id=None):
    print("Connect to \'{}\' mode: {}".format(database, permissions))
    data = __databases.get(database)
    if data is None:
        raise DatabaseError()
    return data.all() if item_id is None else data.get(item_id)


def disconnect(database):
    print("Disconnect from \'{}\'".format(database))
