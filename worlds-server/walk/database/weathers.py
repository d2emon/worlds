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
        RAIN: "[c]Идет дождь.\n[/c]",
        GENTLE_RAIN: "Идет дождь, все вокруг блестит и сверкает, покрытое капельками дождя. "
                     "Высоко в небе над вами видна радуга.\n",
        STORM: "[c]Небо темное и грозовое.\n[/c]",
        SNOW: "[c]Идет снег.\n[/c]",
        BLIZZARD: "[c]Вокруг вас воет метель.\n[/c]",
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
