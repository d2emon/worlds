from ..database import names
from ..globalVars import Globals
from .model import Model
from .character import Character
from .item import Item
from .room_exit import Exit
from .weather import Weather
from .zone import Zone


def room_139(player):
    if any(iswornby(item_id, player.character_id) for item_id in (113, 114, 89)):
        return {'message': "The shield protects you from the worst of the lava stream's heat\n"}
    return {'error': "The intense heat drives you back"}


class Room(Model):
    database_name = names.ROOMS

    DEFAULT_ZONE = Zone()
    ZONES = Zone.all()

    def __init__(
        self,
        room_id,
        title=None,
        exits=(),
        jump_to=None,
        description=None,
        death_room=False,
        no_brief=False,
        is_dark=False,
        outdoors=False,
        climate_id=0,
        zone="TCHAN",
        # permissions="r"
    ):
        super().__init__()
        self.__room_id = room_id
        self.title = title
        self.__exits = exits
        self.jump_to = jump_to
        self.__description = description
        self.death_room = death_room
        self.no_brief = no_brief
        self.is_dark = is_dark
        self.outdoors = outdoors
        self.__zone_name = zone

        self.__zone = None
        self.weather = Weather.get(climate_id) if self.outdoors else None

    @property
    def description(self):
        if self.__description is None:
            return "You are on channel {}\n".format(self.room_id)
        return self.__description

    @property
    def exits(self):
        return [Exit(**data) for data in self.__exits if data is not None]

    @property
    def in_zone(self):
        if self.zone is None:
            return 0
        return self.zone.room_id(self.room_id)

    @property
    def name(self):
        if self.zone is None:
            return None
        zone, in_zone = self.zone.name, self.in_zone
        Globals.wd_there = "{} {}".format(zone, in_zone)
        return "{}{}".format(zone, in_zone)

    @property
    def room_id(self):
        return self.__room_id

    @property
    def zone(self):
        if self.__zone is None:
            self.__zone = Zone.by_name(self.__zone_name)
        return self.__zone

    @property
    def items(self):
        return Item.find(room_id=self.room_id)

    @property
    def characters(self):
        return Character.find(room_id=self.room_id)

    def list_items(self, player):
        def serialize_item(item):
            return {
                'item_id': item.item_id,
                'slug': item.slug,
                'description': item.description,
                'is_destroyed': item.is_destroyed,
            }
        items = list(Item.find(
            wizard=player.is_wizard,
            room_id=self.room_id,
            max_state=3,
            description=True,
        ))
        return {
            'flannel': list(map(serialize_item, Item.list_by_flannel(items, True))),
            'weather': self.weather and self.weather.description,
            'items': list(map(serialize_item, Item.list_by_flannel(items, False))),
        }

    # Events

    @property
    def on_enter(self):
        if self.room_id == -139:
            return room_139
        return lambda player: {}

    def go_direction(self, player, direction_id):
        return self.get(self.exits[direction_id].go(player))


# TODO: Implement


def iswornby(*args):
    # raise NotImplementedError()
    print("iswornby({})".format(args))
    return False
