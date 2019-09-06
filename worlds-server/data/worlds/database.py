from ..utils import Database
from .world import World


class WorldsDB(Database):
    def __init__(
        self,
        items=[],
        loaders=[],
        loader=lambda: [],
    ):
        super().__init__()
        map(self.add, items)
        self.__loaders = loaders
        self.__loader = loader

    @property
    def items(self):
        yield from super().items
        for loader in self.__loaders:
            yield loader()
        for loader in self.__loader():
            yield loader()

    @classmethod
    def world(cls, item):
        return World(**item)

    def all(self):
        return sorted(
            super().all(),
            key=lambda world: world.get('order') or 0,
            reverse=True,
        )
