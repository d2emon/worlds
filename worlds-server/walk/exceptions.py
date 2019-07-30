class ActionError(Exception):
    pass


class DatabaseError(Exception):
    pass


def crapup(*args):
    raise NotImplementedError()
