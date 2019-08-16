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
        # 0-99      Light Indoors
        299: "BLIZZARD",
        # 100-102   Light Outdoors Snow
        # 103-168   Light Indoors  Snow
        # 169       Light Outdoors Snow
        # 170       Light Indoors  Snow
        # 171-178   Light Outdoors Snow
        # 179-182   Light Outdoors Mild
        # 183       Light Indoors  Mild
        # 184-190   Light Outdoors Mild
        # 191-199   Light Indoors  Mild
        # 200-299   Light Indoors
        399: "CAVE",
        # 300-399   Dark  Indoors
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
        # 400-1105  Light Indoors
        2199: "QUARRY",
        # 1106-1112 Light Indoors
        # 1113-1123 Dark  Indoors
        # 1124-2199 Light Indoors
        2299: "LEDGE",
        2499: "INTREE",
        9999: "UNKNOWN",
        19999: "ARDA",
        99999: "WASTE",
        # 2200-...  Light Indoors
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

    def by_name(self, name):
        return self.by_end(next((key for (key, value) in self.__items.items() if value == name), 0))

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
