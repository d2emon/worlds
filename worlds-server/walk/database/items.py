from .database import ListDatabase


class Items(ListDatabase):
    ITEMS = 194

    def __init__(self):
        super().__init__([self.item(item_id) for item_id in range(self.ITEMS)])

    @classmethod
    def __item_data(cls, item_id):
        return {
            'item_id': item_id,
            # Item Data
            'name': '',
            'description': (),
            'max_state': 0,
            'flannel': False,
            'base_value': 0,
            # World Item
            'location': 0,
            # 1-2
            'carry_flag': 0,
        }

    @classmethod
    def item(cls, item_id):
        return cls.__item_data(item_id)

    def set(self, items):
        self.items = items
