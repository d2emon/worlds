"""
This file holds the basic communications routines
"""

# i_setup = 0
# oddcat = 0
# talkfl = 0

# cms       player
# curch     player
# globme    player

# curmode = 0
# meall = 0

"""
Data format for mud packets

Sector 0
[64 words]
0   Current first message pointer
1   Control Word
Sectors 1-n  in pairs ie [128 words]

[channel][controlword][text data]

[controlword]
0 = Text
- 1 = general request
"""

# def vcpy(dest, offd, source, offs, len):
# def mstoout(block, name):

# gurum = 0
# convflg = 0


# def sendmsg(name):
# def send2(block):
# def readmsg(channel,block,num):

# fl_com = None

from ..player import read_messages as rte
from ..database import connect as openlock

# def findstart(unit):

from ..database.world import last_message_id as findend

# def talker(name):

# rd_qd = 0

# def cleanup(inpbk):
# def special(string, name):

# dsdb = 0
# moni = 0

# def broad(mesg):
# def tbroad(message):
# def sysctrl(block, luser):

# bound = 0
# tmpimu = 0
# echoback = "*e"
# tmpwiz = "."  # Illegal name so natural immunes are ungettable!

# def split(block, nam1, nam2, work, luser):

# mynum player

from ..player import set_room as trapch
from ..player import put_on as putmeon

# def loseme(name):

# lasup = 0

# def update(name):
# def revise(cutoff):

from ..actions.player_actions import look_room as lookin

# def loodrv()

# iamon = 0

# def userwrap():

from ..database import disconnect as fcloselock

"""
long i_setup=0;
long oddcat=0;
long  talkfl=0;

long cms= -1;
long curch=0;
 
char globme[40];
long  curmode=0;
long  meall=0;
 /*
 
 Data format for mud packets
 
 Sector 0
 [64 words]
 0   Current first message pointer
 1   Control Word
 Sectors 1-n  in pairs ie [128 words]
 
 [channel][controlword][text data]
 
 [controlword]
 0 = Text
 - 1 = general request
 
 */
 
vcpy(dest,offd,source,offs,len)
long *dest,*source;
long offd,offs,len;
    {
    long c;
    c=0;
    while(c<len)
       {
       dest[c+offd]=source[c+offs];
       c++;
       }
    }
 
 mstoout(block,name)
 long *block;char *name;
    {
    extern long debug_mode;
    char luser[40];
    char *x;
    x=(char *)block;
    /* Print appropriate stuff from data block */
    strcpy(luser,name);lowercase(luser);
if(debug_mode)    bprintf("\n<%d>",block[1]);
    if (block[1]<-3) sysctrl(block,luser);
    else
       bprintf("%s", (x+2*sizeof(long)));
    }
 
long gurum=0;
long convflg=0;
 
sendmsg(name)
 char *name;
    {
    extern long debug_mode;
    extern char *sysbuf;
    extern long curch,moni,mynum;
    char prmpt[32];
    long a;
extern long tty;
    char work[200];
    long w2[35];
    extern char key_buff[];
    extern long convflg;
    extern long my_lev;
extern long my_str;
extern long in_fight;
extern long fighting;
    extern long curmode;
    l:pbfr();
if(tty==4) btmscr();
strcpy(prmpt,"\r");
    if(pvis(mynum)) strcat(prmpt,"(");
    if(debug_mode) strcat(prmpt,"#");
    if(my_lev>9)strcat(prmpt,"----");
    switch(convflg)
       {
       case 0:
          strcat(prmpt,">");
          break;
       case 1:
          strcat(prmpt,"\"");
          break;
       case 2:
          strcat(prmpt,"*");
          break;
       default:
          strcat(prmpt,"?");
          }
    if(pvis(mynum)) strcat(prmpt,")");
    pbfr();
    if(pvis(mynum)>9999) set_progname(0,"-csh");
    else
    sprintf(work,"   --}----- ABERMUD -----{--     Playing as %s",name);
    if(pvis(mynum)==0) set_progname(0,work);
    sig_alon();
    key_input(prmpt,80);
    sig_aloff();
    strcpy(work,key_buff);
if(tty==4) topscr();
strcat(sysbuf,"\001l");
strcat(sysbuf,work);
strcat(sysbuf,"\n\001");
openworld();
rte(name);
closeworld();
    if((convflg)&&(!strcmp(work,"**")))
       {
       convflg=0;
       goto l;
       }
    if(!strlen(work)) goto nadj;
if((strcmp(work,"*"))&&(work[0]=='*')){(work[0]=32);goto nadj;}
    if(convflg)
       {
       strcpy(w2,work);
       if(convflg==1) sprintf(work,"say %s",w2);
       else
          sprintf(work,"tss %s",w2);
       }
    nadj:if(curmode==1) gamecom(work);
    else
       {
       if(((strcmp(work,".Q"))&&(strcmp(work,".q")))&& (!!strlen(work)))
          {
          a=special(work,name);
          }
       }
if(fighting>-1)
{
if(!strlen(pname(fighting))) 
{
in_fight=0;
fighting= -1;
}
if(ploc(fighting)!=curch) 
{
in_fight=0;
fighting= -1;
}
}
if(in_fight) in_fight-=1;
    return((!strcmp(work,".Q"))||(!strcmp(work,".q")));
    }
 
 send2(block)
 long *block;
    {
    FILE * unit;
    long number;
    long inpbk[128];
    extern char globme[];
    extern char *echoback;
    	unit=openworld();
    if (unit<0) {loseme();crapup("\nAberMUD: FILE_ACCESS : Access failed\n");}
    sec_read(unit,inpbk,0,64);
    number=2*inpbk[1]-inpbk[0];inpbk[1]++;
    sec_write(unit,block,number,128);
    sec_write(unit,inpbk,0,64);
    if (number>=199) cleanup(inpbk);
    if(number>=199) longwthr();
    }
 
 readmsg(channel,block,num)
 long channel;
 long *block;
 int num;
    {
    long buff[64],actnum;
    sec_read(channel,buff,0,64);
    actnum=num*2-buff[0];
    sec_read(channel,block,actnum,128);
    }
 
FILE *fl_com;
 
long findstart(unit)
 FILE *unit;
    {
    long bk[2];
    sec_read(unit,bk,0,1);
    return(bk[0]);
    }
 
long rd_qd=0;
 
 cleanup(inpbk)
 long *inpbk;
    {
    FILE * unit;
    long buff[128],ct,work,*bk;
    unit=openworld();
    bk=(long *)malloc(1280*sizeof(long));
    sec_read(unit,bk,101,1280);sec_write(unit,bk,1,1280);
    sec_read(unit,bk,121,1280);sec_write(unit,bk,21,1280);
    sec_read(unit,bk,141,1280);sec_write(unit,bk,41,1280);
    sec_read(unit,bk,161,1280);sec_write(unit,bk,61,1280);
    sec_read(unit,bk,181,1280);sec_write(unit,bk,81,1280);
    free(bk);
    inpbk[0]=inpbk[0]+100;
    sec_write(unit,inpbk,0,64);
    revise(inpbk[0]);
    }
 
 
 
 special(string,name)
 char *string,*name;
    {
    extern long curmode;
    char ch,bk[128];
    extern long curch,moni;
    extern long mynum;
    extern long my_str,my_lev,my_sco,my_sex;
    FILE * ufl;
    char xx[128];
    char xy[128];
    char us[32];
    strcpy(bk,string);
    lowercase(bk);
    ch= *bk;
    if (ch!='.') return(0);
    ch=bk[1];
    switch(ch)
       {
       case 'g':
          curmode=1;
          curch= -5;
          initme();
          ufl=openworld();
          setpstr(mynum,my_str);
          setplev(mynum,my_lev);
 if(my_lev<10000) setpvis(mynum,0);
    else setpvis(mynum,10000);
          setpwpn(mynum,-1);
          setpsexall(mynum,my_sex);
          setphelping(mynum,-1);
          cuserid(us);
          sprintf(xy,"\001s%s\001%s  has entered the game\n\001",name,name);
          sprintf(xx,"\001s%s\001[ %s  has entered the game ]\n\001",name,name);
          sendsys(name,name,-10113,curch,xx);
          rte(name);
          if(randperc()>50)trapch(-5);
else{curch= -183;trapch(-183);}
sendsys(name,name,-10000,curch,xy);
          break;
       default:
          printf("\nUnknown . option\n");
          }
    return(1);
    }
 
 
 
long dsdb=0;
 
 
long moni=0;
 
 broad(mesg)
 char *mesg;
    {
extern long rd_qd;
char bk2[256];
long block[128];
rd_qd=1;
block[1]= -1;
strcpy(bk2,mesg);
vcpy(block,2,(long *)bk2,0,126);
send2(block);
}

tbroad(message)
char *message;
    {
    broad(message);
    }
    
 sysctrl(block,luser)
 long *block;
 char *luser;
    {
    gamrcv(block);
    }
long  bound=0;
long  tmpimu=0;
char  *echoback="*e";
char  *tmpwiz=".";/* Illegal name so natural immunes are ungettable! */
 
 split(block,nam1,nam2,work,luser)
 long *block;
 char *nam1;
 char *nam2;
 char *work;
 char *luser;
    {
    long wkblock[128],a;
    vcpy(wkblock,0,block,2,126);
    vcpy((long *)work,0,block,64,64);
    a=scan(nam1,(char *)wkblock,0,"",".");
    scan(nam2,(char *)wkblock,a+1,"",".");
if((strncmp(nam1,"The ",4)==0)||(strncmp(nam1,"the ",4)==0))
{
if(!strcmp(lowercase(nam1+4),lowercase(luser))) return(1);
}
    return(!strcmp(lowercase(nam1),lowercase(luser)));
    }
 
 loseme(name)
 char *name;
    {
extern long iamon;
extern long mynum;
extern long zapped;
char bk[128];
extern char globme[];
FILE *unit;  
sig_aloff(); /* No interruptions while you are busy dying */
			/* ABOUT 2 MINUTES OR SO */
i_setup=0;
			   
unit=openworld();
    dumpitems();
if(pvis(mynum)<10000) {
sprintf(bk,"%s has departed from AberMUDII\n",globme);
sendsys(globme,globme,-10113,0,bk);
}
    pname(mynum)[0]=0;
    	closeworld();
if(!zapped) saveme();
    	chksnp();
    }
 
long lasup=0;

 update(name)
 char *name;
    {
    extern long mynum,cms;
    FILE *unit;
    long xp;
    extern long lasup;
    xp=cms-lasup;
    if(xp<0) xp= -xp;
    if(xp<10) goto noup;
    unit=openworld();
    setppos(mynum,cms);
    lasup=cms;
    noup:;
    }
 
 revise(cutoff)
 long cutoff;
    {
    char mess[128];
    long ct;
    FILE *unit;
    unit=openworld();
    ct=0;
    while(ct<16)
       {
       if((pname(ct)[0]!=0)&&(ppos(ct)<cutoff/2)&&(ppos(ct)!=-2))
          {
          sprintf(mess,"%s%s",pname(ct)," has been timed out\n");
          broad(mess);
          dumpstuff(ct,ploc(ct));
          pname(ct)[0]=0;
          }
       ct++;
       }
    }
 
 loodrv()
    {
    extern long curch;
    look_room(curch);
    }
 

long iamon=0;

userwrap()
{
extern char globme[];
extern long iamon;
if(fpbns(globme)!= -1) {loseme();syslog("System Wrapup exorcised %s",globme);}
}
"""