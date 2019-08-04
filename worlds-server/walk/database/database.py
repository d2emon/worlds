class Database:
    def all(self):
        raise NotImplementedError

    def get(self, item_id):
        raise NotImplementedError


class ListDatabase(Database):
    def __init__(self, items):
        self.items = items

    def all(self):
        yield from self.items

    def get(self, item_id):
        return lambda: self.items[item_id]


class WorldDatabase(ListDatabase):
    ITEMS = 0

    def __init__(self):
        super().__init__([item_id for item_id in range(self.ITEMS)])

    def set(self, items):
        self.items = items
