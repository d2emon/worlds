from .models.room import Room
from .database import connect


def find_zone(room_id):
    room = Room.get(room_id)
    return room.zone, room.in_zone


def open_room(room_id, permissions):
    return connect(Room.database_name, permissions).get(room_id)


def show_name(room_id):
    return Room.get(room_id).name
