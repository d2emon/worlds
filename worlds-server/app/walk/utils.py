from walk.exceptions import ActionError, StopGame
from walk.player import Player


def current_player():
    return Player.player()


def __update_result(result):
    return {
        **result,
        'errorCode': result.get('errorCode', 0),
        'error': result.get('error'),
        # 'messages': result.get('messages', []),
    }


def __on_error(message):
    return {
        'errorCode': 1,
        'error': str(message),
    }


def __on_stop(message):
    return {
        'errorCode': 2,
        'error': str(message),
        'messages': Player.player().on_stop_game(),
    }


def do_action(f):
    def wrapped(*args, **kwargs):
        try:
            result = f(*args, **kwargs) or {}
        except ActionError as e:
            result = __on_error(e)
        except StopGame as e:
            result = __on_stop(e)

        return __update_result(result)
    return wrapped
