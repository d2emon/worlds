# Zone based name generator

# class Zone:

# zoname = []

from ..room import find_zone as findzone

# ex_dat    Room

from ..player import list_exits as exits

# dirns     Exits

from ..database.rooms import parse_exits as lodex

# def roomnum(str, offstr):

from ..room import show_name as showname

# def loccom():

"""
#include <stdio.h>

 /*
 Zone based name generator
 */

struct zone
{
	char *z_name ;
	long z_loc ;
} ;

typedef struct zone ZONE ;

ZONE zoname[  ]={
    
    } ;

char *dirns[  ]={"North", "East ", "South", "West ", "Up   ", "Down "} ;

 lodex( file )
 FILE *file;
    {
    long a ;
    extern long ex_dat[] ;
    a=0 ;
    while( a<6 )
       {
       fscanf(file," %ld ",&ex_dat[ a ]);
       a++ ;
       }
    }
 roomnum( str, offstr )
 char *str;
 char *offstr;
    {
    long a, b, c ;
    long d ;
    extern ZONE zoname[] ;
    extern char wd_there[];
    char w[64] ;
    b=0 ;c=0 ;
    a=0 ;
    while( b<99990 )
       {
       strcpy( w, zoname[ a ].z_name ) ;lowercase( w ) ;
       if( !strcmp( w, str ) ) goto fnd1 ;
       b=zoname[ a ].z_loc ;
       a++ ;
       }
    return( 0 ) ;
    fnd1: ;
    c=zoname[ a ].z_loc ;
    sscanf(offstr,"%ld",&d);
    if( !strlen( offstr ) ) d=1 ;
    sprintf(wd_there,"%s %s",str,offstr);
    if( d==0 ) return( 0 ) ;
    if( d+b>c ) return( 0 ) ;
    return( -( d+b ) ) ;
    }
 loccom(  )
    {
    extern long my_lev ;
    extern ZONE zoname[] ;
    long a ;
    a=0 ;
if( my_lev<10 )
{
bprintf( "Oh go away, thats for wizards\n" ) ;
return ;
}
    bprintf( "\nKnown Location Nodes Are\n\n" ) ;
    l1:bprintf( "%-20s", zoname[ a].z_name ) ;
    if( a%4==3 ) bprintf( "\n" ) ;
    if( zoname[ a++ ].z_loc!=99999 ) goto l1 ;
    bprintf( "\n" ) ;
    }
"""
