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
class Creatures:
    def __init__(
        self,
        creature_type=None,
        signals=None,
    ):
        names = generate()
        self.creature_type = creature_type or names[13]
        self.signals = signals or names[12]

    def detect(self, distance):
        return "{} вы {} {}.".format(
            distance,
            self.signals,
            self.creature_type,
        )


class World:
    def __init__(
        self,
        world_type=None,
        world_description=None,
        feelings=None,
        summary=None,

        creature_types=None,
        creature_signals=None,
    ):
        names = generate()
        self.world_type = world_type or names[4]
        self.__description = world_description or names[5:7]
        self.__feelings = feelings or names[7:9]
        self.__summary = summary or names[9:11]
        self.creatures = Creatures(
            creature_types,
            creature_signals,
        )

    @property
    def name(self):
        return "{} мир".format(self.world_type)

    @property
    def feelings(self):
        return "".join(self.__feelings) + "."

    @property
    def summary(self):
        return "Этот мир {}.".format("".join(self.__summary))

    @property
    def description(self):
        return "\n".join((
            " ".join(self.__description),
            " ".join((
                self.feelings,
                self.summary
            )),
        ))


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

    def move(self, movement, distance):
        return "Вы {} {}. За ним вас встречает {}. {}\n{}".format(
            movement,
            self.description,
            self.world.name,
            self.world.description,
            self.world.creatures.detect(distance),
        )


def description():
    names = generate()

    movement = names[1]
    world = World(
        names[4],
        names[5:7],
        names[7:9],
        names[9:11],
        names[13],
        names[12],
        # names[14:17],
    )
    p = Portal(names[2], names[3], world)

    text = "".join([
        p.move(names[1], names[11]),
        "\n",
        "{names[11]} вы {names[12]} {names[13]}. {names[14]} {names[15]}. ",
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
