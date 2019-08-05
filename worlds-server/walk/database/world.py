from .database import Database
from .characters import Characters
from .items import Items


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
