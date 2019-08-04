from .database import Database


class Zones(Database):
    __ITEMS = {
        0: "TCHAN",
        1: "LIMBO",
        2: "WSTORE",
        4: "HOME",
        5: "START",
        6: "PIT",
        19: "WIZROOM",
        99: "DEAD",
        299: "BLIZZARD",
        399: "CAVE",
        499: "LABRNTH",
        599: "FOREST",
        699: "VALLEY",
        799: "MOOR",
        899: "ISLAND",
        999: "SEA",
        1049: "RIVER",
        1069: "CASTLE",
        1099: "TOWER",
        1101: "HUT",
        1105: "TREEHOUSE",
        2199: "QUARRY",
        2299: "LEDGE",
        2499: "INTREE",
        99999: "WASTE",
    }

    def __init__(self):
        self.__items = self.__ITEMS

    @property
    def __default(self):
        return self.__items[0]

    def by_end(self, end):
        end = max(end, 0)
        keys = [key for key in self.__items.keys() if key < end]
        return {
            'name': self.__items.get(end, self.__default),
            'begin': max(keys) + 1 if len(keys) else None,
            'end': end,
        }

    def by_room_id(self, room_id):
        room_id = -room_id
        keys = [key for key in self.__items.keys() if key >= room_id]
        return self.by_end(min(keys) if len(keys) else 0)

    def all(self):
        return (self.by_end(end) for end in self.__items.keys())

    def get(self, item_id):
        keys = list(self.__items.keys())
        keys.sort()
        return lambda: self.by_room_id(keys[item_id])
