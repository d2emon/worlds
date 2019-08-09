from ..database import Database
from ..characters import Characters
from ..items import Items
from .messages import Messages


class WorldData(Database):
    def __init__(self):
        self.messages = Messages()
        self.items = Items()
        self.players = Characters()

    def all(self):
        return {
            'messages': self.messages,
            'items': self.items,
            'players': self.players,
        }

    def get(self, item_id):
        return None

    def reset(self):
        self.messages.reset()
        self.items.reset()
        self.players.reset()

    def set(self, items, players):
        self.items.set(items)
        self.players.set(players)
