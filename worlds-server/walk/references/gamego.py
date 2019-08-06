# Two Phase Game System

from ..exceptions import StopGame as crapup

# def getkbd(s, l):

# long sig_active=0;

# def sig_alon():
# def unblock_alarm():
# def block_alarm():
# def sig_aloff():

# long interrupt=0;

# def sig_occur():

from ..player import sig_init as sig_init
from ..player import sig_oops as sig_oops
from ..player import sig_ctrlc as sig_ctrlc

# def set_progname(n, text):

"""
char *getkbd(s,l)   /* Getstr() with length limit and filter ctrl */
 char *s;
 int l;
    {
    char c,f,n;
    f=0;c=0;
    while(c<l)
       {
       regec:n=getchar();
       if ((n<' ')&&(n!='\n')) goto regec;
       if (n=='\n') {s[c]=0;f=1;c=l-1;}
       else
          s[c]=n;
       c++;
       }
    if (f==0) {s[c]=0;while(getchar()!='\n');}
    return(s);
    }
"""

"""
long sig_active=0;

sig_alon()
{
	extern int sig_occur();
	sig_active=1;	
	signal(SIGALRM,sig_occur);
	alarm(2);
}



unblock_alarm()
{
	extern int sig_occur();
	signal(SIGALRM,sig_occur);
	if(sig_active) alarm(2);
}

block_alarm()
{
	signal(SIGALRM,SIG_IGN);
}


sig_aloff()
{
	sig_active=0;	
	signal(SIGALRM,SIG_IGN);
	alarm(2147487643);
}

long interrupt=0;

sig_occur()
{
	extern char globme[];
	if(sig_active==0) return;
	sig_aloff();
	openworld();
	interrupt=1;
	rte(globme);
	interrupt=0;
	on_timing();
	closeworld();
	key_reprint();
	sig_alon();
}

set_progname(n,text)
char *text;
{
	/*
	int x=0;
	int y=strlen(argv_p[n])+strlen(argv_p[1]);  
	y++;
	if(strcmp(argv_p[n],text)==0) return;
	
	while(x<y)
	   argv_p[n][x++]=0; 
	strcpy(argv_p[n],text);
	*/
}
"""