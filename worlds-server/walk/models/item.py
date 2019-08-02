import random
from ..database import World
from ..globalVars import Globals
from .model import Model


class Item(Model):
    def __init__(
        self,
        item_id,
    ):
        super().__init__()
        self.item_id = item_id

    @classmethod
    def database(cls):
        return World.instance.items

    @property
    def description(self):
        text = olongt(self.item_id, state(self.item_id))
        # if Globals.debug_mode:
        #     return "{{{}}} {}\n".format(item_id, text)
        # elif len(text):
        #     return "{}\n".format(text)
        return {
            'item_id': self.item_id,
            'text': text,
        }

    @classmethod
    def by_flannel(cls, flannel):
        for item_id in range(cls.database().NOBS):
            item = cls(item_id=item_id)
            if not ishere(item_id) or oflannel(item_id) != flannel:
                continue
            if state(item_id) > 3:
                continue
            if len(olongt(item_id, state(item_id))) <= 0:
                continue
            # OLONGT NOTE TO BE ADDED
            Globals.wd_it = oname(item_id)
            result = item.description
            result.update({'destroyed': isdest(item_id)})
            yield result

    @classmethod
    def list_items(cls):
        yield from cls.by_flannel(True)
        yield showwthr()
        yield from cls.by_flannel(False)


def by_flannel(flannel):
    return Item.by_flannel(flannel)


def list_items():
    return Item.list_items()


# Not Implemented


def isdest(*args):
    # raise NotImplementedError()
    print("isdest({})".format(args))
    return random.randrange(100) > 50


def ishere(*args):
    # raise NotImplementedError()
    print("ishere({})".format(args))
    return True


def oflannel(*args):
    # raise NotImplementedError()
    print("oflannel({})".format(args))
    return random.randrange(100) > 50


def olongt(*args):
    # raise NotImplementedError()
    print("olongt({})".format(args))
    return "TEXT"


def oname(*args):
    # raise NotImplementedError()
    print("oname({})".format(args))
    return "TEXT"


def showwthr(*args):
    # raise NotImplementedError()
    print("showwthr({})".format(args))
    return {}


def state(*args):
    # raise NotImplementedError()
    print("state({})".format(args))
    return 1
