# The next part of the universe...

"""
Weather Routines

Current weather defined by state of object 47

states are

0   Sunny
1   Rain
2   Stormy
3   Snowing
"""

# def setwthr(n):
# def suncom():
# def raincom():
# def stormcom():
# def snowcom():
# def blizzardcom():
# def adjwthr(n):
# def longwthr():
# def wthrrcv(type):

from ..models.item import show_weather as showwthr
from ..models.room import outdoors as outdoors

# Silly Section

# def sillycom(txt):
# def laughcom():
# def purrcom():
# def crycom():
# def sulkcom():
# def burpcom():
# def hiccupcom():

# hasfarted = 0;

# def fartcom():
# def grincom():
# def smilecom():
# def winkcom():
# def sniggercom():
# def posecom():
# def emotecom():
# def praycom():
# def yawncom():
# def groancom():
# def moancom():
# def cancarry(plyr):
# def setcom():

from ..actions.player_actions import is_dark as isdark
from ..models.item import get_weather_id as modifwthr

# def setpflags():


"""
#include <stdio.h>
#include "files.h"
extern FILE *openlock();
extern FILE *openuaf();
extern FILE *openroom();
extern FILE *openworld();
extern char *oname();
extern char *pname();
extern char globme[];
extern char wordbuf[];


 /*
 
 The next part of the universe...
 
 
 */
 
 /*
 
 Weather Routines
 
 Current weather defined by state of object 47
 
 states are
 
 0   Sunny
 1   Rain
 2   Stormy
 3   Snowing
 
 */
 
 
 setwthr(n)
    {
    extern long my_lev;
    if(my_lev<10)
       {
       bprintf("What ?\n");
       return;
       }
    adjwthr(n);
    }
 
 suncom()
    {
    setwthr(0);
    }
 
 raincom()
    {
    setwthr(1);
    }
 
 stormcom()
    {
    setwthr(2);
    }
 
 snowcom()
    {
    setwthr(3);
    }
 
 blizzardcom()
    {
    	setwthr(4);
    }
 adjwthr(n)
    {
    long x;
    extern char globme[];
    extern long curch;
    x=state(0);
    setstate(0,n);
    if(x!=n) sendsys(globme,globme,-10030,n,"");
    }
 
 longwthr()
    {
    long a;
    a=randperc();
    if(a<50)
       {
       adjwthr(1);
       return;
       }
    if(a>90)
       {
       adjwthr(2);
       return;
       }
    adjwthr(0);
    return;
    }
 
 
 wthrrcv(type)
    {
    if(!outdoors()) return;
    type=modifwthr(type);
    switch(type)
       {
       case 0:
          bprintf("\001cThe sun comes out of the clouds\n\001");
          break;
       case 1:
          bprintf("\001cIt has started to rain\n\001");
          break;
       case 2:
          break;
       case 3:
          bprintf("\001cIt has started to snow\n\001");
          break;
       case 4:
          bprintf("\001cYou are half blinded by drifting snow, as a white, icy blizzard sweeps across\nthe land\n\001");
          break;
          }
    } 
 
 /* Silly Section */
 
 sillycom(txt)
 char *txt;
    {
    extern char globme[];
    extern long curch;
    char bk[256];
    sprintf(bk,txt,globme,globme);
    sendsys(globme,globme,-10000,curch,bk);
    }
 
 laughcom()
    {
    if(chkdumb()) return;
    sillycom("\001P%s\001\001d falls over laughing\n\001");
    bprintf("You start to laugh\n");
    }
 
 purrcom()
    {
    if(chkdumb()) return;
    sillycom("\001P%s\001\001d starts purring\n\001");
    bprintf("MMMMEMEEEEEEEOOOOOOOWWWWWWW!!\n");
    }
  
 crycom()
    {
    if(chkdumb()) return;
    sillycom("\001s%s\001%s bursts into tears\n\001");
    bprintf("You burst into tears\n");
    }
 
 sulkcom()
    {
    sillycom("\001s%s\001%s sulks\n\001");
    bprintf("You sulk....\n");
    }
 
 burpcom()
    {
    if(chkdumb()) return;
    sillycom("\001P%s\001\001d burps loudly\n\001");
    bprintf("You burp rudely\n");
    }
 
 hiccupcom()
    {
    if(chkdumb()) return;
    sillycom("\001P%s\001\001d hiccups\n\001");
    bprintf("You hiccup\n");
    }
 
long hasfarted=0;

fartcom()
    {
    extern long hasfarted;
    hasfarted=1;
    sillycom("\001P%s\001\001d lets off a real rip roarer\n\001");
    bprintf("Fine...\n");
    }
 
 grincom()
    {
    sillycom("\001s%s\001%s grins evilly\n\001");
    bprintf("You grin evilly\n");
    }
 
 smilecom()
    {
    sillycom("\001s%s\001%s smiles happily\n\001");
    bprintf("You smile happily\n");
    }
 
 winkcom()
    {					/* At person later maybe ? */
    sillycom("\001s%s\001%s winks suggestively\n\001");
    bprintf("You wink\n");
    }
 
 sniggercom()
    {
    if(chkdumb()) return;
    sillycom("\001P%s\001\001d sniggers\n\001");
    bprintf("You snigger\n");
    }
 
 posecom()
    {
    long a;
    extern long my_lev;
    if(my_lev<10)
       {
       bprintf("You are just not up to this yet\n");
       return;
       }
    time(&a);
    srand(a);
    a=randperc();
    a=a%5;
    bprintf("POSE :%d\n",a);
    switch(a)
       {
       case 0:
          break;
       case 1:
	sillycom("\001s%s\001%s throws out one arm and sends a huge bolt of fire high\n\
into the sky\n\001");
          broad("\001cA massive ball of fire explodes high up in the sky\n\001");
          break;
       case 2:
          sillycom("\001s%s\001%s turns casually into a hamster before resuming normal shape\n\001");
          break;
       case 3:
          sillycom("\001s%s\001%s \
starts sizzling with magical energy\n\001");
          break;
       case 4:
          sillycom("\001s%s\001%s begins to crackle with magical fire\n\001");
          break;
          }
    }

 emotecom()
 /*
  (C) Jim Finnis
 */
 {
 	extern long my_lev;
 	char buf[100];
 	strcpy(buf,"\001P%s\001 ");
 	getreinput(buf+6);
 	strcat(buf,"\n");
 	if (my_lev<10000)
 		bprintf("Your emotions are strictly limited!\n");
	else
		sillycom(buf);
}
		
 praycom()
    {
    extern long curch;
    sillycom("\001s%s\001%s falls down and grovels in the dirt\n\001");
    bprintf("Ok\n");
    }

 yawncom()
    {
    sillycom("\001P%s\001\001d yawns\n\001");
    }
 
 groancom()
    {
    sillycom("\001P%s\001\001d groans loudly\n\001");
    bprintf("You groan\n");
    }
 
 moancom()
    {
    sillycom("\001P%s\001\001d starts making moaning noises\n\001");
    bprintf("You start to moan\n");
    }
 
 cancarry(plyr)
    {
    extern long numobs;
    long a,b;
    a=0;
    b=0;
    if(plev(plyr)>9) return(1);
    if(plev(plyr)<0) return(1);
    while(a<numobs)
       {
       if((iscarrby(a,plyr))&&(!isdest(a))) b++;
       a++;
       }
    if(b<plev(plyr)+5) return(1);
    return(0);
    }
 
 
 setcom()
    {
    long a,b,c;
    extern long my_lev;
    extern char wordbuf[];
    if(brkword()== -1)
       {
       bprintf("set what\n");
       return;
       }
    if(my_lev<10)
       {
       bprintf("Sorry, wizards only\n");
       return;
       }
    a=fobna(wordbuf);
    if(a== -1)
       {
         goto setmobile;
       }
    if(brkword()== -1)
       {
       bprintf("Set to what value ?\n");
       return;
       }
       if(strcmp(wordbuf,"bit")==0) goto bitset;
       if(strcmp(wordbuf,"byte")==0) goto byteset;
    b=numarg(wordbuf);
    if(b>omaxstate(a))
       {
       bprintf("Sorry max state for that is %d\n",omaxstate(a));
       return;
       }
    if(b<0)
       {
       bprintf("States start at 0\n");
       return;
       }
    setstate(a,b);
    return;
bitset:if(brkword()==-1)
       {
       	   bprintf("Which bit ?\n");
       	   return;
       	}
       	b=numarg(wordbuf);
       	if(brkword()==-1)
       	{
       	   bprintf("The bit is %s\n",otstbit(a,b)?"TRUE":"FALSE");
       	   return;
       	}
       	c=numarg(wordbuf);
       	if((c<0)||(c>1)||(b<0)||(b>15))
       	{
       		bprintf("Number out of range\n");
       		return;
       	}
       	if(c==0) oclrbit(a,b);
       	else osetbit(a,b);
       	return;
byteset:if(brkword()==-1)
       {
       	   bprintf("Which byte ?\n");
       	   return;
       	}
       	b=numarg(wordbuf);
       	if(brkword()==-1)
       	{
       	   bprintf("Current Value is : %d\n",obyte(a,b));
       	   return;
       	}
       	c=numarg(wordbuf);
       	if((b<0)||(b>1)||(c<0)||(c>255))
       	{
       		bprintf("Number out of range\n");
       		return;
       	}
	osetbyte(a,b,c);
       	return;       
setmobile:a=fpbn(wordbuf);
           if(a==-1)
           {
           	bprintf("Set what ?\n");
           	return;
           }
           if(a<16)
           {
           	bprintf("Mobiles only\n");
           	return;
           }
           if(brkword()==-1)
           {
           	bprintf("To what value ?\n");
           	return;
           }
           b=numarg(wordbuf);
           setpstr(a,b);
    }
 
 
 
setpflags()
{
	long a,b,c,d;
	extern long mynum;
	extern char wordbuf[];
	if(!ptstbit(mynum,2))
	{
		bprintf("You can't do that\n");
		return;
	}
	if(brkword()==-1) 
	{
		bprintf("Whose PFlags ?\n");
		return;
	}
	a=fpbn(wordbuf);
	if(a==-1)
	{
		bprintf("Who is that ?\n");
		return;
	}
	if(brkword()==-1)
	{
		bprintf("Flag number ?\n");
		return;
	}
	b=numarg(wordbuf);
	if(brkword()==-1)
	{
		bprintf("Value is %s\n",ptstflg(a,b)?"TRUE":"FALSE");
		return;
	}
	c=numarg(wordbuf);
	if((c<0)||(c>1)||(b<0)||(b>31))
	{
		bprintf("Out of range\n");
		return;
	}
	if(c) psetflg(a,b);
	else pclrflg(a,b);
}
"""
