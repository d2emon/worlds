import re


class State:
    messages = []

    log_file = None

    snooped_id = None
    snooper_id = None

    ail_blind = False
    channel = False


####


def clear_messages():
    State.messages = []


def add_message(message):
    State.messages.append(message)


####

def __block_alarm():
    pass


def __unblock_alarm():
    pass


def __save_world():
    pass


def get_player(player_id):
    return None


def isdark(channel):
    return False


####


def __set_name(player):
    if player.player_id > 15 and player.player_id not in (fpbns("riatha").player_id, fpbns("shazareth").player_id):
        State.wd_it = player.name
        return
    if player.sex:
        State.wd_her = player.name
    else:
        State.wd_him = player.name
    State.wd_them = player.name


def see_player(player_id_1, player_id_2):
    player_1 = get_player(player_id_1)
    player_2 = get_player(player_id_2)
    if player_1 is None:
        return False
    if player_2 is None:
        return True
    if player_id_1 == player_id_2:
        return True

    if player_1.level < player_2.level:
        return False
    if State.ail_blind:
        return False
    if (State.channel == player_2.channel) and isdark(State.channel):
        return False
    __set_name(player_2)
    return True


def __pfile(match):
    return match.group(0)


def __pndeaf(match):
    return match.group(0)


def __pcansee(match):
    see_player(None, None)
    return match.group(0)


def __prname(match):
    see_player(None, None)
    return match.group(0)


def __pndark(match):
    return match.group(0)


def __ppndeaf(match):
    see_player(None, None)
    return match.group(0)


def __ppnblind(match):
    see_player(None, None)
    return match.group(0)


def __pnotkb(match):
    return match.group(0)


"""
int pfile(str,ct,file)
 char *str;
 FILE *file;
    {
    extern long debug_mode;
    char x[128];
    ct=tocontinue(str,ct,x,128);
    if(debug_mode) fprintf(file,"[FILE %s ]\n",str);
    f_listfl(x,file);
    return(ct);
    }

int pndeaf(str,ct,file)
 char *str;
 FILE *file;
    {
    char x[256];
    extern long ail_deaf;
    ct=tocontinue(str,ct,x,256);
    if(!ail_deaf)fprintf(file,"%s",x);
    return(ct);
    }

 pcansee(str,ct,file)
 char *str;
 FILE *file;
    {
    char x[25];
    char z[257];
    long a;
    ct=tocontinue(str,ct,x,23);
    a=fpbns(x);
    if(!seeplayer(a))
       {
       ct=tocontinue(str,ct,z,256);
       return(ct);
       }
    ct=tocontinue(str,ct,z,256);
    fprintf(file,"%s",z);
    return(ct);
    }

 prname(str,ct,file)
 char *str;
 FILE *file;
    {
    char x[24];
    ct=tocontinue(str,ct,x,24);
    if(!seeplayer(fpbns(x)))
    fprintf(file,"Someone");
    else
      fprintf(file,"%s",x);
    return(ct);
    }


int pndark(str,ct,file)
 char *str;
 FILE *file;
    {
    char x[257];
    extern long ail_blind;
    ct=tocontinue(str,ct,x,256);
    if((!isdark())&&(ail_blind==0))
    fprintf(file,"%s",x);
    return(ct);
    }

int ppndeaf(str,ct,file)
 char *str;
 FILE *file;
    {
    char x[24];
    extern long ail_deaf;
    long a;
    ct=tocontinue(str,ct,x,24);
    if(ail_deaf) return(ct);
    a=fpbns(x);
    if(seeplayer(a)) fprintf(file,"%s",x);
    else
      fprintf(file,"Someone");
    return(ct);
    }

int  ppnblind(str,ct,file)
char *str;
FILE *file;
    {
    extern long ail_blind;
    char x[24];
    long a;
    ct=tocontinue(str,ct,x,24);
    if(ail_blind) return(ct);
    a=fpbns(x);
    if(seeplayer(a)) fprintf(file,"%s",x);
    else
       fprintf(file,"Someone");
    return(ct);
    }
int pnotkb(str,ct,file)
 char *str;
 FILE *file;
    {
    extern long iskb;
    char x[128];
    ct=tocontinue(str,ct,x,127);
    if(iskb) return(ct);
    fprintf(file,"%s",x);
    return(ct);
    }
"""


def __process_special(message, is_keyboard):
    message = re.sub(r"\[f\](.{0, 128})\[/f\]", __pfile, message)
    message = re.sub(r"\[d\](.{0, 128})\[/d\]", __pndeaf, message)
    message = re.sub(r"\[s\](.{0, 128})\[/s\]", __pcansee, message)
    message = re.sub(r"\[p\](.{0, 128})\[/p\]", __prname, message)
    message = re.sub(r"\[c\](.{0, 128})\[/c\]", __pndark, message)
    message = re.sub(r"\[P\](.{0, 128})\[/P\]", __ppndeaf, message)
    message = re.sub(r"\[D\](.{0, 128})\[/D\]", __ppnblind, message)
    message = re.sub(r"\[l\](.{0, 128})\[/l\]", __pnotkb, message)
    return message


def show_file(filename):
    return "[f]{}[/f]".format(filename)


class Service:
    CONNECTIONS = {}
    __last_connection_id = 0
    __DATA = []

    def __init__(self, filename, permissions):
        self.__last_connection_id += 1
        self.__filename = filename
        self.__permissions = permissions
        self.CONNECTIONS[self.__last_connection_id] = self
        self.service_id = self.__last_connection_id

    def disconnect(self):
        self.service_id = None

    def append(self, message):
        if not self.service_id:
            raise Exception()

        self.__DATA.append(message)

    def contents(self):
        yield from self.__DATA

    def reset(self):
        self.__DATA = []


class LogService(Service):
    __ALLOWED_USER_ID = 'ALLOWED_USER_ID'

    def __init__(self, user_id, permissions):
        self.__validate_user(user_id)
        super().__init__('mud_log', permissions)

    @classmethod
    def __validate_user(cls, user_id):
        if user_id == cls.__ALLOWED_USER_ID:
            raise Exception('Not allowed from this ID')

    @classmethod
    def restore(cls, user_id, log_id):
        cls.__validate_user(user_id)
        return cls.CONNECTIONS[log_id]


class SnoopService(Service):
    __SNOOP = 'SNOOP'

    def __init__(self, player, permissions):
        super().__init__(self.__SNOOP + player, permissions)


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


def log_cmd(**kwargs):
    user_id = kwargs.get('user_id')
    if State.log_file is not None:
        service = LogService.restore(user_id, State.log_file)
        service.append("\nEnd of log....\n\n")
        service.disconnect()

        State.log_file = None
        add_message("End of log")
        return

    add_message("Commencing Logging Of Session")

    service = LogService(user_id, 'a')
    if not service.service_id:
        service = LogService(user_id, 'w')
    if not service.service_id:
        add_message("Cannot open log file mud_log")
        return

    State.log_file = service.service_id
    add_message("The log will be written to the file 'mud_log'")


def snoop_cmd(*args, **kwargs):
    level = kwargs.get('level', 0)
    player_id = kwargs.get('player_id', None)
    name = kwargs.get('name', "")

    if level < 10:
        add_message("Ho hum, the weather is nice isn't it")
        return

    snooped = get_player(State.snooped_id)
    if snooped:
        add_message("Stopped snooping on {}".format(snooped))
        sendsys(State.snooped_id, player_id, -400, 0, "")
        State.snooped_id = None

    if len(args) < 1:
        return

    snooped = fpbn(args[0])
    if not snooped:
        add_message("Who is that ?")
        return

    if (level < 10000 and snooped.level >= 10) or snooped.bit[6]:
        add_message("Your magical vision is obscured")
        State.snooped_id = None
        return

    State.snooped_id = snooped.player_id
    add_message("Started to snoop on {}".format(snooped.name))
    sendsys(snooped.player_id, player_id, -401, 0, "")

    service = SnoopService(name, "w")
    service.append(" ")
    service.disconnect()


def post_clear_messages():
    State.messages = []
    return {
        'result': True,
    }


def post_add_message(message):
    add_message(message)
    return {
        'result': True,
    }


def get_messages(is_finished, user_id, name):
    def output(is_keyboard):
        for message in State.messages:
            yield __process_special(message, is_keyboard)

    __block_alarm()
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
    __unblock_alarm()
    return {
        'is_clean': is_clean,
        'is_finished': False,
        'messages': result,
        'snoop': __view_snoop(name),
        'result': True,
    }
