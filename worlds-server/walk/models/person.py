from .model import RequestModel


class Person(RequestModel):
    _URL = "http://worlds_walker_1:5000/api/person"

    def __init__(
        self,
        person_id=None,
        strength=0,
        level=0,
        flags=None,
        score=0,
    ):
        self.person_id = person_id
        self.strength = strength
        self.level = level
        self.flags = flags or []
        self.score = score

    @classmethod
    def _parse_response(cls, data):
        return data.get('person')

    def serialize(self):
        return {
            'person_id': self.person_id,
            'strength': self.strength,
            'score': self.score,
            'level': self.level,
            'flags': self.flags,
        }

    @classmethod
    def get(cls, item_id):
        person = cls._get("{}/{}".format(cls._URL, item_id))
        return cls(**person) if person is not None else None

    def save(self):
        self._put("{}/{}".format(self._URL, self.person_id), self.serialize())
        return self

    @classmethod
    def load(cls, player, new_player):
        person_id = player.name.lower()

        person = cls.get(person_id)
        if person is not None:
            return person

        player = new_player()
        person = cls(
            person_id=person_id,
            strength=player.strength,
            level=player.level,
            flags=[player.sex],
            score=player.score,
        )
        return person.save()

    @classmethod
    def remove(cls, person_id):
        return cls._delete("{}/{}".format(cls._URL, person_id))


