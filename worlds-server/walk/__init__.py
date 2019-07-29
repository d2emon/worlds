class CommandException(Exception):
    pass


class User:
    brmode = False


def look_room(room_id, brmode=None):
    if brmode is None:
        brmode = User.brmode

    room = Room(room_id)
    closeworld()
    if ail_blind:
        # raise CommandException("You are blind... you can't see a thing!")
        yield "You are blind... you can't see a thing!"
    if my_lev > 9:
        room.showname()
    un1 = room.open("r")
    if un1:
        # xx1
        xxx = 0
        un1.lodex()
        if is_dark():
            un1.close()
            yield "It is dark\n"
            openworld()
            onlook()
            return

        for s in  un1:
            """
            """

    """
    if (un1!=NULL)
    {

       while(getstr(un1,str)!=0)
          {
          if(!strcmp(str,"#DIE"))
             {
             if(ail_blind) {rewind(un1);ail_blind=0;goto xx1;}
             if(my_lev>9)bprintf("<DEATH ROOM>\n");
             else
                {
                loseme(globme);
                crapup("bye bye.....\n");
                }
             }
          else
{
if(!strcmp(str,"#NOBR")) brmode=0;
else
             if((!ail_blind)&&(!xxx))bprintf("%s\n",str);
          xxx=brmode;
}
          }
       }
    else
       bprintf("\nYou are on channel %d\n",room);
    fclose(un1);
    openworld();
    if(!ail_blind)
    {
	    lisobs();
	    if(curmode==1) lispeople();
    }
    bprintf("\n");
    onlook();
    """
