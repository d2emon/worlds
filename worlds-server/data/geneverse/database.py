from ..utils import Database
from .thing import Thing


class GeneverseDB(Database):
    @classmethod
    def thing(cls, item):
        return Thing(**item)


