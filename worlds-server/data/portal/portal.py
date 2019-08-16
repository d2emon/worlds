import random
from .generators import data, GeneratorItem as BaseGeneratorItem


class GeneratorItem(BaseGeneratorItem):
    @property
    def hostile(self):
        return None

    @property
    def negative(self):
        return None


class Movement(GeneratorItem):
    pass


class PortalType(GeneratorItem):
    pass


class PortalDescription(GeneratorItem):
    pass


class WorldType(GeneratorItem):
    @property
    def negative(self):
        return self.item_id <= 15


# 5, 6
class WorldDescription(WorldType):
    @property
    def negative(self):
        return self.item_id <= 19

    @classmethod
    def validate(cls, item, items):
        if item is None:
            return None
        return item.negative == items[4].negative


class Feeling1(GeneratorItem):
    @property
    def hostile(self):
        if self.item_id <= 5:
            return 0
        elif self.item_id <= 10:
            return 1
        elif self.item_id <= 15:
            return 2
        else:
            return 3


class Feeling2(Feeling1):
    @classmethod
    def validate(cls, item, items):
        if item is None:
            return None
        return item.hostile == items[7].hostile


class Summary1(GeneratorItem):
    @property
    def negative(self):
        return self.item_id <= 10

    @classmethod
    def validate(cls, item, items):
        if item is None:
            return None
        return item.negative == items[4].negative


class Summary2(Summary1):
    @classmethod
    def validate(cls, item, items):
        if item is None:
            return None
        return item.negative == items[9].negative


item_ids = range(21)
item_classes = {
    1: Movement,
    2: PortalType,
    3: PortalDescription,
    4: WorldType,
    5: WorldDescription,
    6: WorldDescription,
    7: Feeling1,
    8: Feeling2,
    9: Summary1,
    10: Summary2,
}


def random_items(group_id):
    items = [item for item in data if item.generator_id == 'realm' and item.group_id == group_id]
    item_class = item_classes.get(group_id, GeneratorItem)
    return item_class.fill(random.choice(items)) if len(items) > 0 else None


def list_data():
    for group_id in item_ids:
        items = [item for item in data if item.generator_id == 'realm' and item.group_id == group_id]
        item_class = item_classes.get(group_id, GeneratorItem)
        for item in items:
            i = item_class.fill(item)
            s = i.serialize()
            s.update({
                'hostile': i.hostile,
                'negative': i.negative,
            })
            # print(s)


list_data()
