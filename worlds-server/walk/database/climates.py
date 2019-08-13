from .database import Database
from .weathers import Weathers


class Climates(Database):
    DEFAULT = 0
    RAINY = 1
    SNOWY = 2
    MILD = 3

    __ITEMS = {
        DEFAULT: (Weathers.NONE, Weathers.RAIN, Weathers.STORM, Weathers.SNOW),
        RAINY: (Weathers.NONE, Weathers.RAIN, Weathers.NONE, Weathers.RAIN),
        SNOWY: (Weathers.NONE, Weathers.SNOW, Weathers.BLIZZARD, Weathers.SNOW),
        MILD: (Weathers.NONE, Weathers.GENTLE_RAIN, Weathers.STORM, Weathers.SNOW),
    }

    def __init__(self):
        self.__items = self.__ITEMS
        self.__weathers = Weathers()

    def all(self):
        return (self.get(item_id) for item_id in self.__ITEMS.keys())

    def get(self, item_id):
        return lambda: {
            'climate_id': item_id,
            'descriptions': [self.__weathers.get(weather_id)() for weather_id in self.__ITEMS.get(item_id, [])]
        }
