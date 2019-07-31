from .database import Database


class Zones(Database):
    __ZONES = {
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
        super().__init__(list(self.__zones_generator()))

    @classmethod
    def __zones_generator(cls):
        ends = list(cls.__ZONES.keys())
        ends.sort()
        begin = 1
        for end in ends:
            yield {
                'name': cls.__ZONES[end],
                'begin': begin,
                'end': end,
            }
            begin = end + 1

    def get(self, item_id):
        return self.all().get(item_id)
