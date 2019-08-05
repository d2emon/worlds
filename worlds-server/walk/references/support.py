# Some more basic functions

# Note

# state(obj)
# setstate(obj,val)
# destroy(obj)

# are elsewhere

# In Character DB
# def pname(chr):
# def pchan(chr):
# def ploc(chr):
# def setploc(chr,n):
# def ppos(chr):
# def setppos(chr,v):
# def pstr(chr):
# def setpstr(chr,v):
# def pvis(chr):
# def setpvis(chr,v):
# def psexall(chr):
# def setpsexall(chr,v):
# def plev(chr):
# def setplev(chr,v):
# def pwpn(chr):
# def setpwpn(chr,n):
# def phelping(x,y):
# def setphelping(x,y):
# Character Flags
# def psex(chr):
# def setpsex(chr,v):

# In Item DB

# def oloc(ob):
# def setoloc(ob,l,c):
# def ocarrf(ob):
# def setocarrf(ob, v):

# In ItemData DB

# def oname(ob):
# def  olongt(ob, st):
# def omaxstate(ob):
# def obflannel(ob): # Old version
# def oflannel(ob):
# def obaseval(ob):

# def isdest(ob):
# def isavl(ob):
# def ospare(ob):
# def ocreate(ob):
# def osetbit(ob,x):
# def oclearbit(ob,x):
# def oclrbit(ob,x):
# def otstbit(ob,x):
# def osetbyte(o,x,y):
# def obyte(o,x):
# def ohany(mask):
# def ptothlp(pl):
# def psetflg(ch,x):
# def pclrflg(ch,x):

# Pflags

# 0 sex
# 1 May not be exorcised ok
# 2 May change pflags ok
# 3 May use rmedit ok
# 4 May use debugmode ok
# 5 May use patch
# 6 May be snooped upon

# def ptstbit(ch,x):
# def ptstflg(ch,x):

"""
 isdest(ob)
    {
    if(otstbit(ob,0))return(1);
    return(0);
    }

 isavl(ob)
    {
    extern long mynum;
    if(ishere(ob)) return(1);
    return(iscarrby(ob,mynum));
    }

 ospare(ob)
    {
    return(otstbit(ob,0)?-1:0);
    }

ocreate(ob)
{
oclrbit(ob,0);
}

osetbit(ob,x)
{
extern long objinfo[];
bit_set(&(objinfo[4*ob+2]),x);
}
oclearbit(ob,x)
{
extern long objinfo[];
bit_clear(&(objinfo[4*ob+2]),x);
}
oclrbit(ob,x)
{
oclearbit(ob,x)
;
}
otstbit(ob,x)
{
extern long objinfo[];
return(bit_fetch(objinfo[4*ob+2],x));
}
osetbyte(o,x,y)
{
extern long objinfo[];
byte_put(&(objinfo[4*o+2]),x,y);
}
obyte(o,x)
{
extern long objinfo[];
return(byte_fetch(objinfo[4*o+2],x));
}
ohany(mask)
long mask;
{
extern long numobs;
auto a;
extern long mynum;
extern long objinfo[];
a=0;
mask=mask<<16;
while(a<numobs)
{
if(((iscarrby(a,mynum))||(ishere(a,mynum)))&&(objinfo[4*a+2]&mask))return(1);
a++;
}
return(0);
}

ptothlp(pl)
{
int tot;
extern long maxu;
int ct=0;
while(ct<maxu)
{
if(ploc(ct)!=ploc(pl)){ct++;continue;}
if(phelping(ct)!=pl){ct++;continue;}
return(ct);
}
return(-1);
}


psetflg(ch,x)
long ch;
long x;
{
	extern long ublock[];
	ublock[16*ch+9]|=(1<<x);
}

pclrflg(ch,x)
long ch;
long x;
{
	extern long ublock[];
	ublock[16*ch+9]&=~(1<<x);
}

ptstbit(ch,x)
long ch;
long x;
{
	return(ptstflg(ch,x));
}


ptstflg(ch,x)
long ch;
long x;
{
	extern long ublock[];
	extern char globme[];
	if((x==2)&&(strcmp(globme,"Debugger")==0)) return(1<<x);
	return(ublock[16*ch+9]&(1<<x));
}
"""
