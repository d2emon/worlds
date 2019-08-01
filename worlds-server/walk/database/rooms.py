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
            5: parse(iter((
                0, 0, -623, 0, 0, 0,
                "The Temple Of Paradise",
                "You stand in the temple of paradise, a huge stone structure whose walls",
                "are decorated with ancient carvings and runes, some so old that even the ",
                "priests no longer know their meanings. ",
                "",
                "A single set of steps lead south descending the huge mound upon which",
                "the temple is built into the forests below.",
                "",
                "At your feet a huge sacrificial pit allows you to give valuables to the",
                "gods in the hope of being rewarded.",
            ))),
            182: parse(iter((
                -183, -184, -187, -181, 0, 0,
                "The Village Green",
                "You are standing on a square of grass in the centre of the village.",
                "A cottage stands to the east surrounded by gently swaying trees.",
                "",
                "To the north is a small church, and a path leads west into the trees."
            ))),
            183: parse(iter((
                0, 0, -182, 0, 0, 0,
                "The Village Church",
                "You are in the villages small wooden church. A gentle breeze blows into",
                "the church disturbing the dust which dances in the sunbeams that shine faintly",
                "through the windows. A doorway leads south.",
                "",
                "There is a sacrificial pit in the floor into which you can drop items",
                "in search of blessings from the gods.",
            ))),
        })

    def get(self, item_id):
        return self.all().get(item_id)
