from .database import ListDatabase
from .logger import logger


class Items(ListDatabase):
    ITEMS = 194
    __ITEMS_DATA = (
        ("SYS$WEATHER", "The Weather", "", "", "", 1, 0, 4),
        ("umbrella", "A furled umbrella lies here", "An unfurled umbrella lies here", "", "", 1, 30, 0),
        (
            "shelf",
            "A wooden shelf on the north wall looks as if it once held many ancient tomes\n"
            "There is a small opening in the north wall.",
            "A wooden shelf on the north wall looks as if it once held many ancient tomes",
            "", "", 1, 0, 1
        ),
        ("panel", "A small wooden panel is open in the southern wall", "", "", "", 1, 0, 1),
        (
            "candle",
            "A red candle burns here, emitting a soft flickering flame",
            "There is a red candle here",
            "", "", 1, 20, 0
        ),
        (
            "candle",
            "A blue candle burns here, emitting a soft flickering flame",
            "There is a blue candle here",
            "", "", 1, 20, 0
        ),
        (
            "candle",
            "A green candle burns here, emitting a soft flickering flame",
            "There is a green candle here",
            "", "", 1, 20, 0
        ),
        (
            "ball",
            "A crystal ball has been placed here",
            "A crystal ball has been placed here, glowing a pale red",
            "A crystal ball has been placed here, glowing a pale blue",
            "A crystal ball has been placed here, glowing a pale green",
            3, 20, 0
        ),
        ("scroll", "A tattered scroll lies at your feet", "", "", "", 0, 20, 0),
        ("runes", "Some mysterious runes are etched on the wall", "", "", "", 1, 0, 1),

        # 10
        (
            "candlestick",
            "A hefty gold candlestick lies here, a candle flickering brightly within it",
            "A hefty gold candlestick lies here, with a candle in it",
            "A hefty gold candlestick lies here",
            "", 2, 100, 0
        ),
        ("cauldron", "A large cauldron bubbles away before you", "", "", "", 1, 0, 1),
        (
            "fire",
            "A large fire blazes away in one corner",
            "The ashes of a fire smoulder in a corner",
            "", "", 1, 0, 1
        ),
        ("wand", "A short slender wand lies here", "", "", "", 0, 0, 0),
        (
            "ball",
            "A ball of light floats in the centre of the room",
            "The centre of the room is filled with an expanding ball of light",
            "The room is filled with an expanding ball of light",
            "", 3, 0, 1
        ),
        ("coins", "Some coins lie piled up in a heap on the floor", "", "", "", 0, 100, 0),
        ("staff", "A long runed staff lies here, etched with strange markings", "", "", "", 0, 400, 0),
        ("orb", "A small gold orb has been left here", "", "", "", 0, 50, 0),
        ("ring", "A small gold ring has been dropped here", "", "", "", 0, 100, 0),
        ("sceptre", "A large silver sceptre has been placed here", "", "", "", 0, 100, 0),

        # 20
        (
            "door",
            "The door to the north is open",
            "The door to the north is closed",
            "The door to the north is locked",
            "", 2, 0, 1
        ),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("book", "There is a large mystical looking book here", "A large book rests on the shelf", "", "", 1, 30, 0),
        ("hole", "There is a small hole carved into the south wall", "", "", "", 1, 0, 1),
        ("torch", "A battered torch hangs on the south wall", "", "", "", 1, 0, 1),
        ("key", "A small brass key has been left here", "", "", "", 0, 0, 0),
        ("door", "There is a small door open in the south wall", "", "", "", 1, 0, 1),
        ("door", "The door is open", "The door is closed", "", "", 1, 0, 1),
        (
            "portcullis",
            "The Portcullis is raised.",
            "The heavy iron portcullis bars the way north",
            "", "", 1, 0, 1
        ),
        (
            "portcullis",
            "A raised portcullis allows access south",
            "A heavy iron portcullis bars the way south",
            "", "", 1, 0, 1
        ),

        # 30
        ("lever", "There is a large iron lever on the east wall", "", "", "", 0, 0, 1),
        ("horseshoe", "An old horseshoe lies nearby", "", "", "", 0, 10, 0),
        (
            "sword",
            "A huge sword has been left here, its blade black and strangely pulsing with\n"
            "light",
            "A huge sword stands upright before you, imbedded in the solid stone floor",
            "", "", 1, 500, 0
        ),
        ("shortsword", "A sharp shortsword has been dropped here", "", "", "", 0, 10, 0),
        ("dagger", "A small dagger has been dropped here", "", "", "", 0, 10, 0),
        ("knife", "A short sharp knife has been left here, probably lobbed by some dwarf", "", "", "", 0, 20, 0),
        ("maiden", "The iron maiden is open", "The iron maiden is closed", "", "", 1, 0, 1),
        ("maiden", "The iron maiden is open", "The iron maiden is closed", "", "", 1, 0, 1),
        (
            "throne",
            "A huge gleaming throne is set against the south wall, beside a narrow escape\n"
            "tunnel",
            "A huge gleaming throne is set against the south wall",
            "", "", 1, 0, 1
        ),
        (
            "throne",
            "A small hole leads north into the hall",
            "The exit north is blocked by the back of a throne",
            "", "", 1, 0, 1
        ),

        # 40
        ("bagpipes", "A set of bagpipes lies here, waiting to be played", "", "", "", 0, 50, 0),
        ("sporran", "A sporran has been dumped here", "", "", "", 0, 20, 0),
        (
            "claymore",
            "A wicked looking claymore, decorated with silver wire lies at your feet.",
            "", "", "", 0, 300, 0
        ),
        ("bat", "A dead bat decays slowly in a corner", "", "", "", 0, 10, 0),
        (
            "rose",
            "A small but beautiful rose has been left here, slowly wilting away",
            "A beautiful rose grows in amongst the trees",
            "", "", 1, 40, 0
        ),
        ("cross", "A hefty gold cross lies sparkling before you!", "", "", "", 0, 200, 0),
        ("lead", "A neat pile of roofing lead has been left stacked in a corner", "", "", "", 0, 100, 0),
        ("weathercock", "A golden weathercock has been left here, somewhat out of order", "", "", "", 0, 50, 0),
        ("pitcher", "A small stone pitcher has been placed here", "", "", "", 0, 10, 0),
        ("rope", "", "", "", "", 0, 0, 1),

        # 50
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("warhammer", "A large, and heavy looking warhammer has been left here", "", "", "", 0, 50, 0),
        ("coin", "A small silver coin has been dropped here", "", "", "", 0, 20, 0),

        # 60
        ("ale", "A large bottle of strong ale has been left here", "", "", "", 0, 40, 0),
        ("biscuit", "A hard biscuit has been dropped here", "", "", "", 0, 20, 0),
        ("gates", "The dwarven gates are open", "The dwarven gates are closed", "", "", 1, 0, 1),
        ("gates", "The dwarven gates are open", "The dwarven gates are closed", "", "", 1, 0, 1),
        ("cutlery", "Some gold cutlery has been left here", "", "", "", 0, 75, 0),
        ("plate", "A silver plate has been left here", "", "", "", 0, 75, 0),
        ("crystal", "A beautiful, well cut crystal glints in front of you", "", "", "", 0, 100, 0),
        (
            "axe",
            "A small axe, marked with the words 'if found please return to thrower', lies\n"
            "before you",
            "", "", "", 0, 50, 0
        ),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),

        # 70
        ("pepper", "Some pepper has been left here", "", "", "", 0, 30, 0),
        ("ruby", "A huge ruby sparkles at your feet", "", "", "", 0, 250, 0),
        ("sapphire", "A massive sapphire glitters stunningly before you", "", "", "", 0, 250, 0),
        ("diamond", "There is a huge diamond on the floor in front of you", "", "", "", 0, 500, 0),
        ("fire", "A huge fire burns here, its flames making the temple sparkle and glitter", "", "", "", 0, 0, 1),
        ("spring", "", "", "", "", 1, 0, 0),
        ("branch", "A burning branch lies here", "An old branch lies here", "", "", 1, 1, 0),
        ("stick", "A burning stick has been left here", "An old stick lies here", "", "", 1, 0, 0),
        ("plank", "A burning plank has been left here", "An old plank lies here", "", "", 1, 0, 0),
        ("fountain", "", "", "", "", 1, 0, 0),

        # 80
        ("potion", "A potion of restore strength lies here", "", "", "", 0, 250, 0),
        ("crown", "A beautiful gold crown lies here", "", "", "", 0, 400, 0),
        ("key", "A long key lies here", "", "", "", 0, 10, 0),
        ("loaf", "A fairly stale, but edible loaf has been left here", "", "", "", 0, 10, 0),
        ("pie", "A cold but fairly fresh rabbit pie has been put here", "", "", "", 0, 10, 0),
        ("bed", "", "", "", "", 0, 0, 1),
        (
            "apple",
            "A large juicy apple lies temptingly before you",
            "A large apple hangs from a tree branch",
            "", "", 0, 40, 0
        ),
        ("waybread", "Some waybread has been put here", "", "", "", 0, 50, 0),
        ("waybread", "Some waybread has been put here", "", "", "", 0, 50, 0),
        ("shield", "A small shield has been left here", "", "", "", 0, 100, 0),

        # 90
        ("amulet", "An unadorned gold amulet has been put here", "", "", "", 0, 50, 0),
        ("bedding", "", "", "", "", 0, 0, 1),
        ("hammer", "A large hammer has been left around here for some reason", "", "", "", 0, 10, 0),
        ("rock", "A small rock has been dropped here", "", "", "", 0, 1, 0),
        ("gem", "A small uncut gem lies before you", "", "", "", 0, 100, 0),
        ("pick", "An old pick has been dumped here", "", "", "", 0, 10, 0),
        ("ale", "A skin of ale has been dropped here", "", "", "", 0, 10, 0),
        ("sandwiches", "Some sandwiches have been put here", "", "", "", 0, 10, 0),
        ("nugget", "A gold nugget twinkles before you", "", "", "", 0, 50, 0),
        ("nugget", "A gold nugget twinkles before you", "", "", "", 0, 200, 0),

        # 100
        ("garlic", "чеснок", "У ваших ног лежит чеснок, вы чувствуете его запах", "", "", "", 0, 10, 0),
        (
            "robe",
            "A black robe with two silver lightning bolts down the back has been put here",
            "", "", "", 0, 10, 0
        ),
        ("rations", "Some rations have been left here, old but edible", "", "", "", 0, 10, 0),
        ("rations", "Some old rations have been left here", "", "", "", 0, 10, 0),
        (
            "statue",
            "A huge stone statue of a sorceror stands here, beside a hole leading down",
            "A huge stone statue of a sorceror stands proudly against the north wall",
            "", "", 1, 0, 1
        ),
        (
            "statue",
            "There is a hole in the roof above you",
            "There is a hole in the roof above you but it is blocked by the statue's base",
            "", "", 1, 0, 1
        ),
        ("robe", "A black robe has been neatly folded and left here", "", "", "", 0, 10, 0),
        ("key", "A small silver key has been dropped here", "", "", "", 0, 50, 0),
        ("soap", "Some soap has been dropped here", "", "", "", 0, 20, 0),
        ("broom", "An old broom has been left here", "", "", "", 0, 20, 0),

        # 110
        (
            "coffin",
            "An ornate coffin is set in the centre of the room. The coffin is open",
            "An ornate coffin is set in the centre of the room.",
            "", "", 1, 0, 1
        ),
        ("powerstone", "A magical powerstone has been put here by someone", "", "", "", 0, 100, 0),
        ("shield", "", "", "", "", 0, 0, 1),
        ("shield", "A heavy painted shield has been dropped here", "", "", "", 0, 30, 0),
        ("shield", "A small wooden shield has been put here", "", "", "", 0, 20, 0),
        ("runes", "", "", "", "", 0, 0, 1),
        ("obsidian", "A large gleaming piece of obsidian lies on the ground", "", "", "", 0, 100, 0),
        ("pumice", "A piece of pumice has been discarded here", "", "", "", 0, 100, 0),
        ("panel", "A small panel is open in the east wall", "", "", "", 1, 0, 1),
        ("sack", "A very large sack has been left here", "", "", "", 0, 30, 0),

        # 120
        ("rod", "A carved ebony rod floats in front of you, humming quietly", "", "", "", 0, 200, 0),
        ("powerstone", "A magical powerstone has been placed here", "", "", "", 0, 100, 0),
        (
            "pillar",
            "A huge stone pillar bridges the gap and allows you to go east",
            "A huge stone pillar lies fallen on the floor",
            "", "", 1, 0, 1
        ),
        ("pillar", "A huge stone pillar bridges the gap to the west", "", "", "", 1, 0, 1),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("tripwire", "There is a tripwire stretched out across the passage", "", "", "", 0, 0, 1),
        ("knife", "A small curved surgeons knife has been dropped here", "", "", "", 0, 20, 0),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),
        ("door", "The door is open", "The door is closed", "The door is locked", "", 2, 0, 1),

        # 130
        ("bar", "An iron bar is set into wall", "", "", "", 0, 0, 1),
        ("boulder", "A huge boulder rests against one of the walls", "", "", "", 0, 0, 1),
        ("passage", "A secret passage leads eastwards.", "", "", "", 1, 0, 1),
        ("passage", "A secret passage leads westwards.", "", "", "", 1, 0, 1),
        ("hole", "A hole allows you to clamber eastwards.", "", "", "", 1, 0, 1),
        ("hole", "A hole allows you to go west.", "", "", "", 1, 0, 1),
        ("wand", "A long red wand has been placed here.", "", "", "", 0, 100, 0),
        (
            "pit",
            "There is a pit in the floor",
            "There is a pit of slime in the floor",
            "A HUGE mass of green slime pulsates and bubbles in front of you",
            "", 2, 0, 1
        ),
        ("lever", "A heavy iron lever is set into the south wall", "", "", "", 0, 0, 1),
        ("garland", "A beautiful garland of flowers sends a sweet smell wafting around you", "", "", "", 0, 100, 0),

        # 140
        ("grille", "The grille is open.", "The grille is closed.", "", "", 1, 0, 1),
        ("grille", "The grille is open.", "The grille is closed.", "", "", 1, 0, 1),
        ("coins", "A few coins lie scattered on the ground.", "", "", "", 0, 20, 0),
        ("necklace", "A beautiful necklace has been left here", "", "", "", 0, 200, 0),
        ("tube", "A long ivory scroll tube has been dropped here", "", "", "", 0, 50, 0),
        ("scroll", "A battered papyrus scroll has been dropped here", "", "", "", 0, 100, 0),
        (
            "curtains",
            "A narrow passage leads north, through a gap in the curtains",
            "The curtains are closed",
            "", "", 1, 0, 1
        ),
        (
            "curtains",
            "To the south the passage leads into a curtained hall",
            "To the south the passage passes through some curtains",
            "", "", 1, 0, 1
        ),
        ("harp", "A beautiful golden harp has been placed here", "", "", "", 0, 300, 0),
        ("lever", "", "", "", "", 0, 0, 1),

        # 150
        ("bridge", "A huge iron drawbridge crosses the lava, and leads west", "", "", "", 0, 0, 1),
        ("bridge", "A huge iron drawbridge crosses the lava to the east", "", "", "", 0, 0, 1),
        ("bridge", "A crystal bridge leads south across the pool", "", "", "", 1, 0, 1),
        ("bridge", "A crystal bridge leads north across the pool", "", "", "", 1, 0, 1),
        ("picture", "", "", "", "", 0, 0, 1),
        ("fire", "", "", "", "", 0, 0, 1),
        ("orb", "A glowing white orb pulsates before you", "", "", "", 0, 300, 0),
        ("moonstone", "A huge moonstone lies in front of you", "", "", "", 0, 200, 0),
        ("rod", "A black rod marked with a red pentacle has been placed here", "", "", "", 0, 150, 0),
        ("talisman", "A battered silver talisman has been dumped here", "", "", "", 0, 100, 0),

        # 160
        ("giant", "A giant snores loudly in one corner", "", "", "", 0, 0, 1),
        ("robe", "A rather worn robe lies here tatty and fraying", "", "", "", 0, 10, 0),
        ("bookcase", "", "", "", "", 0, 0, 1),
        ("powerstone", "A magical powerstone has been placed here", "", "", "", 0, 100, 0),
        ("book", "A heavy iron bound book has been left here", "", "", "", 0, 200, 0),
        ("well", "", "", "", "", 0, 0, 1),
        ("fire", "A huge fire burns in the centre of the room", "", "", "", 0, 0, 1),
        ("branch", "A burning branch has been left here", "An old branch has been dropped here", "", "", 0, 0, 0),
        ("poker", "A heavy iron poker has been left here", "", "", "", 0, 10, 0),
        ("pick", "A small but well made ice pick has been dropped here", "", "", "", 0, 20, 0),

        # 170
        ("stick", "A burning stick lies on the ground", "An old stick lies on the ground", "", "", 1, 10, 0),
        ("stone", "", "", "", "", 0, 0, 1),
        ("scimitar", "A long curved scimitar has been placed here", "", "", "", 0, 30, 0),
        ("bag", "A small bag has been dumped in one corner", "", "", "", 0, 20, 0),
        ("pendant", "A small crystal pendant has been dropped here", "", "", "", 0, 50, 0),
        ("fountain", "A small icy fountain burbles gently in the centre of the room", "", "", "", 0, 0, 1),
        ("hole", "A hole has been dug north through the snow", "", "", "", 1, 0, 1),
        ("hole", "A hole has been dug south through the snow", "", "", "", 1, 0, 1),
        ("cupboard", "The cupboard is open", "The cupboard is closed", "The cupboard is locked", "", 1, 0, 1),
        ("cupboard", "The cupboard is open", "The cupboard is closed", "The cupboard is locked", "", 1, 0, 1),

        # 180
        (
            "chest",
            "A huge iron bound chest lies open before you",
            "A huge iron bound chest lies before you",
            "", "", 1, 0, 1
        ),
        ("coronet", "A small jewelled coronet glitters before you", "", "", "", 0, 300, 0),
        ("key", "An old rusty key lies here", "", "", "", 0, 0, 0),
        ("pillowcase", "A soggy pillowcase has been dumped here", "", "", "", 0, 10, 0),
        ("dagger", "A strange, thin icy dagger lies at your feet.", "", "", "", 0, 100, 0),
        ("gem", "A small orange gem has been dropped here", "", "", "", 0, 20, 0),
        (
            "slab",
            "A heavy stone slab has been shifted to one side, allowing access down",
            "A heavy stone slab appears to bar an exit downwards",
            "", "", 1, 0, 1
        ),
        (
            "slab",
            "A heavy stone slab has been shifted to one side, allowing access upwards",
            "A heavy stone slab seals the barrow from above",
            "", "", 1, 0, 1
        ),
        ("wreath", "An old wreath lies here", "", "", "", 0, 50, 0),
        ("shroud", "A silk shroud has been placed here", "", "", "", 0, 50, 0),

        # 190
        ("effigy", "A small stone effigy has been left here", "", "", "", 0, 75, 0),
        ("statuette", "A small gold statuette has stands here, glittering in the light", "", "", "", 0, 75, 0),
        ("chute", "There is a chute in the west wall, too small to climb down.", "", "", "", 0, 0, 1),
        ("chute", "There is a chute in the east wall, too small to climb down.", "", "", "", 0, 0, 1),
    )
    __ITEMS_INITIAL = {
        0: {'room_id': 0},
        1: {'room_id': -5},
        # 2-34
        35: {'room_id': -600},
        # 36-39
        40: {'room_id': -340},
        41: {'room_id': -340},
        42: {'room_id': -342},
        43: {'room_id': -309},
        44: {'room_id': -620},
        45: {'room_id': -633},
        46: {'room_id': -644},
        47: {'room_id': -645},
        48: {'room_id': -609},
        49: {'room_id': -641},
        50: {'room_id': -302},
        51: {'room_id': -309},
        52: {'room_id': -305},
        53: {'room_id': -306},
        54: {'room_id': -307},
        55: {'room_id': -308},
        56: {'room_id': -311},
        57: {'room_id': -313},
        58: {'room_id': -305},
        59: {'room_id': -313},
        60: {'room_id': -315},
        61: {'room_id': -314},
        62: {'room_id': -332},
        63: {'room_id': -600},
        64: {'room_id': -319},
        65: {'room_id': -316},
        66: {'room_id': -321},
        67: {'room_id': -320},
        68: {'room_id': -325},
        69: {'room_id': -326},
        # 70
        71: {'room_id': -326},
        72: {'room_id': -326},
        73: {'room_id': -326},
        74: {'room_id': -5},
        75: {'room_id': -609},
        76: {'room_id': -612},
        77: {'room_id': -637},
        # 78-81
        82: {'room_id': -643},
        # 83-85
        86: {'room_id': -614},
        # 87-99
        100: {'room_id': -101, 'flags': {0, 6}},  # 100: {'room_id': -102},
        # 101
        102: {'room_id': -104},
        103: {'room_id': -104},
        104: {'room_id': -107},
        105: {'room_id': -109},
        # 106-184
        185: {'room_id': -109},
        186: {'room_id': -651},
        187: {'room_id': -650},
        188: {'room_id': -650},
        189: {'room_id': -650},
        190: {'room_id': -109},
        191: {'room_id': -109},
    }

    @classmethod
    def __item_data(cls, item_id):
        slug = None
        if 0 <= item_id < len(cls.__ITEMS_DATA):
            data = cls.__ITEMS_DATA[item_id]
            if len(data) > 8:
                slug = data[0]
                data = data[1:]
        else:
            data = None
        name = data[0] if data else ''
        initial = cls.__ITEMS_INITIAL.get(item_id, {})
        has_connected = item_id % 2 > 0
        flags = initial.get('flags', set())
        # logger.debug("%s(%s):\t%s %s", item_id, has_connected, data, initial)
        return {
            'item_id': item_id,
            # Item Data
            'name': name,
            'slug': slug or name,
            'description': data[1:5] if data else [''] * 4,
            'max_state': data[5] if data else 0,
            'flannel': data[7] > 0 if data else False,
            'base_value': data[6] if data else 0,
            # World Item
            'location': initial.get('room_id', 0),
            # 1-2
            'carry_flag': 0,
            'state': 0,

            # Flags
            'is_destroyed': 0 in flags,
            'has_connected': 1 in flags,
            # 2
            # 3
            # 4-7
            # 8-11
            'change_on_take': 12 in flags,
            'is_light': 13 in flags,
            # 14
            'is_weapon': 15 in flags,
        }

    @classmethod
    def item(cls, item_id):
        return cls.__item_data(item_id)

    def reset(self):
        return (self.item(item_id) for item_id in range(self.ITEMS))
