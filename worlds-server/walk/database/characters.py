from .database import ListDatabase
from .logger import logger


class Characters(ListDatabase):
    ITEMS = 48
    MOBILES = [
        {
            'name': "The Wraith",
            'room_id': -1077,
            'strength': 60,
            'sex': 2,
            'level': -2,
        },
        {
            'name': "Shazareth",
            'room_id': -1080,
            'strength': 99,
            'sex': 0,
            'level': -30,
        },
        {
            'name': "Bomber",
            'room_id': -308,
            'strength': 50,
            'sex': 2,
            'level': -10,
        },
        {
            'name': "Owin",
            'room_id': -311,
            'strength': 50,
            'sex': 2,
            'level': -11,
        },
        {
            'name': "Glowin",
            'room_id': -318,
            'strength': 50,
            'sex': 2,
            'level': -12,
        },
        {
            'name': "Smythe",
            'room_id': -320,
            'strength': 50,
            'sex': 2,
            'level': -13,
        },
        {
            'name': "Dio",
            'room_id': -332,
            'strength': 50,
            'sex': 2,
            'level': -14,
        },
        {
            'name': "The Dragon",
            'room_id': -326,
            'strength': 500,
            'sex': 2,
            'level': -2,
        },

        {
            'name': "The Zombie",
            'room_id': -639,
            'strength': 20,
            'sex': 2,
            'level': -2,
        },
        {
            'name': "The Golem",
            'room_id': -1056,
            'strength': 90,
            'sex': 2,
            'level': -2,
        },
        {
            'name': "The Haggis",
            'room_id': -341,
            'strength': 50,
            'sex': 2,
            'level': -2,
        },
        {
            'name': "The Piper",
            'room_id': -630,
            'strength': 50,
            'sex': 2,
            'level': -2,
        },
        {
            'name': "The Rat",
            'room_id': -1064,
            'strength': 20,
            'sex': 2,
            'level': -2,
        },
        {
            'name': "The Ghoul",
            'room_id': -129,
            'strength': 40,
            'sex': 2,
            'level': -2,
        },
        {
            'name': "The Figure",
            'room_id': -130,
            'strength': 90,
            'sex': 2,
            'level': -2,
        },
        {
            'name': "The Ogre",
            'room_id': -144,
            'strength': 40,
            'sex': 2,
            'level': -2,
        },

        {
            'name': "Riatha",
            'room_id': -165,
            'strength': 50,
            'sex': 0,
            'level': -31,
        },
        {
            'name': "The Yeti",
            'room_id': -173,
            'strength': 80,
            'sex': 2,
            'level': -2,
        },
        {
            'name': "The Guardian",
            'room_id': -197,
            'strength': 50,
            'sex': 2,
            'level': -2,
        },
        {
            'name': "Prave",
            'room_id': -201,
            'strength': 60,
            'sex': 2,
            'level': -400,
        },
        {
            'name': "Wraith",
            'room_id': -350,
            'strength': 60,
            'sex': 2,
            'level': -2,
        },
        {
            'name': "Bath",
            'room_id': -1,
            'strength': 70,
            'sex': 2,
            'level': -401,
        },
        {
            'name': "Ronnie",
            'room_id': -809,
            'strength': 40,
            'sex': 2,
            'level': -402,
        },
        {
            'name': "The Mary",
            'room_id': -1,
            'strength': 50,
            'sex': 2,
            'level': -403,
        },

        {
            'name': "The Cookie",
            'room_id': -126,
            'strength': 70,
            'sex': 2,
            'level': -404,
        },
        {
            'name': "MSDOS",
            'room_id': -1,
            'strength': 50,
            'sex': 2,
            'level': -405,
        },
        {
            'name': "The Devil",
            'room_id': -1,
            'strength': 70,
            'sex': 2,
            'level': -2,
        },
        {
            'name': "The Copper",
            'room_id': -1,
            'strength': 40,
            'sex': 2,
            'level': -2,
        },
    ]

    @classmethod
    def __is_aggressive(cls, name):
        return name in (
            "shazareth",
            "wraith",
            "bomber",
            "owin",
            "glowin",
            "smythe",
            "dio",
            "zombie",
            "rat",
            "ghoul",
            "ogre",
            "riatha",
            "yeti",
            "guardian",
        )

    @classmethod
    def __is_undead(cls, name):
        return name in (
            "wraith",
            "zombie",
        )

    @classmethod
    def __character_data(cls, character_id):
        return {
            'character_id': character_id,
            'name': '',
            'room_id': 0,
            'message_id': -1,
            # 6
            'strength': 0,
            'visible': 0,
            'level': 0,
            'weapon': 0,
            # 12
            'helping': None,
            # Flags
            'sex': 0,
            # Other
            'is_aggressive': False,
            'is_undead': False,
        }

    @classmethod
    def character(cls, character_id):
        result = cls.__character_data(character_id)
        if character_id < 16:
            # logger.debug("%s:\t%s", character_id, result)
            return result
        character_id -= 16
        if character_id < len(cls.MOBILES):
            result.update(cls.MOBILES[character_id])

            name = result.get('name', '').lower()
            if name[:4] == "the ":
                name = name[4:]
            result.update({
                'is_aggressive': cls.__is_aggressive(name),
                'is_undead': cls.__is_undead(name),
            })
        # logger.debug("%s:\t%s", character_id + 16, result)
        return result

    def reset(self):
        return (self.character(character_id + 1) for character_id in range(self.ITEMS))
