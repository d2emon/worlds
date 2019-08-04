from .database import Database, WorldDatabase
from .characters import Characters


class Items(WorldDatabase):
    ITEMS = 194


class WorldData(Database):
    def __init__(self):
        self.items = Items()
        self.players = Characters()

    def all(self):
        return (
            self.items,
            self.players,
        )

    def get(self, item_id):
        return None

    def set(self, items, players):
        self.items.set(items)
        self.players.set(players)
