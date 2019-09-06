from ..utils import ListDatabase
from .thing import Thing


class GeneverseDB(ListDatabase):
    @classmethod
    def thing(cls, item):
        return Thing(**item)


