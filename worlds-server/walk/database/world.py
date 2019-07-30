from .database import Database


class WorldData(Database):
    def __init__(self):
        super().__init__({
            'items': [],
            'players': [],
        })

    def get(self, item_id):
        return self.all().get(item_id)
