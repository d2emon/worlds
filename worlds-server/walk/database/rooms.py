from .database import Database


def room_example():
    for _ in range(6):
        yield 0
    yield "Title"
    # Description
    yield "#NOBR"
    yield "Description1"
    yield "Description2"
    yield "Description3"


def load_exits(data):
    return [next(data) for _ in range(6)]


def parse(data):
    room = {
        'title': None,
        'exits': load_exits(data),
        'description': '',
        'death_room': False,
        'no_brief': False,
    }
    for s in data:
        if s == "#DIE":
            room['death_room'] = True
        elif s == "#NOBR":
            room['no_brief'] = True
        elif room['title'] is None:
            room['title'] = s
        else:
            room['description'] += "{}\n".format(s)
    return room


class Rooms(Database):
    def __init__(self):
        super().__init__({
            0: parse(room_example()),
            2: {
                'title': "Title",
                'description': "Description\n",
                'death_room': False,
                'no_brief': True,
            },
        })

    def get(self, item_id):
        return self.all().get(item_id)
