from .database import Database, ListDatabase


class WorldDatabase(ListDatabase):
    def __init__(self):
        super().__init__([])

    def set(self, items):
        self.items = items


class Items(WorldDatabase):
    NOBS = 194


class Players(WorldDatabase):
    pass


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
