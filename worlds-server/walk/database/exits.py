from .database import Database


class Exits(Database):
    def all(self):
        yield None

    def get(self, item_id):
        return lambda: None

    @classmethod
    def parse(cls, room_id, data):
        return cls.by_room(room_id, (int(next(data)) for _ in range(6)))

    @classmethod
    def by_room(cls, room_from, exits):
        return ({
            'direction_id': direction_id,
            'room_from': room_from,
            'room_to': room_to,
        } for direction_id, room_to in enumerate(exits))
