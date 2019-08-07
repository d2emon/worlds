import random
from .item import Item


class Weather(Item):
    @property
    def weather_id(self):
        # return self.state
        return random.randrange(3)

    @classmethod
    def get(cls, item_id=0):
        return super().get(0)

    @classmethod
    def __get_weather_id(cls, room_id, weather_id):
        if -199 >= room_id >= -179:
            return weather_id % 2 if weather_id > 1 else weather_id
        elif -100 >= room_id >= -178:
            return weather_id + 2 if weather_id in (1, 2) else weather_id
        return weather_id

    def get_description(self, room):
        if not room.outdoors:
            return None

        stormy = -178 > room.room_id > -199
        weather_id = self.__get_weather_id(room.room_id, self.weather_id)
        if weather_id == 1:
            if stormy:
                return "It is raining, a gentle mist of rain, which sticks to everything around\n" \
                       "you making it glisten and shine. High in the skies above you is a rainbow\n"
            else:
                return "[c]It is raining\n[/c]"
        elif weather_id == 2:
            return "[c]The skies are dark and stormy\n[/c]"
        elif weather_id == 3:
            return "[c]It is snowing\n[/c]"
        elif weather_id == 4:
            return "[c]A blizzard is howling around you\n[/c]"
        return None
