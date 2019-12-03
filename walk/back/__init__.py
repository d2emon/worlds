import logging


def __openworld():
    pass


def __closeworld():
    pass


def __on_timing():
    pass


def __rte(name, interrupt):
    pass


def __talker(name):
    pass


class State:
    in_fight = 0
    name = ''


def post_start(user_id, name):
    logging.info("GAME ENTRY: {}[{}]".format(name, user_id))
    State.name = name
    __talker(name)
    return {
        'message': "Hello {}".format(name),
    }


def get_timer(name):
    __openworld()
    __rte(name, True)
    __on_timing()
    __closeworld()
    return {}


def get_can_exit():
    return not State.in_fight


def get_loose():
    pass
