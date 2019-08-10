import re
from .models.character import Character


def __file_contents(debug_mode):
    # pfile
    text = "f_listfl(match.group(1), dst)"
    return lambda match: "[FILE {} ]\n{}".format(match.group(1), text) if debug_mode else text


def __hear(player):
    # pndeaf
    # return lambda match: match.group(1) if Globals.ail_deaf else ""
    return lambda match: match.group(1)


def __see_name(player):
    # prname
    return lambda match: "Someone" if Character.find(name=match.group(1), visible_for=player) else ""


def __not_dark(player):
    # pndark
    return lambda match: match.group(1) if player.can_see else ""


def __not_deaf_name(player):
    # ppndeaf
    # def f(match):
    #     if Globals.ail_deaf:
    #         return ""
    return __see_name(player)


def __not_blind_name(player):
    # ppnbind
    # def f(match):
    #     if Globals.ail_blind:
    #         return ""
    return __see_name(player)


def __see(player):
    # pcansee
    return lambda match: match.group(2) if Character.find(name=match.group(1), visible_for=player) else ""


def __not_keyboard(is_keyboard):
    # pnotkb
    return lambda match: "" if is_keyboard else "`{}`".format(match.group(1))


def process(player, src, dst=None, is_keyboard=True, debug_mode=False):
    if not src:
        return src
    src = re.sub(r'\[f\](\w{0,128})\[/f\]', __file_contents(debug_mode), src, flags=re.S)
    src = re.sub(r'\[d\](.*)\[/d\]', __hear(player), src, flags=re.S)
    src = re.sub(r'\[s\s+name=\"(\w{0,23})\"\](.*)\[/s\]', __see(player), src, flags=re.S)
    src = re.sub(r'\[p\](\w{0,23})\[/p\]', __see_name(player), src, flags=re.S)
    src = re.sub(r'\[c\](.*)\[/c\]', __not_dark(player), src, flags=re.S)
    src = re.sub(r'\[P\](\w{0,23})\[/P\]', __not_deaf_name(player), src, flags=re.S)
    src = re.sub(r'\[D\](\w{0,23})\[/D\]', __not_blind_name(player), src, flags=re.S)
    src = re.sub(r'\[l\](.*)\[/l\]', __not_keyboard(is_keyboard), src, flags=re.S)
    return src
