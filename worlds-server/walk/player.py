import random


class Player:
    WIZARD_LEVEL = 10
    GOD_LEVEL = 10000

    level = 10000  # my_lev
    room_id = random.choice([
        -5,
        -183,
    ])  # curch
    is_god = level >= GOD_LEVEL
    is_wizard = level >= WIZARD_LEVEL
