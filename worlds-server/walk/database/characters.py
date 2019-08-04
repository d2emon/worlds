from .database import WorldDatabase


class Characters(WorldDatabase):
    ITEMS = 48
    MOBILES = [
        {
            'name': "The Wraith",
            'room_id': -1077,
            'strength': 60,
            'sex': 0,
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
            'sex': 0,
            'level': -10,
        },
        {
            'name': "Owin",
            'room_id': -311,
            'strength': 50,
            'sex': 0,
            'level': -11,
        },
        {
            'name': "Glowin",
            'room_id': -318,
            'strength': 50,
            'sex': 0,
            'level': -12,
        },
        {
            'name': "Smythe",
            'room_id': -320,
            'strength': 50,
            'sex': 0,
            'level': -13,
        },
        {
            'name': "Dio",
            'room_id': -332,
            'strength': 50,
            'sex': 0,
            'level': -14,
        },
        {
            'name': "The Dragon",
            'room_id': -326,
            'strength': 500,
            'sex': 0,
            'level': -2,
        },

        {
            'name': "The Zombie",
            'room_id': -639,
            'strength': 20,
            'sex': 0,
            'level': -2,
        },
        {
            'name': "The Golem",
            'room_id': -1056,
            'strength': 90,
            'sex': 0,
            'level': -2,
        },
        {
            'name': "The Haggis",
            'room_id': -341,
            'strength': 50,
            'sex': 0,
            'level': -2,
        },
        {
            'name': "The Piper",
            'room_id': -630,
            'strength': 50,
            'sex': 0,
            'level': -2,
        },
        {
            'name': "The Rat",
            'room_id': -1064,
            'strength': 20,
            'sex': 0,
            'level': -2,
        },
        {
            'name': "The Ghoul",
            'room_id': -129,
            'strength': 40,
            'sex': 0,
            'level': -2,
        },
        {
            'name': "The Figure",
            'room_id': -130,
            'strength': 90,
            'sex': 0,
            'level': -2,
        },
        {
            'name': "The Ogre",
            'room_id': -144,
            'strength': 40,
            'sex': 0,
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
            'sex': 0,
            'level': -2,
        },
        {
            'name': "The Guardian",
            'room_id': -197,
            'strength': 50,
            'sex': 0,
            'level': -2,
        },
        {
            'name': "Prave",
            'room_id': -201,
            'strength': 60,
            'sex': 0,
            'level': -400,
        },
        {
            'name': "Wraith",
            'room_id': -350,
            'strength': 60,
            'sex': 0,
            'level': -2,
        },
        {
            'name': "Bath",
            'room_id': -1,
            'strength': 70,
            'sex': 0,
            'level': -401,
        },
        {
            'name': "Ronnie",
            'room_id': -809,
            'strength': 40,
            'sex': 0,
            'level': -402,
        },
        {
            'name': "The Mary",
            'room_id': -1,
            'strength': 50,
            'sex': 0,
            'level': -403,
        },

        {
            'name': "The Cookie",
            'room_id': -126,
            'strength': 70,
            'sex': 0,
            'level': -404,
        },
        {
            'name': "MSDOS",
            'room_id': -1,
            'strength': 50,
            'sex': 0,
            'level': -405,
        },
        {
            'name': "The Devil",
            'room_id': -1,
            'strength': 70,
            'sex': 0,
            'level': -2,
        },
        {
            'name': "The Copper",
            'room_id': -1,
            'strength': 40,
            'sex': 0,
            'level': -2,
        },
    ]

    @classmethod
    def character(cls, character_id):
        if character_id < 16:
            return {}
        character_id -= 16
        if character_id >= len(cls.MOBILES):
            return {}
        return cls.MOBILES[character_id]
