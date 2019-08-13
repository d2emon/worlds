from ..messages import process as dcprnt  # The main loop

# bprintf   Player.add_message
# seeplayer Character.find(player=player)
# sysbuf    Player.__text_messages
# pbfr      Player.get_text

# setname   Player.__set_pronoun

# FILE * log_fl= 0; /* 0 = not logging */

# def logcom():

# long snoopd= -1;

# def opensnoop(user,per):

# long snoopt= -1;
# char sntn[32];

# def snoopcom():
# def viewsnoop():
# def chksnp():

"""
FILE * log_fl= 0; /* 0 = not logging */

void logcom()
    {
    extern FILE * log_fl;
    extern char globme[];
    if(getuid()!=geteuid()) {bprintf("\nNot allowed from this ID\n");return;}
    if(log_fl!=0)
       {
       fprintf(log_fl,"\nEnd of log....\n\n");
       fclose(log_fl);
       log_fl=0;
       bprintf("End of log\n");
       return;
       }
    bprintf("Commencing Logging Of Session\n");
    log_fl=fopen("mud_log","a");
    if(log_fl==0) log_fl=fopen("mud_log","w");
    if(log_fl==0)
       {
       bprintf("Cannot open log file mud_log\n");
       return;
       }
    bprintf("The log will be written to the file 'mud_log'\n");
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
"""