# Object structure

# Name,
# Long Text 1
# Long Text 2
# Long Text 3
# Long Text 4
# statusmax
# Value
# flags (0=Normal 1+flannel)

# NOBS      World.Items
# OBMUL = 8

# numobs    World.Items
# long objinfo[NOBS*4];

# def inventory():

# Objinfo

# Loc
# Status
# Stamina
# Flag 1=carr 0=here

# def lobjsat(loc):
# def aobjsat(loc,mode):
# def iscontin(o1,o2):
# def fobnsys(nam, ctrl, ct_inf):
# def fobn(word):
# def fobna(word):
# def fobnin(word, ct):
# def fobnc(word):
# def fobncb(word, by):
# def fobnh(word):
# def getobj():

from ..models.item import by_here as ishere

# def iscarrby(item,user):
# def dropitem():

from ..models.item import list_items as lisobs
from ..models.item import list_here_by_flannel as lojal2

# def dumpitems():
# def dumpstuff(n,loc):

# long ublock[16*49];

# def whocom():
# def dispuser(ubase):
# def disle3(n,s):
# def disl4(n,s):

# def fpbn(name):


from ..models.character import by_name as fpbns
from ..models.character import list_characters as lispeople

# def usercom():

from ..models.item import oplong as oplong

"""
/*


 */

 inventory()
    {
    extern long mynum;
   bprintf("You are carrying\n");
    lobjsat(mynum);
    }

 /*
 Objinfo

 Loc
 Status
 Stamina
 Flag 1=carr 0=here
 */

lobjsat(loc)
{
aobjsat(loc,1);
}


aobjsat(loc,mode)  /* Carried Loc ! */
    {
    long a,b,c,d,e,f;
    char x[6],y[6];
    extern long debug_mode;
    b=0;
    c=0;
    d=0;
    e=0;
    f=0;
    while(c<NOBS)
       {
       if(((iscarrby(c,loc))&&(mode==1))||
((iscontin(c,loc))&&(mode==3)))
          {
          e=1;
              f+=1+strlen(oname(c));
if(debug_mode){ f+=5;sprintf(x,"%d",c);sprintf(y,"{%-3s}",x);}
if(isdest(c)) f+=2;
if(iswornby(c,loc)) f+=strlen("<worn> ");
          if(f>79)
             {
             f=0;
            bprintf("\n");
             }
if(isdest(c)) bprintf("(");
         bprintf("%s",oname(c));
         if(debug_mode) bprintf(y);
if(iswornby(c,loc)) bprintf(" <worn>");
if(isdest(c)) bprintf(")");
bprintf(" ");
          f++;
          }
       d+=4;
       c++;
       }
    if(!e)bprintf("Nothing");
   bprintf("\n");
    }


iscontin(o1,o2)
{
extern long my_lev;
if(ocarrf(o1)!=3) return(0)
;
if(oloc(o1)!=o2) return(0);
if((my_lev<10)&&(isdest(o1)))return(0);
return(1);
}

fobnsys(nam,ctrl,ct_inf)
char *nam;
long ctrl,ct_inf;
{
    extern char wd_it[];
    extern long mynum;
    long a;
    long l1[32],l2[32];
    extern char wordbuf[];
    strcpy(l1,nam);lowercase(l1);
    a=0;
if(!strcmp(l1,"red")) {brkword();return(4);}
if(!strcmp(l1,"blue")) {brkword();return(5);}
if(!strcmp(l1,"green")) {brkword();return(6);}
    while(a<NOBS)
       {
       strcpy(l2,oname(a));lowercase(l2);
       if(!strcmp(l1,l2))
          {
	  strcpy(wd_it,nam);
          switch(ctrl)
             {
             case 0:
                return(a);
             case 1:/* Patch for shields */
                if((a==112)&&(iscarrby(113,mynum))) return(113);
                if((a==112)&&(iscarrby(114,mynum))) return(114);
                if(isavl(a)) return(a);
                break;
             case 2:
                if(iscarrby(a,mynum)) return(a);
                break;
             case 3:
                if(iscarrby(a,ct_inf)) return(a);
                break
                ;
             case 4:
                if(ishere(a)) return(a);
                break;
             case 5:
                if(iscontin(a,ct_inf)) return(a);
                break;
             default:
                return(a);
                }
          }
       a++;
       }
    return(-1);
    }

 fobn(word)
 char *word;
    {
long x;
x=fobna(word);
if(x!=-1) return(x);
    return(fobnsys(word,0,0));
    }

 fobna(word)
 char *word;
    {
    return(fobnsys(word,1,0));
    }

 fobnin(word,ct)
 char *word;
 long ct;
 {
 	return(fobnsys(word,5,ct));	
 }

 fobnc(word)
 char *word;
    {
    return(fobnsys(word,2,0));
    }

 fobncb(word,by)
 char *word;
    {
    return(fobnsys(word,3,by));
    }

 fobnh(word)
 char *word;
    {
    return(fobnsys(word,4,0));
    }
    
 getobj()
    {
    extern long mynum;
    extern char globme[];
    extern long curch;
    extern char wordbuf[];
    long a,b;
    long i;
    long des_inf= -1;
    extern long stp;
    char bf[256];
    if(brkword()==-1)
       {
      bprintf("Get what ?\n");
       return;
       }
    a=fobnh(wordbuf);
    /* Hold */
    i=stp;
    strcpy(bf,wordbuf);
    if((brkword()!=-1)&&((strcmp(wordbuf,"from")==0)||(strcmp(wordbuf,"out")==0)))
    {
    	if(brkword()==-1)
    	{
    		bprintf("From what ?\n");
    		return;
    	}
    	des_inf=fobna(wordbuf);
    	if(des_inf==-1)
    	{
    		bprintf("You can't take things from that - it's not here\n");
    		return;
    	}
    	a=fobnin(bf,des_inf);
    }
    stp=i;
    if(a==-1)
       {
      bprintf("That is not here.\n");
       return;
       }
if((a==112)&&(des_inf==-1))
{
if(isdest(113)) a=113;
else if(isdest(114)) a=114;
if((a==113)||(a==114)) oclrbit(a,0);
else bprintf("The shields are all to firmly secured to the walls\n");
}
    if(obflannel(a)==1)
       {
      bprintf("You can't take that!\n");
       return;
       }
if(dragget()) return;
    if(!cancarry(mynum))
       {
      bprintf("You can't carry any more\n");
       return;
}
if((a==32)&&(state(a)==1)&&(ptothlp(mynum)==-1))
{
	bprintf("Its too well embedded to shift alone.\n");
	return;
}
    setoloc(a,mynum,1);
    sprintf(bf,"\001D%s\001\001c takes the %s\n\001",globme,oname(a));
   bprintf("Ok...\n");
    sendsys(globme,globme,-10000,curch,bf);
if(otstbit(a,12)) setstate(a,0);
if(curch==-1081) 
{
	setstate(20,1);
	bprintf("The door clicks shut....\n");
}
    }


 iscarrby(item,user)
    {
    extern long curch;
extern long my_lev;
    if((my_lev<10)&&(isdest(item)))return(0);
    if((ocarrf(item)!=1)&&(ocarrf(item)!=2)) return(0);
    if(oloc(item)!=user) return(0);
    return(1);
    }

 dropitem()
    {
    extern long mynum,curch;
    extern char wordbuf[],globme[];
    extern long my_sco;
    long a,b,bf[32];
    extern long my_lev;
    if(brkword()==-1)
       {
      bprintf("Drop what ?\n");
       return;
       }
    a=fobnc(wordbuf);
    if(a==-1)
       {
      bprintf("You are not carrying that.\n");
       return;
       }

if((my_lev<10)&&(a==32))
{
bprintf("You can't let go of it!\n");
return;
}
    setoloc(a,curch,0);
   bprintf("OK..\n");
    sprintf(bf,"\001D%s\001\001c drops the %s.\n\n\001",globme,wordbuf);
    sendsys(globme,globme,-10000,curch,bf);
    if((curch!=-183)&&(curch!=-5))return;
   sprintf(bf,"The %s disappears into the bottomless pit.\n",wordbuf);
   bprintf("It disappears down into the bottomless pit.....\n");
    sendsys(globme,globme,-10000,curch,bf);
    my_sco+=(tscale()*obaseval(a))/5;
    calibme();
setoloc(a,-6,0);
    }

 dumpitems()
    {
    extern long mynum;
    extern long curch;
    dumpstuff(mynum,curch);
    }

 dumpstuff(n,loc)
    {
    long b;
    b=0;
    while(b<NOBS)
       {
       if(iscarrby(b,n))

          {
          setoloc(b,loc,0);
          }
       b++;
       }
    }

long ublock[16*49];


 whocom()
    {
    long a;
    extern long my_lev;
    long bas;
    a=0;
    bas=16;
    if(my_lev>9)
       {
      bprintf("Players\n");
       bas=48;
       }
    while(a<bas)
       {
       if(a==16)bprintf("----------\nMobiles\n");
       if(!strlen(pname(a))) goto npas;
       dispuser(a);
       npas:a++;
       }
   bprintf("\n");
    }

 dispuser(ubase)
    {
extern long my_lev;
    if(pstr(ubase)<0) return; /* On  Non game mode */
    if(pvis(ubase)>my_lev) return;
if(pvis(ubase)) bprintf("(");
   bprintf("%s ",pname(ubase));
    disl4(plev(ubase),psex(ubase));
if(pvis(ubase)) bprintf(")");
if(ppos(ubase)==-2) bprintf(" [Absent From Reality]");
bprintf("\n");
    }

 disle3(n,s)
    {
    disl4(n,s);
   bprintf("\n");
    }
 disl4(n,s)
    {
    extern long hasfarted;
    switch(n)
       {
       case 1:
         bprintf("The Novice");
          break;
       case 2:
          if(!s)bprintf("The Adventurer");
          else
            bprintf("The Adventuress");
          break;
       case 3:
         bprintf("The Hero");
          if(s)bprintf("ine");
          break;
       case 4:
         bprintf("The Champion");
          break;
       case 5:
          if(!s)bprintf("The Conjurer");
          else
            bprintf("The Conjuress");
          break;
       case 6:
         bprintf("The Magician");
          break;
       case 7:
          if(s)bprintf("The Enchantress");
          else
            bprintf("The Enchanter");
          break;
       case 8:
          if(s)bprintf("The Sorceress");
          else
            bprintf("The Sorceror");
          break;
case 9:bprintf("The Warlock");
break;
       case 10:
          if(s)bprintf("The Apprentice Witch");
          else
            bprintf("The Apprentice Wizard");
          break;
case 11:bprintf("The 370");
break;
case 12:bprintf("The Hilbert-Space");
break;
case 14:bprintf("The Completely Normal Naughty Spud");
break;
case 15:bprintf("The Wimbledon Weirdo");
break;
case 16:bprintf("The DangerMouse");
break;
case 17:bprintf("The Charred Wi");
if(s) bprintf("tch");
else bprintf("zard");
break;
case 18:bprintf("The Cuddly Toy");
break;
case 19:if(!hasfarted) bprintf("Of The Opera");
else bprintf("Raspberry Blower Of Old London Town");
break;
case 20:bprintf("The 50Hz E.R.C.S");
break;
case 21:bprintf("who couldn't decide what to call himself");
break;
case 22:bprintf("The Summoner");
break;
case 10000:
bprintf("The 159 IQ Mega-Creator");
break;
case 10033:
case 10001:bprintf("The Arch-Wi");
if(s)bprintf("tch");
else bprintf("zard");
break;
case 10002:bprintf("The Wet Kipper");
break;
case 10003:bprintf("The Thingummy");
break;
case 68000:
bprintf("The Wanderer");
break;
case -2:
bprintf("\010");
break;
case -11:bprintf("The Broke Dwarf");break;
case -12:bprintf("The Radioactive Dwarf");break;
case -10:bprintf("The Heavy-Fan Dwarf");break;
case -13:bprintf("The Upper Class Dwarven Smith");break;
case -14:bprintf("The Singing Dwarf");break;
case -30:bprintf("The Sorceror");break;
case -31:bprintf("the Acolyte");break;
       default:
         bprintf("The Cardboard Box");
          break;
          }
    }
fpbn(name)
char *name;
{
long s;
extern char wd_them[],wd_him[],wd_her[],wd_it[];
s=fpbns(name);
if(s==-1) return(s);
if(!seeplayer(s)) return(-1);
return(s);
}

usercom()
{
extern long my_lev;
long a;
a=my_lev;
my_lev=0;
whocom();
my_lev=a;
}
"""
