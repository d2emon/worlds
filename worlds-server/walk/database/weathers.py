from .database import Database


class Weathers(Database):
    NONE = 0
    RAIN = 1
    GENTLE_RAIN = 2
    STORM = 3
    SNOW = 4
    BLIZZARD = 5

    __ITEMS = {
        NONE: "",
        RAIN: "[c]It is raining\n[/c]",
        GENTLE_RAIN: "It is raining, a gentle mist of rain, which sticks to everything around\n"
                     "you making it glisten and shine. High in the skies above you is a rainbow\n",
        STORM: "[c]The skies are dark and stormy\n[/c]",
        SNOW: "[c]It is snowing\n[/c]",
        BLIZZARD: "[c]A blizzard is howling around you\n[/c]",
    }

    def __init__(self):
        self.__items = self.__ITEMS

    def all(self):
        return ({
            'weather_id': key,
            'description': value,
        } for key, value in self.__ITEMS.items())

    def get(self, item_id):
        return lambda: self.__ITEMS.get(item_id, '')
