import uuid
from .model import Model


class Person(Model):
    def __init__(
        self,
        person_id=None,
        name=None,
        strength=0,
        level=0,
        flags=None,
        score=0,
    ):
        self.person_id = person_id or uuid.uuid4()
        self.name = name
        self.strength = strength
        self.level = level
        self.flags = flags or []
        self.score = score

        super().__init__()

    @property
    def id(self):
        return self.name

    @property
    def _item(self):
        return next((item for item in self._items() if item.get('name') == self.name), None)

    def serialize(self):
        return {
            'person_id': self.person_id,
            'name': self.name,
            'strength': self.strength,
            'score': self.score,
            'level': self.level,
            'flags': self.flags,
        }

    @classmethod
    def _items(cls):
        return DATA


DATA = []
