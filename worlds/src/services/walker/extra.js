import {
  getState,
  setState,
} from './state';
import addMessage, {
  notDark,
  showFile,
  showMessages, visual,
} from './bprintf';
import {
  findItemAvailable,
  findPlayerVisible,
  isCarriedBy,
} from './objsys';
import {
  getItem,
  getPlayer, loadWorld,
  saveWorld,
  setItem,
  setPlayer,
} from './world';
import {
  randomPercent,
} from './magic';
import {error} from "./crapup";
import {sendMessage} from "./events";

const EXAMINES = 'EXAMINES';
const HELP1 = 'HELP1';
const HELP2 = 'HELP2';
const HELP3 = 'HELP3';
const LEVELS = 'LEVELS';
const WIZLIST = 'WIZLIST';
const sendsys = (playerTo, playerFrom, code, channel, message) => Promise.resolve();
const showname = location => '';
const fobn = item => null;
const ocreate = item => Promise.resolve();
const destroy = item => Promise.resolve();
const teletrap = location => null;
const trapch = location => null;
const fopen = (filename, permissions) => Promise.resolve();
const fclose = file => Promise.resolve();
const tscale = () => 0;

const onExamine = {
  7: (item) => {
    const state = randomPercent() % 3 + 1;
    return setItem(
      item.itemId,
      {
        state,
      },
    )
      .then(() => {
        if (state === 1) {
          return addMessage('It glows red');
        } else if (state === 2) {
          return addMessage('It glows blue');
        } else if (state === 3) {
          return addMessage('It glows green');
        }
      })
      .then(() => true);
  },
  8: (item, state) => {
    const connected = getItem(7);
    if (!connected || !connected.state) {
      return false;
    }
    const fromState = getItem(3 + connected.state);
    return (fromState && isCarriedBy(fromState, state.playerId) && fromState.bit[13])
      && addMessage('Everything shimmers and then solidifies into a different view!')
        .then(() => destroy(item.itemId))
        .then(() => teletrap(-1074))
        .then(() => true);
  },
  85: (item) => {
    const connected = getItem(83);
    return connected
      && connected.byte[0]
      && addMessage('Aha. under the bed you find a loaf and a rabbit pie')
        .then(() => Promise.all([
          ocreate(83),
          ocreate(84),
        ]))
        .then(() => {
          const item83 = getItem(83);
          item83.byte[0] = 1;
          return item83 && setItem(
            item.itemId,
          {
              byte: item83.byte,
            }
          );
        })
        .then(() => true);
  },
  91: (item, state) => {
    const connected = getItem(90);
    return connected
      && connected.byte[0]
      && addMessage('You pull an amulet from the bedding')
        .then(() => ocreate(connected.itemId))
        .then(() => {
          connected.byte[0] = 1;
          return setItem(
            item.itemId,
            {
              byte: connected.byte,
            }
          )
        })
        .then(() => true);
  },
  101: (item, state) => {
    if (item.byte[0] !== 0) {
      return false;
    }

    const connected = getItem(107);
    item.byte[0] = 1;
    connected.bit[0] = false;
    return addMessage('You take a key from one pocket')
      .then(() => setItem(
        item.itemId,
        {
          byte: item.byte,
        },
      ))
      .then(() => setItem(
        connected.itemId,
        {
          bit: connected.bit,
          location: state.playerId,
          carryFlag: 1,
        },
      ))
      .then(() => true);
  },
  144: (item, state) => {
    if (item.byte[0] !== 0) {
      return false;
    }

    const connected = getItem(145);
    item.byte[0] = 1;
    return addMessage('You take a scroll from the tube.')
      .then(() => setItem(
        item.itemId,
        {
          byte: item.byte,
        }
      ))
      .then(() => ocreate(connected.itemId))
      .then(() => setItem(
        connected.itemId,
        {
          location: state.playerId,
          carryFlag: 1,
        }
      ))
      .then(() => true);
  },
  145: (item, state) => setState({ location: -114 })
    .then(() => addMessage('As you read the scroll you are teleported!'))
    .then(() => destroy(item.itemId))
    .then(() => trapch(state.location))
    .then(() => true),
};

const statItem = item => new Promise(() => {
  const container = (item.carryFlag === 3)
    ? getItem(item.location)
    : (item.carryFlag !== 0)
      ? getPlayer(item.location)
      : null;
  return addMessage('')
    .then(() => addMessage(`Item        :${item.name}`))
    .then(() => (item.carryFlag === 3)
      ? `Contained in:${container && container.name}`
      :  (item.carryFlag !== 0)
        ? `Held By     :${container && container.name}`
        : `Position    :${showname(item.location)}`
    )
    .then(() => addMessage(`State       :${item.state}`))
    .then(() => addMessage(`Carr_Flag   :${item.carryFlag}`))
    .then(() => addMessage(`Spare       :${item.spare}`))
    .then(() => addMessage(`Max State   :${item.maxState}`))
    .then(() => addMessage(`Base Value  :${item.baseValue}`))
});

const statPlayer = player => new Promise(() => {
  if (!player) {
    throw new Error('Whats that?');
  }
  return Promise.resolve()
    .then(() => addMessage(`Name      : ${player.name}`))
    .then(() => addMessage(`Level     : ${player.level}`))
    .then(() => addMessage(`Strength  : ${player.strength}`))
    .then(() => addMessage(`Sex       : ${(player.sex === 0) ? 'MALE' : 'FEMALE'}`))
    .then(() => addMessage(`Location  : ${showname(player.location)}`));
});

const helpPlayer = async (target) => {
  const state = getState();
  const player = await findPlayerVisible(target);
  const me = await getPlayer(state.playerId);
  if (!player) {
    throw new Error('Help who?')
  }
  if (player.location !== state.location) {
    throw new Error('They are not here')
  }
  if (player.playerId === state.playerId) {
    throw new Error('You can\'t help yourself.')
  }

  const helped = await getPlayer(me.helping);
  if (helped) {
    await sendsys(
      player.name,
      player.name,
      -10011,
      state.channel,
      `${notDark(state.name)} has stopped helping you`,
    );
    await addMessage(`Stopped helping ${helped && helped.name}`);
  }
  await setPlayer(
    state.playerId,
    {
      helping: player.playerId,
    }
  );
  await sendsys(
    player.name,
    player.name,
    -10011,
    state.channel,
    `${notDark(state.name)} has offered to help you`,
  );
  await addMessage('OK...');
};

const help = () => saveWorld()
  .then(() => addMessage(showFile(HELP1)))
  .then(() => addMessage('\n'))
  .then(() => (getState().level > 9)
    && addMessage('Hit <Return> For More....')
      .then(showMessages)
      .then(() => addMessage(showFile(HELP2)))
      .then(() => addMessage('\n'))
  )
  .then(() => (getState().level > 9999)
    && addMessage('Hit <Return> For More....')
      .then(showMessages)
      .then(() => addMessage(showFile(HELP3)))
      .then(() => addMessage('\n'))
  );

export const helpcom = target => (
  target
    ? helpPlayer(target)
    : help()
)
  .catch(e => addMessage(e.message));

export const levcom = () => saveWorld()
  .then(() => addMessage(showFile(LEVELS)))
  .catch(e => addMessage(e.message));

export const valuecom = name => Promise.resolve()
  .then(() => {
    if (!name) {
      throw new Error('Value what?');
    }
    const item = findItemAvailable(name);
    if (!item) {
      throw new Error('There isn\'t one of those here.');
    }
    const value = (tscale() * item.baseValue) / 5;
    return addMessage(`${name} : ${value} points`)
  })
  .catch(e => addMessage(e.message));

const stacom = name => Promise.resolve(getState())
  .then((state) => {
    if (!name) {
      throw new Error('STATS what?')
    }
    if (state.level < 10) {
      throw new Error('Sorry, this is a wizard command buster...')
    }

    const item = fobn(name);
    return item
      ? statItem(item)
      : findPlayerVisible(name)
        .then(statPlayer);
  })
  .catch(e => addMessage(e.message));

const examcom = name => Promise.resolve()
  .then(() => {
    if (!name) {
      throw new Error('Examine what?')
    }

    const item = findItemAvailable(name);
    if (!item) {
      return addMessage('You see nothing special at all');
    }

    const event = onExamine[item.itemId];
    return event
      ? event(item, getState())
        .then(result => result ? null : item)
      : item;
  })
  .then((item) => {
    return item && fopen(`${EXAMINES}${item.itemId}`)
      .then((x) => {
        x.forEach(addMessage);
        return x;
      })
      .then(fclose)
      .catch(() => addMessage('You see nothing special.'));
  })
  .catch(e => addMessage(e.message));

export const wizlist = () => Promise.resolve(getState())
  .then((state) => {
    if (state.level < 10) {
      throw new Error('Huh?')
    }
    return saveWorld()
      .then(() => addMessage(showFile(WIZLIST)));
  })
  .catch(e => addMessage(e.message));

export const incom = (rn, rv, st) => Promise.resolve(getState())
  .then((state) => {
    if (state.level < 10) {
      throw new Error('Huh');
    }
    if (!rn) {
      throw new Error('In where?');
    }
    if (!rv) {
      throw new Error('In where?');
    }
    const exits = [...state.exDat];
    const channel = roomnum(rn, rv);
    if (!channel) {
      throw new Error('Where is that?');
    }
    return saveWorld()
      .then(() => loadWorld())
      .catch(() => throw new Error('No such room'))
      .then(unit => setState({ channel}).then(() => unit))
      .then((unit) => {
        lodex(unit);
        return fclose(unit);
      })
      .then(loadWorld)
      .then(() => gamecom(st))
      .then(loadWorld)
      .then(() => ({
        exits,
        channel,
      }))
  })
  .then(({ exits, channel }) => {
    const state = getState();
    return setState({
      channel,
      exDat: (channel === state.channel) ? exits : state.exDat,
    });
  })
  .catch(e => addMessage(e.message));

const jumtb = {
  '-643': -633,
  '-1050': -662,
  '-1082': -1053,
};

const jumpcom = () => Promise.resolve(getState())
  .then((state) => {
    const channel = jumtb[state.channel];
    if (!channel) {
      return addMessage('Wheeeeee....');
    }

    const item = getItem(1);
    if ((state.level < 10) && (!isCarriedBy(item, state.playerId) || !item.state)) {
      return setState({channel})
        .then(() => addMessage('Wheeeeeeeeeeeeeeeee  <<<<SPLAT>>>>'))
        .then(() => addMessage('You seem to be splattered all over the place'))
        .then(loseme)
        .then(() => error('I suppose you could be scraped up - with a spatula'));
    }
    return sendMessage(
      state.playerId,
      state.channel,
      visual(state.name, ' has just left'),
    )
      .then(() => setState({ channel }));
  })
  .then(state => sendMessage(
    state.playerId,
    state.channel,
    visual(state.name, ' has just dropped in'),
  ))
  .then(({ channel }) => trapch(channel))
  .catch(e => addMessage(e.message));

export const getLocated = (locationId, carryFlag) => {
  const state = getState();
  if ((state.level < 10) && !carryFlag && (locationId > -5)) {
    return 'Somewhere.....';
  }
  if (carryFlag === 3) {
    const location = getItem(locationId);
    return `In the ${location.name}`
  }
  if (carryFlag) {
    const location = getPlayer(locationId);
    return `Carried by ${notDark(location.name)}`;
  }
  return openroom(location, 'r')
    .then((unit) => {
      let message = unit[7];
      if (state.level > 9) {
        message += ` | ${showname(location)}`;
      }
      return fclose(unit).then(message);
    })
    .catch(() => 'Out in the void')
};

export const wherecom = (name) => Promise.resolve(getState())
  .then((state) => {
    if (state.level < 10) {
      throw new Error('You are too weak');
    }
    if (state.level < 10) {
      return setState({strength: state.strength - 2});
    }
    return state;
  })
  .then((state) => {
    if ([
      getItem(111),
      getItem(121),
      getItem(163),
    ].some(i => isCarriedBy(i, state.playerId))) {
      return 100
    }
    return 10 * state.level;
  })
  .then((chance) => saveWorld()
    .then(() => {
      const rnd = randomPercent();
      return rnd > chance;
    })
  )
  .then((fail) => {
    if (fail) {
      throw new Error('Your spell fails...');
    }
    if (!name) {
      throw new Error('What is that?');
    }
    const state = getState();
    let items = [];
    for (let itemId = 0; itemId < numobs; itemId += 1) {
      items.push(getItem(itemId));
    }
    return Promise.all(items.map((i) => {
      if (!i || i.name !== name) {
        return Promise.resolve(false);
      }
      let message = '';
      if (state.level > 9999) {
        message += `[${item.itemId}]`;
      }
      message += `${item.name} - `;
      message += ((state.level < 10) && !state.spare)
        ? 'Nowhere'
        : getLocated(item.location, item.carryFlag);
      return addMessage(message).then(() => true);
    }));
  })
  .then((found) => {
    const player = findPlayerVisible(name);
    let r = found.filter(v => v).length;
    if (!player) {
      return r;
    }
    r += 1;
    return addMessage(`${player.name} - ${getLocated(player.location)}`)
      .then(() => r);
  })
  .then(r => r || addMessage('I dont know what that is'))
  .catch(e => addMessage(e.message));

const checkNumber = (value, minValue=null, maxValue=null) => {
  if (!value) {
    throw new Error('Missing numeric argument');
  }
  if (((minValue !== null) && (value < minValue))
    || ((maxValue !== null) && (value > maxValue))) {
    throw new Error('Invalid range')
  }
};

const eItem = (itemId, valueId, value) => {
  checkNumber(itemId, 1, numobs);
  checkNumber(valueId, 0, 3);
  checkNumber(value);
  return setItem(
    itemId,
    {
      [valueId]: value,
    }
  );
};

const ePlayer = (playerId, valueId, value) => {
  checkNumber(playerId, 1, 47);
  checkNumber(valueId, 0, 15);
  checkNumber(value);
  return setPlayer(
    playerId,
    {
      [valueId]: value,
    }
  );
};

export const editWorld = (mode, itemId, valueId, value) => Promise.resolve(getState())
  .then((state) => {
    const me = getPlayer(state.playerId);
    if (!player || !player.bit[5]) {
      throw new Error('Must be Game Administrator');
    }
    if (mode === 'player') {
      return ePlayer(itemId, valueId, value);
    } else if (mode === 'object') {
      return eItem(itemId, valueId, value);
    } else {
      throw new Error('Must Specify Player or Object');
    }
  })
  .then(() => addMessage('Tis done'))
  .catch(e => addMessage(e.message));
