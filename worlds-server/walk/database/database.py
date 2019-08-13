class Database:
    def all(self):
        raise NotImplementedError

    def get(self, item_id):
        raise NotImplementedError


class ListDatabase(Database):
    def __init__(self):
        self.items = list(self.reset())

    def all(self):
        yield from self.items

    def set_all(self, items):
        self.items = items

    def get(self, item_id):
        return lambda: self.items[item_id]

    def set(self, index, **data):
        self.items[index].update(data)

    def reset(self):
        raise NotImplementedError


class WorldDatabase(ListDatabase):
    ITEMS = 0

    def set_all(self, items):
        self.items = items

    def reset(self):
        yield from range(self.ITEMS)
