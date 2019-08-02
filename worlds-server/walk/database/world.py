from .database import Database, ListDatabase


class WorldDatabase(ListDatabase):
    ITEMS = 0

    def __init__(self):
        super().__init__([item_id for item_id in range(self.ITEMS)])

    def set(self, items):
        self.items = items


class Items(WorldDatabase):
    ITEMS = 194


class Players(WorldDatabase):
    ITEMS = 48


class WorldData(Database):
    def __init__(self):
        self.items = Items()
        self.players = Players()

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
