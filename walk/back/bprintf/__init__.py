from .services import LogService, SnoopService
from .pronouns import Pronouns
import re


class State:
    messages = []

    log_file = None

    snooped_id = None
    snooper_id = None

    ail_blind = False
    ail_deaf = False
    channel = False
    player = None


####


def __clear_messages():
    State.messages = []


def __add_message(message):
    State.messages.append(message)


####
def __save_world():
    pass


def get_player(player_id):
    return None


def isdark(channel=None):
    return False


def fpbn(player):
    return None


def fpbns(player):
    return None


def sendsys(receiver, sender, code, channel_id, payload):
    return None


####


def see_player(player_1, player_2):
    if player_1 is None:
        return False
    if player_2 is None:
        return True
    if player_1.player_id == player_2.player_id:
        return True
    if player_1.level < player_2.level:
        return False
    if State.ail_blind:
        return False
    if (State.channel == player_2.channel) and isdark(State.channel):
        return False
    return True


# Special


def __pfile(match):
    """
    if(debug_mode) fprintf(file,"[FILE %s ]\n",str);
    f_listfl(x,file);
    """
    return match.group(0)


def __pndeaf(match):
    if State.ail_deaf:
        return ""
    return match.group(0)


def __pcansee(match):
    """
    a=fpbns(x);
    if(!seeplayer(a))
       {
       ct=tocontinue(str,ct,z,256);
       return(ct);
       }
    ct=tocontinue(str,ct,z,256);
    fprintf(file,"%s",z);
    """
    player_1 = None
    player_2 = None
    pronouns = Pronouns()
    see = see_player(player_1, player_2)
    if not see:
        return ""
    pronouns.set_name(player_2)
    return match.group(0)


def __prname(match):
    """
    if(!seeplayer(fpbns(x)))
    fprintf(file,"Someone");
    else
      fprintf(file,"%s",x);
    """
    player_1 = None
    player_2 = None
    pronouns = Pronouns()
    see = see_player(player_1, player_2)
    if not see:
        return "Someone"
    pronouns.set_name(player_2)
    return match.group(0)


def __pndark(match):
    if isdark() or State.ail_blind:
        return ""
    return match.group(0)


def __ppndeaf(match):
    if State.ail_deaf:
        return ""
    return __prname(match)


def __ppnblind(match):
    if State.ail_blind:
        return ""
    return __prname(match)


def __pnotkb(is_keyboard):
    def f(match):
        if is_keyboard:
            return ""
        return match.group(0)
    return f


def __process_special(message, is_keyboard):
    message = re.sub(r"\[f\](.{0, 128})\[/f\]", __pfile, message)
    message = re.sub(r"\[d\](.{0, 256})\[/d\]", __pndeaf, message)
    message = re.sub(r"\[s name=\".{0, 24}\"\](.{0, 256})\[/s\]", __pcansee, message)
    message = re.sub(r"\[p\](.{0, 24})\[/p\]", __prname, message)
    message = re.sub(r"\[c\](.{0, 256})\[/c\]", __pndark, message)
    message = re.sub(r"\[P\](.{0, 24})\[/P\]", __ppndeaf, message)
    message = re.sub(r"\[D\](.{0, 24})\[/D\]", __ppnblind, message)
    message = re.sub(r"\[l\](.{0, 128})\[/l\]", __pnotkb(is_keyboard), message)
    return message


def show_file(filename):
    return "[f]{}[/f]".format(filename)


# Snoop


def __view_snoop(name):
    if not State.snooped_id:
        return ""

    service = SnoopService(name, 'r+')
    if not service.service_id:
        return ""

    result = "\n".join(map(lambda s: "|{}".format(s), service.contents()))
    service.reset()
    service.disconnect()

    return result


def check_snoop(player_id):
    if not State.snooped_id:
        return

    sendsys(State.snooped_id, player_id, -400, 0, "")


# Commands


def log_cmd(**kwargs):
    user_id = kwargs.get('user_id')
    if State.log_file is not None:
        service = LogService.restore(user_id, State.log_file)
        service.append("\nEnd of log....\n\n")
        service.disconnect()

        State.log_file = None
        __add_message("End of log")
        return

    __add_message("Commencing Logging Of Session")

    service = LogService(user_id, 'a')
    if not service.service_id:
        service = LogService(user_id, 'w')
    if not service.service_id:
        __add_message("Cannot open log file mud_log")
        return

    State.log_file = service.service_id
    __add_message("The log will be written to the file 'mud_log'")


def snoop_cmd(*args, **kwargs):
    level = kwargs.get('level', 0)
    player_id = kwargs.get('player_id', None)
    name = kwargs.get('name', "")

    if level < 10:
        __add_message("Ho hum, the weather is nice isn't it")
        return

    snooped = get_player(State.snooped_id)
    if snooped:
        __add_message("Stopped snooping on {}".format(snooped))
        sendsys(State.snooped_id, player_id, -400, 0, "")
        State.snooped_id = None

    if len(args) < 1:
        return

    snooped = fpbn(args[0])
    if not snooped:
        __add_message("Who is that ?")
        return

    if (level < 10000 and snooped.level >= 10) or snooped.bit[6]:
        __add_message("Your magical vision is obscured")
        State.snooped_id = None
        return

    State.snooped_id = snooped.player_id
    __add_message("Started to snoop on {}".format(snooped.name))
    sendsys(snooped.player_id, player_id, -401, 0, "")

    service = SnoopService(name, "w")
    service.append(" ")
    service.disconnect()


# Controllers


def post_clear_messages():
    State.messages = []
    return {
        'result': True,
    }


def post_add_message(message):
    __add_message(message)
    return {
        'result': True,
    }


def get_messages(is_finished, user_id, name):
    def output(is_keyboard):
        for message in State.messages:
            yield __process_special(message, is_keyboard)

    __save_world()

    is_clean = len(State.messages) == 0

    result = []
    if not is_clean and not is_finished:
        result.append("")

    if State.log_file:
        service = LogService(user_id, State.log_file)
        map(service.append, output(False))

    snooper = get_player(State.snooper_id)
    if snooper:
        service = SnoopService(snooper.name, 'a')
        if service.service_id:
            map(service.append, output(False))
            service.disconnect()

    result += output(True)

    State.messages = []
    return {
        'is_clean': is_clean,
        'is_finished': False,
        'messages': result,
        'snoop': __view_snoop(name),
        'result': True,
    }
