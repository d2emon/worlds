class Person:
    __records = {}

    def __init__(
        self,
        player_id=None,
        strength=0,
        level=0,
        flags=None,
        score=0,
    ):
        self.player_id = player_id
        self.strength = strength
        self.level = level
        self.flags = flags or []
        self.score = score

    def as_dict(self):
        return {
            'player_id': self.player_id,
            'strength': self.strength,
            'score': self.score,
            'level': self.level,
            'flags': self.flags,
        }

    def save(self):
        record = self.__records.get(self.player_id)
        self.player_id = record.player_id if record else len(self.__records)
        self.__records[self.player_id] = self
        return self

    @classmethod
    def load(cls, player, on_create):
        person = cls.__records.get(player.name)
        if person is not None:
            return person.as_dict()

        player = on_create()
        return cls(
            player_id=player.name,
            strength=player.strength,
            level=player.level,
            flags=[player.sex],
            score=player.score,
        ).save().as_dict()

    @classmethod
    def remove(cls, player_id):
        name = player_id.lower()
        record = cls.__records.get(player_id)
        if record is None:
            return
        if record.name.lower() != name:
            raise StopGame("Panic: Invalid Persona Delete")
        record.name = ""
        record.level = -1


