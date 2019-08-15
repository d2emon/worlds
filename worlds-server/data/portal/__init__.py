from .portal import item_ids, random_items


# Generators
def __get_item(item_id, items, forbidden=()):
    item = random_items(item_id)
    if item is None:
        return None
    elif not item.validate(item, items):
        return None
    elif item in forbidden:
        return None
    else:
        return item


def __next_item(item_id, items, forbidden=()):
    while True:
        item = __get_item(item_id, items, forbidden)
        if item is not None:
            return item


def __next_items(item_id, items, count):
    item = []
    for _ in range(count):
        item.append(__next_item(item_id, items, item))
    return item


def __get_text(item):
    if item is None:
        return None
    if isinstance(item, list):
        return [str(i) for i in item]
    return str(item)


def generate():
    items = [None]
    for i in item_ids:
        item_id = i + 1
        item = None
        while item is None:
            if item_id in (17, 20):
                item = __next_items(item_id, items, 3)
                # item = []
                # for _ in range(3):
                #     item.append(__next_item(item_id, items, item))
            else:
                item = __next_item(item_id, items)
        items.append(item)

    return [__get_text(item) for item in items]


# Classes
class World:
    def __init__(self, world_type=None, world_description=None, n6=None):
        names = generate()
        self.world_type = world_type or names[4]
        self.__description = world_description or names[5]
        self.__n6 = n6 or names[6]

    @property
    def name(self):
        return "{} мир".format(self.world_type)

    @property
    def description(self):
        return "{} {}.".format(self.__description, self.__n6)


class Portal:
    def __init__(self, portal_type=None, placement=None, world=None):
        names = generate()
        self.portal_type = portal_type or names[2]
        self.placement = placement or names[3]
        self.world = world or World()

    @property
    def name(self):
        return "{} портал".format(self.portal_type)

    @property
    def description(self):
        return "{}, {}".format(self.name, self.placement)

    def move(self, movement):
        return "Вы {} {}. За ним вас встречает {}. {}".format(
            movement,
            self.description,
            self.world.name,
            self.world.description,
        )


def description():
    names = generate()

    movement = names[1]
    world = World(names[4], names[5], names[6])
    p = Portal(names[2], names[3], world)

    text = "".join([
        p.move(names[1]),
        "\n",
        "{names[7]}{names[8]}. Этот мир {names[9]}{names[10]}.",
        "\n",
        "{names[11]} вам {names[12]} о {names[13]}. {names[14]}, {names[15]}. ",
        "{names[16]} {names[17][0]} существа, {names[17][1]} существа, ",
        "и что-то похожее на каких-то {names[17][2]} существ.",
        "\n",
        "{names[18]} как {names[19]}. ",
        "Но с {names[20][0]}, {names[20][1]}, и {names[20][2]}, {names[21]}. ",
    ])
    return text.format(
        movement=movement,
        portal=p,
        names=names,
    ).replace("\n", "\n\n")
