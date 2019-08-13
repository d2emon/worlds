import random
from .item import Item
from ..database import names, World
from .model import Model


class Weather(Model):
    class WeatherItem(Item):
        @property
        def state(self):
            return random.randrange(3)

        @classmethod
        def get(cls, item_id=0):
            return super().get(0)

    database_name = names.CLIMATES

    __WEATHER_ITEM = None

    def __init__(
        self,
        climate_id,
        descriptions=(),
    ):
        super().__init__()
        self.climate_id = climate_id
        self.__descriptions = descriptions

        if self.__WEATHER_ITEM is None:
            World.load()
            self.__WEATHER_ITEM = self.WeatherItem.get()

    @property
    def description(self):
        weather_id = self.__WEATHER_ITEM.state
        return self.__descriptions[weather_id] if weather_id < len(self.__descriptions) else None
