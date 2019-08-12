import random


class BaseItem:
    GENERATOR_DATA = ()

    def __init__(self, name=None):
        self.name = name or self.__class__.__name__
        self.__items = None

    @classmethod
    def set_count(cls, min_count=1, max_count=None):
        def f():
            if max_count is None:
                count = min_count
            else:
                count = random.randint(min_count, max_count)
            return [cls() for _ in range(count)]
        return f

    @classmethod
    def set_probability(cls, probability=100):
        return lambda: [cls()] if random.uniform(0, 100) < probability else []

    @classmethod
    def get_factories(cls):
        return cls.GENERATOR_DATA

    @classmethod
    def items_generator(cls):
        items = [factory() for factory in cls.get_factories()]
        for item in items:
            if isinstance(item, BaseItem):
                yield item
            yield from item

    @property
    def items(self):
        if self.__items is None:
            self.__items = list(self.items_generator())
        return self.__items

    def get_items(self, item_class):
        return (item for item in self.items if isinstance(item, item_class))
