# def on_timing():

from ..player import on_look as onlook
from ..player import check_fight as chkfight
from ..player import check_move as consid_move

# def crashcom():
# def singcom():
# def spraycom():

# More new stuff */

# def dircom():
# def sys_reset():
from ..item import do_rune as dorune
# def pepdrop():
# def dragget():

from ..player import check_help as helpchkr


"""
on_timing()
{
	if(randperc()>80) onlook();
}

 crashcom(  )
    {
    extern long my_lev ;
    if( my_lev<10 )
       {
       bprintf( "Hmmm....\n" ) ;
       bprintf( "I expect it will sometime\n" ) ;
       return ;
       }
    bprintf( "Bye Bye Cruel World...\n" ) ;
    sendsys( "", "", -666, 0, "" ) ;
    rescom(  ) ;
    }
 
 singcom(  )
    {
    if( chkdumb(  ) ) return ;
    sillycom( "\001P%s\001\001d sings in Gaelic\n\001" ) ;
    bprintf( "You sing\n" ) ;
    }
 
 spraycom(  )
    {
    long a, b ;
    long c ;
    char bk[ 128 ] ;
    extern long wordbuf[  ] ;
    extern long mynum ;
    extern long curch ;
    b=vichere( &a ) ;
    if( b== -1 ) return ;
    if( brkword(  )== -1 )
       {
       bprintf( "With what ?\n" ) ;
       return ;
       }
    if( !strcmp( wordbuf, "with" ) )
       {
       if( brkword(  )== -1 )
          {
          bprintf( "With what ?\n" ) ;
          return ;
          }
       }
    c=fobna( wordbuf ) ;
    if( c== -1 )
       {
       bprintf( "With what ?\n" ) ;
       return ;
       }
    switch( c )
       {
       default:
          bprintf( "You can't do that\n" ) ;
          break ;
          }
    return ;
    }
 
 /* More new stuff */
 
 dircom(  )
    {
    long a ;
    char b[ 40 ] ;
    char d[ 40 ] ;
    long c ;
    extern long my_lev ;
    extern long numobs ;
    if( my_lev<10 )
       {
       bprintf( "That's a wiz command\n" ) ;
       return ;
       }
    a=0 ;
    while( a<numobs )
       {
       c=findzone( oloc( a ), b ) ;
       sprintf( d, "%s%d", b, c ) ;
       if( ocarrf( a ) ) strcpy( d, "CARRIED" ) ;
       if( ocarrf( a )==3 ) strcpy( d, "IN ITEM" ) ;
       bprintf( "%-13s%-13s", oname( a ), d ) ;
       if( a%3==2 )bprintf( "\n" ) ;
       if( a%18==17 ) pbfr(  ) ;
       a++ ;
       }
    bprintf( "\n" ) ;
    }
 
 sys_reset(  )
    {
    extern long my_lev ;
    char xx[ 128 ] ;
    FILE *fl ;
    long t, u ;
    if( tscale(  )!=2 )
       {
       bprintf( "There are other people on.... So it wont work!\n" ) ;
       return ;
       }
    time( &t ) ;
    fl=openlock( RESET_N, "ruf" ) ;
    if(fl==NULL) goto errk;
    fscanf( fl, "%ld", &u ) ;
    fclose(fl ) ;
    if( ( t-u<( 3600 ) )&&( u<t ) )
       {
       bprintf( "Sorry at least an hour must pass between resets\n" ) ;
       return ;
       }
errk:t=my_lev ;
    my_lev=10 ;
    rescom(  ) ;
    my_lev=t ;
    }
 
 
 pepdrop(  )
    {
    extern long my_sco ;
    long a, b ;
    extern char globme[];
    extern long mynum ;
    extern long curch ;
    sendsys( " ", " ", -10000, curch, "You start sneezing ATISCCHHOOOOOO!!!!\n" ) ;
    if( ( !strlen( pname( 32 ) ) )||( ploc( 32 )!=curch ) )
    return ;
    /* Ok dragon and pepper time */
    if( ( iscarrby( 89, mynum ) )&&( ocarrf( 89 )==2 ) )
       {
       /* Fried dragon */
       strcpy( pname( 32 ), "" ) ; /* No dragon */
       my_sco+=100 ;
       calibme(  ) ;
       return ;
       }
    else
       {
       /* Whoops !*/
       bprintf( "The dragon sneezes forth a massive ball of flame.....\n" ) ;
       bprintf( "Unfortunately you seem to have been fried\n" ) ;
       loseme(  ) ;
       crapup( "Whoops.....   Frying tonight" ) ;
       }
    }
 
 dragget(  )
    {
    extern long curch, my_lev ;
    long a, b ;
long l ;
if( my_lev>9 ) return( 0 ) ;
l=fpbns( "dragon" ) ;
if( l== -1 ) return( 0 ) ;
    if( ploc( l )!=curch ) return( 0 ) ;
    return( 1 ) ;
    }
"""