import random
from .generators import data, GeneratorItem


class Item4(GeneratorItem):
    @property
    def negative(self):
        return self.item_id < 15


class Item5(Item4):
    @property
    def negative(self):
        return self.item_id < 20

    @classmethod
    def validate(cls, item, items):
        if item is None:
            return None
        return item.negative == items[4].negative


class Item7(GeneratorItem):
    @property
    def hostile(self):
        if self.item_id < 5:
            return 0
        elif self.item_id < 10:
            return 1
        elif self.item_id < 15:
            return 2
        else:
            return 3


class Item8(Item7):
    @classmethod
    def validate(cls, item, items):
        if item is None:
            return None
        return item.hostile == items[7].hostile


item_ids = range(21)


def random_items(group_id):
    items = [item for item in data if item.generator_id == 'realm' and item.group_id == group_id]

    if group_id == 4:
        item_class = Item4
    elif group_id == 5:
        item_class = Item5
    elif group_id == 7:
        item_class = Item7
    elif group_id == 8:
        item_class = Item8
    else:
        item_class = GeneratorItem

    if len(items) <= 0:
        return None
    return item_class.fill(random.choice(items))
