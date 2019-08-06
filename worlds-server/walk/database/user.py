from .database import ListDatabase


class User(ListDatabase):
    __DEBUGGER = {
        'name': "Debugger",
        'strength': 100,
        'sex': 0,
        'level': 10033,
    }

    def reset(self):
        yield self.__DEBUGGER
