from .database import World
from .exceptions import ActionError
from .player import Player
from .room import look_room, go_direction


class Globals:
    my_lev = 0
    in_fight = 0


def go(parser):
    word = next(parser)
    if word is None:
        raise ActionError("GO where?")
    return go_direction(parser.get_direction_id(word))


def look(parser):
    def __look():
        return look_room(Player.room_id)

    def __look_at():
        return examcom()

    def __look_in(container):
        if container is None:
            raise ActionError("In what ?")

        container = fobna(container)
        if container is None:
            raise ActionError("What ?")
        if not container.flags[14]:
            raise ActionError("That isn't a container")
        if container.flags[2] and container.state != 0:
            raise ActionError("It's closed!")
        text = "The {} contains:\n".format(container)
        aobjsat(container, 3)
        return text

    word = next(parser)
    if word is None:
        return __look()
    elif word == "at":
        return __look_at()
    elif word in ("in", "into"):
        return __look_in(next(parser))


__actions = {
  1: go,
  11: look,
}
"""
       case 1: 
          dogocom();
          break;
       case 139:
          if(in_fight) 
             {
             bprintf("Not in a fight!\n");break;
             }
          gropecom();
          break;
       case 8:
          if(isforce)
             {
             bprintf("You can't be forced to do that\n");
             break;
             }
          rte(globme);
          openworld();
          if(in_fight)
             {
             bprintf("Not in the middle of a fight!\n");
             break;
             }
          sprintf(xx,"%s has left the game\n",globme);
          bprintf("Ok");
          sendsys(globme,globme,-10000,curch,xx);
          sprintf(xx,"[ Quitting Game : %s ]\n",globme);
          sendsys(globme,globme,-10113,0,xx);
          dumpitems();
          setpstr(mynum,-1);
          pname(mynum)[0]=0;
          closeworld();
          curmode=0;curch=0;
          saveme();
          crapup("Goodbye");
          break;
       case 9:
          getobj();
          break;
       case 137:
          crashcom();
          break;
       case 10:
          dropitem();
          break;
       case 11:
          look_cmd();
          break;
       case 12:
          inventory();
          break;
       case 13:
          whocom();
          break;
       case 14:
          rescom();
          break;
       case 15:
          lightning();
          break;
       case 16:
          eatcom();
          break;
       case 17:
          playcom();
          break;
       case 18:
          shoutcom();
          break;
       case 19:
          saycom();
          break;
       case 20:
          tellcom();
          break;
       case 21:
          saveme();
          break;
       case 22:
          scorecom();
          break;
       case 23:
          exorcom();
          break;
       case 24:
          givecom();
          break;
       case 25:
          stealcom();
          break;
       case 26:
          levcom();
          break;
       case 27:
          helpcom();
          break;
       case 28:
          valuecom();
          break;
       case 29:
          stacom();
          break;
       case 30:
          examcom();
          break;
       case 31:
          delcom();
          break;
       case 32:
          passcom();
          break;
       case 33:
          sumcom();
          break;
       case 34:
          weapcom();
          break;
       case 35:
          killcom();
          break;
       case 50:
          laughcom();
          break;
       case 51:
          crycom();
          break;
       case 52:
          burpcom();
          break;
       case 53:
          fartcom();
          break;
       case 54:
          hiccupcom();
          break;
       case 55:
          grincom();
          break;
       case 56:
          smilecom();
          break;
       case 57:
          winkcom();
          break;
       case 58:
          sniggercom();
          break;
       case 59:
          posecom();
          break;
       case 60:
          setcom();
          break;
       case 61:
          praycom();
          break;
       case 62:
          stormcom();
          break;
       case 63:
          raincom();
          break;
       case 64:
          suncom();
          break;
       case 65:
          snowcom();
          break;
       case 66:
          goloccom();
          break;
       case 100:
          wearcom();
          break;
       case 101:
          removecom();
          break;
       case 102:
          putcom();
          break;
       case 103:
          wavecom();
          break;
       case 104:
          blizzardcom();
          break;
       case 105:
          opencom();
          break;
       case 106:
          closecom();
          break;
       case 107:
          lockcom();
          break;
       case 108:
          unlockcom();
          break;
       case 109:
          forcecom();
          break;
       case 110:
          lightcom();
          break;
       case 111:
          extinguishcom();
          break;
       case 118:
          cripplecom();
          break;
       case 119:
          curecom();
          break;
       case 120:
          dumbcom();
          break;
       case 121:
          changecom();
          break;
       case 122:
          missilecom();
          break;
       case 123:
          shockcom();
          break;
       case 124:
          fireballcom();
          break;
       case 126:
          blowcom();
          break;
       case 127:
          sighcom();
          break;
       case 128:
          kisscom();
          break;
       case 129:
          hugcom();
          break;
       case 130:
          slapcom();
          break;
       case 131:
          ticklecom();
          break;
       case 132:
          screamcom();
          break;
       case 133:
          bouncecom();
          break;
       case 134:
          wizcom();
          break;
       case 135:
          starecom();
          break;
       case 136:
          exits();
          break;
       case 138:
          singcom();
          break;
       case 140:
          spraycom();
          break;
       case 141:
          groancom();
          break;
       case 142:
          moancom();
          break;
       case 143:
          dircom();
          break;
       case 144:
          yawncom();
          break;
       case 117:;
       case 113:
          pushcom();
          break;
       case 145:
          wizlist();
          break;
       case 146:
          incom();
          break;
       case 147:
          lightcom();
          break;
       case 114:
          inviscom();
          break;
       case 115:
          viscom();
          break;
       case 148:
          deafcom();
          break;
       case 149:
          ressurcom();
          break;
       case 150:
          logcom();
          break;
       case 151:
          tsscom();
          break;
       case 152:
          rmeditcom();
          break;
       case 154:
          squeezecom();
          break;
       case 153:
          loccom();
          break;
       case 155:
          usercom();
          break;
       case 156:
          u_system();
          break;
       case 157:
          inumcom();
          break;
       case 158:
          updcom();
          break;
       case 159:
          becom();
          break;
       case 160:
          systat();
          break;
       case 161:
          convcom();
          break;
       case 162:
          snoopcom();
          break;
       case 163:
          shellcom();
          break;
       case 164:
          rawcom();
          break;
       case 165:
          purrcom();
          break;
       case 166:
          cuddlecom();
          break;
       case 167:
          sulkcom();
          break;
       case 168:
          rollcom();
          break;
       case 169:
          bprintf("\001f%s\001",CREDITS);
          break;
       case 170:
          brmode=!brmode;
          break;
       case 171:
          debugcom();
          break;
       case 172:
          jumpcom();
          break;
       case 112:
          wherecom();
          break;
       case 173:
          bprintf("Your adventurers automatic monster detecting radar, and long range\n");
          bprintf("mapping kit, is, sadly, out of order.\n");break;
       case 174:
          if(!in_fight)
             {
             dogocom();
             break;
             }
          else
             {
             char ar[120];
             if(iscarrby(32,mynum)) 
                {
                bprintf("The sword won't let you!!!!\n");
                break;
                }
             sprintf(ar,"\001c%s\001 drops everything in a frantic attempt to escape\n",globme);
             sendsys(globme,globme,-10000,curch,ar);
             sendsys(globme,globme,-20000,curch,"");
             my_sco-=my_sco/33; /* loose 3% */
             calibme();
             in_fight=0;
             on_flee_event();
             dogocom();
             break;
             }
       case 175:
          bugcom();
          break;
       case 176:
          typocom();
          break;
       case 177:
          pncom();
          break;
       case 178:
          blindcom();
          break;
       case 179:
          edit_world();
          break;
       case 180:
          if(ptstflg(mynum,4)) debug_mode=1-debug_mode;
          break;
       case 181:
          setpflags();
          break;
       case 182:
          frobnicate();
          break;
       case 183:
          setincom();
          break;
       case 184:
          setoutcom();
          break;
       case 185:
          setmincom();
          break;
       case 186:
          setmoutcom();
          break;
       case 187:
          emotecom();
          break;
       case 188:
          digcom();
          break;
       case 189:
          emptycom();
          break;
       default:
          if(my_lev>9999)bprintf("\n",n);
          else bprintf("\n");
          break;
"""


def execute_action(action_id):
    World.load()

    if 1 < action_id < 8:
        return go_direction(action_id)

    action = __actions.get(action_id)
    if action is not None:
        return action()

    if Globals.my_lev > 9999:
        raise ActionError("Sorry not written yet[COMREF %d]".format(action_id))
    else:
        raise ActionError("I don't know that verb.")


def aobjsat(*args):
    raise NotImplementedError()


def examcom():
    raise NotImplementedError()


def fobna(*args):
    raise NotImplementedError()
