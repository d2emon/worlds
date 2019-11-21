const Globals = {
  mynum: 0,
  myLev: 0,
  mySco: 0,
  globme: '',
  curch: 0,
};
const sendsys = (from_player, to_player, code, chanel, message) => null;
const oname = (itemId) => '';
const otstbit = (itemId, bitId) => false;
const obyte = (itemId, byteId) => 0;
const pname = (playerId) => '';
const pstr = (playerId) => 0;
const plev = (playerId) => 0;
const damof = (playerId) => 0;
const setpstr = (playerId, value) => null;
const brkword = () => null;
const bprintf = text => console.log(text);
const calibme = () => null;
const randperc = () => 50;
const iscarrby = (itemId, playerId) => false;
const iswornby = (itemId, playerId) => false;
const fobnc = (item) => null;
const woundmn = (playerId, damage) => null;
const __p = text => text;

export const Blood = {
  inFight: 0,
  fighting: null,
  wpnheld: null,
};

const damageByItem = (itemId) => {
  if (!itemId) return 4;
  if (!otstbit(itemId, 15)) return null;
  return obyte(itemId, 0);
};

export const weapcom = () => {
  const itemName = brkword();
  if (!itemName) return bprintf('Which weapon do you wish to select though');

  const itemId = fobnc(itemName);
  if (!itemId) return bprintf('Whats one of those?');

  const damage = damageByItem(itemId);
  if (!damage) {
    Blood.wpnheld = null;
    return bprintf('That\'s not a weapon');
  }

  Blood.wpnheld = itemId;
  calibme();
  bprintf('OK...');
};

export const hitplayer = (target, weapon) => {
  if (!pname(target)) return;

  if (weapon && !iscarrby(weapon, Globals.mynum)) {
    bprintf(`You belatedly realise you dont have the ${oname(weapon)},and are forced to use your hands instead..`);
    weapon = null;
  }

  Blood.wpnheld = weapon;

  if ((weapon === 32) && iscarrby(16, target)) {
    bprintf('The runesword flashes back away from its target, growling in anger!');
    return;
  }
  if (damageByItem(weapon) === null) {
    weapon = null;
    bprintf('That\'s no good as a weapon');
    return;
  }
  if (Blood.inFight) {
    bprintf('You are already fighting!');
    return;
  }

  Blood.fighting = target;
  Blood.inFight = 300;

  const res = randperc();
  let toHit = 40 + 3 * Globals.myLev;
  if ([89, 113, 114].some(itemId => iswornby(itemId, target))) {
    toHit -= 10;
  }
  if (toHit < 0) {
    toHit = 0;
  }

  if (res < toHit) {
    let message = `You hit ${__p(pname(target))}`;
    if (weapon) {
      message += ` with the ${oname(weapon)}`;
    }
    bprintf(message);
    const damage = randperc() % damageByItem(weapon);
    const x = {
      enemy: Globals.mynum,
      damage,
      weapon,
    };

    if (pstr(target) - damage < 0) {
      bprintf('Your last blow did the trick');

      if (pstr(target) >= 0) {
        Globals.mySco += (target < 16)
          ? (plev(target) * plev(target) * 100)
          : (10 * damof(target));
      }
      setpstr(target, -1);
      Blood.inFight = 0;
      Blood.fighting = null;
    }

    if (target < 16) {
      sendsys(pname(target), Globals.globme, -10021, Globals.curch, x);
    } else {
      woundmn(target, damage);
    }

    Globals.mySco += damage * 2;
    calibme();
  } else {
    bprintf(`You missed ${__p(pname(target))}`);
    const x = {
      enemy: Globals.mynum,
      damage: null,
      weapon,
    };
    if (target < 16) {
      sendsys(pname(target), Globals.globme, -10021, Globals.curch, x);
    } else {
      woundmn(target, 0);
    }
  }
};

export const killcom = () => {
  const target = brkword();
  if (!target) {
    return bprintf('Kill who');
  }
  if (target === 'door') {
    return bprintf('Who do you think you are, Moog?');
  }

  const itemId = fobna(target);
  if (itemId) {
    return breakItem(itemId);
  }

  const playerId = fpbn(target);
  if (!playerId) {
    return bprintf('You can\'t do that');
  }
  if (playerId === Globals.mynum) {
    return bprintf('Come on, it will look better tomorrow...');
  }
  if (ploc(playerId) !== Globals.curch) {
    return bprintf('They aren\'t here');
  }

  const xwisc = (weapon) => {
    if (!weapon) {
      return hitplayer(target, Blood.wpnheld);
    }

    if (weapon === 'with') {
      weapon = brkword();
      if (!weapon) {
        return bprintf('with what?');
      } else {
        return xwisc(weapon);
      }
    }

    const weaponId = fobnc(weapon);
    if (!weaponId) {
      return bprintf('with what?');
    }
    hitplayer(playerId, weaponId);
    return null;
  };

  xwisc(brkword());
};

export const bloodrcv = (data, isMe) => {
  if (!isMe) return;
  if (!data.enemy) return;

  if (!pname(data.enemy)) return;
  Blood.fighting = data.enemy;
  Blood.inFight = 300;
  if (!data.damage) {
    let message = `${__p(pname(data.enemy))} attacks you`;
    if (data.weapon) {
      message += ` with the ${oname(data.weapon)}`;
    }
    bprintf(message);
  } else {
    let message = `You are wounded by ${__p(pname(data.enemy))}`;
    if (data.weapon) {
      message += ` with the ${oname(data.weapon)}`;
    }
    bprintf(message);

    if (Globals.myLev < 10) {
      Globals.myStr -= data.damage;
      if (data.enemy === 16) {
        Globals.mySco -= 100 * data.damage;
        bprintf('You feel weaker, as the wraiths icy touch seems to drain your very life force');
        if (Globals.mySco < 0) {
          Globals.myStr = -1;
        }
      }
    }

    if (Globals.myStr < 0) {
      console.log(`${Globals.globme} slain by ${pname(data.enemy)}`);
      dumpitems();
      loseme();
      closeworld();

      delpers(Globals.globme);

      openworld();
      sendsys(Globals.globme, Globals.globme, -10000, Globals.curch, `${__p(Globals.globme)} has just died.`);
      sendsys(Globals.globme, Globals.globme, -10113, Globals.curch, `[ ${__p(Globals.globme)} has been slain by ${pname(data.enemy)} ]`);
      crapup('Oh dear... you seem to be slightly dead');
    }

    Globals.meCal = true;
  }
};

const breakItem = (itemId) => {
  if (itemId === 171) {
    return sysReset();
  }
  if (!itemId) {
    return bprintf('What is that?');
  }
  return bprintf('You can\'t do that');
};
