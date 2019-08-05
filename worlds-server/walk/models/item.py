import random
from ..database import World
from ..globalVars import Globals
from .model import Model


class Item(Model):
    def __init__(
        self,
        item_id,
        name='',
        description=(),
        max_state=0,
        flannel=False,
        base_value=0,
        location=0,
        carry_flag=0,
    ):
        super().__init__()
        self.item_id = item_id

        self.__name = name
        self.__description = description
        self.__max_state = max_state
        self.__flannel = flannel
        self.__base_value = base_value

        self.__location = location
        self.__carry_flag = carry_flag

    @classmethod
    def database(cls):
        return World.instance.items

    @classmethod
    def count(cls):
        return cls.database().ITEMS

    @property
    def description(self):
        return self.__description[state(self.item_id)]

    @property
    def flannel(self):
        return self.__flannel

    @property
    def name(self):
        return self.__name

    @classmethod
    def by_flannel(cls, flannel):
        for item_id in cls.database().all():
            item = cls(item_id=item_id)
            if not ishere(item_id) or item.__flannel != flannel:
                continue
            if state(item_id) > 3:
                continue
            result = {
                'item_id': item.item_id,
                'text': item.description
            }
            if len(item.description) <= 0:
                continue
            # OLONGT NOTE TO BE ADDED
            Globals.wd_it = item.name
            result.update({'destroyed': isdest(item_id)})
            yield result

    @classmethod
    def list_items(cls):
        # yield from cls.by_flannel(True)
        yield showwthr()
        # yield from cls.by_flannel(False)

    @property
    def location(self):
        return self.__location

    @property
    def carried_by(self):
        if self.__carry_flag not in (1, 2):
            return None
        return self.location

    @property
    def owner(self):
        if self.__carry_flag not in (0, 3):
            return None
        return self.location

    def set_location(self, location, carry_flag):
        self.__location = location
        self.__carry_flag = carry_flag


def by_flannel(flannel):
    return Item.by_flannel(flannel)


def list_items():
    return Item.list_items()


# TODO: Implement


def isdest(*args):
    # raise NotImplementedError()
    print("isdest({})".format(args))
    return random.randrange(100) > 50


def ishere(*args):
    # raise NotImplementedError()
    print("ishere({})".format(args))
    return True


def showwthr(*args):
    # raise NotImplementedError()
    print("showwthr({})".format(args))
    return {}


def state(*args):
    # raise NotImplementedError()
    print("state({})".format(args))
    return 1
