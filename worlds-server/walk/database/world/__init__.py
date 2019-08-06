from ..database import Database
from ..characters import Characters
from ..items import Items


class WorldData(Database):
    def __init__(self):
        self.value0 = 1
        self.value1 = 1
        self.items = Items()
        self.players = Characters()

    def all(self):
        return {
            0: self.value0,
            1: self.value1,
            'items': self.items,
            'players': self.players,
        }

    def get(self, item_id):
        return None

    def reset(self):
        self.value0 = 1
        self.value1 = 1
        self.items.reset()
        self.players.reset()

    def set(self, items, players):
        self.items.set(items)
        self.players.set(players)
