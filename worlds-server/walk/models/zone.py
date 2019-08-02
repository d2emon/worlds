from ..database import names
from .model import Model


class Zone(Model):
    database_name = names.ZONES

    def __init__(
        self,
        name="TCHAN",
        begin=None,
        end=0
    ):
        super().__init__()
        self.name = name
        self.begin = begin
        self.end = end + 1

    @classmethod
    def by_room_id(cls, room_id):
        if room_id > 0:
            return cls()
        return cls(**cls.database().by_room_id(room_id))

    def room_id(self, room_id):
        return 0 if self.begin is None else (-room_id) - self.begin
