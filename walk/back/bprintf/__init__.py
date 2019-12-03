import re


class State:
    messages = []

    log_file = None

    ail_blind = False
    channel = False

####

def add_message(message):
    State.messages.append(message)

####

def get_player(player_id):
    return None


def isdark(channel):
    return False


def setname(name):
    return False


####


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
    setname(player_id_2.name)
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
"""


def __process_special(message):
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


class LogService:
    __ALLOWED_USER_ID = 'ALLOWED_USER_ID'
    __LOG = []

    def __init__(self, user_id, log_id):
        self.__validate_user(user_id)
        self.__connected = False
        self.service_id = log_id

    @classmethod
    def __validate_user(cls, user_id):
        if user_id == cls.__ALLOWED_USER_ID:
            raise Exception('Not allowed from this ID')

    def append(self, message):
        if not self.__connected:
            raise Exception()

        self.__LOG.append(message)

    def disconnect(self):
        self.__connected = False

    @classmethod
    def connect(cls, user_id, filename, permissions):
        return cls(user_id, 0)


def log_cmd(*args, **kwargs):
    user_id = kwargs.get('user_id')
    if State.log_file is not None:
        service = LogService(user_id, State.log_file)
        service.append("\nEnd of log....\n\n")
        service.disconnect()

        State.log_file = None
        add_message("End of log")
        return

    add_message("Commencing Logging Of Session")

    service = LogService.connect(user_id, 'mud_log', 'a') or LogService.connect(user_id, 'mud_log', 'w')
    if not service:
        add_message("Cannot open log file mud_log")
        return

    State.log_file = service.service_id
    add_message("The log will be written to the file 'mud_log'")


"""
void pbfr()
    {
    FILE *fln;
    long mu;
    block_alarm();
    closeworld();
    if(strlen(sysbuf)) pr_due=1;
    if((strlen(sysbuf))&&(pr_qcr)) putchar('\n');
    pr_qcr=0;
    if(State.log_file!=NULL)
       {
       iskb=0;
       dcprnt(sysbuf, State.log_file);
       }
    if(snoopd!=-1)
       {
       fln=opensnoop(pname(snoopd),"a");
       if(fln>0)
          {
iskb=0;
          dcprnt(sysbuf,fln);
          fcloselock(fln);
          }
       }
    iskb=1;
    dcprnt(sysbuf,stdout);
    sysbuf[0]=0; /* clear buffer */
    if(snoopt!=-1) viewsnoop();
    unblock_alarm();
    }

long iskb=1;

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

long snoopd= -1;

FILE *opensnoop(user,per)
char *per;
char *user;
    {
    FILE *x;
    extern FILE *openlock();
    char z[256];
    sprintf(z,"%s%s",SNOOP,user);
    x=openlock(z,per);
    return(x);
    }

long snoopt= -1;

char sntn[32];

void snoopcom()
    {
    FILE *fx;
    long x;
    if(my_lev<10)
       {
       bprintf("Ho hum, the weather is nice isn't it\n");
       return;
       }
    if(snoopt!=-1)
       {
       bprintf("Stopped snooping on %s\n",sntn);
       snoopt= -1;
       sendsys(sntn,globme,-400,0,"");
       }
    if(brkword()== -1)
       {
       return;
       }
    x=fpbn(wordbuf);
    if(x==-1)
       {
       bprintf("Who is that ?\n");
       return;
       }
    if(((my_lev<10000)&&(plev(x)>=10))||(ptstbit(x,6)))
       {
       bprintf("Your magical vision is obscured\n");
       snoopt= -1;
       return;
       }
    strcpy(sntn,pname(x));
    snoopt=x;
    bprintf("Started to snoop on %s\n",pname(x));
    sendsys(sntn,globme,-401,0,"");
    fx=opensnoop(globme,"w");
    fprintf(fx," ");
    fcloselock(fx);
    }

void viewsnoop()
    {
    long x;
    char z[128];
    FILE *fx;
    fx=opensnoop(globme,"r+");
    if(snoopt==-1) return;
    if(fx==0)return;
    while((!feof(fx))&&(fgets(z,127,fx)))
           printf("|%s",z);
    ftruncate(fileno(fx),0);
    fcloselock(fx);
    x=snoopt;
    snoopt= -1;
    /*
    pbfr();
    */
    snoopt=x;
    }
void chksnp()
{
if(snoopt==-1) return;
sendsys(sntn,globme,-400,0,"");
}

void setname(x)  /* Assign Him her etc according to who it is */
long x;
{
	if((x>15)&&(x!=fpbns("riatha"))&&(x!=fpbns("shazareth")))
	{
		strcpy(wd_it,pname(x));
		return;
	}
	if(psex(x)) strcpy(wd_her,pname(x));
	else strcpy(wd_him,pname(x));
	strcpy(wd_them,pname(x));
}
"""


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
