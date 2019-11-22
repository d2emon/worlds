import {
  getState,
  setState,
} from './state';
import {
  sendWound,
  sendMessage,
  sendWizardMessage,
} from './events';
import {
  getItem,
  getPlayer, loadWorld, saveWorld,
  setPlayer,
} from './world';
import {
  bprintf,
  _p,
} from './messages';
import {
  updatePlayer,
} from './parse';
import {
  randomPercent,
} from './magic';
import {
  dumpItems,
  findItemAvailable,
  findItemOwned,
  findPlayerVisible,
  isCarriedBy,
} from './objsys';
import {
  isWornBy,
  woundMonster,
} from './new1';
import {
  sysReset,
} from './mobile';
import {
  loose,
} from './player';
import {
  deleteUser,
} from './newuaf';
import {
  error,
} from './crapup';

const maxDamageByItem = (item) => {
  if (!item) return 4;
  return item.isWeapon ? item.data[0] : null;
};

const breakItem = (item) => {
  if (!item) {
    bprintf('What is that?');
    return;
  }
  if (item.itemId === 171) {
    sysReset();
    return;
  }
  bprintf('You can\'t do that');
};

const playerWounded = (player, weapon, damage) => {
  if (!player.isBot) {
    const state = getState();
    sendWound(
      player.playerId,
      state.playerId,
      state.channel,
      damage || null,
      weapon,
    );
  } else {
    woundMonster(player, damage || 0);
  }
};

export const weapcom = (itemName) => {
  if (!itemName) {
    bprintf('Which weapon do you wish to select though');
    return;
  }

  const item = findItemOwned(itemName);
  if (!item) {
    bprintf('Whats one of those?');
    return;
  }

  const damage = maxDamageByItem(item);
  if (!damage) {
    setState({ weapon: null });
    bprintf('That\'s not a weapon');
    return;
  }

  setState({ weapon: item.itemId });
  updatePlayer();
  bprintf('OK...');
};

export const hitplayer = (target, weapon) => {
  let itemId = weapon;
  let item = getItem(itemId);
  const player = getPlayer(target);
  const state = getState();
  if (!player.name) return;

  if (isCarriedBy(item, state.playerId)) {
    bprintf(`You belatedly realise you dont have the ${item.name},and are forced to use your hands instead..`);
    itemId = null;
    item = null;
  }

  setState({ weapon: item && item.itemId });

  if (item && (item.itemId === 32) && isCarriedBy(getItem(16), target)) {
    bprintf('The runesword flashes back away from its target, growling in anger!');
    return;
  }
  if (maxDamageByItem(item) === null) {
    bprintf('That\'s no good as a weapon');
    return;
  }
  if (state.inFight) {
    bprintf('You are already fighting!');
    return;
  }

  setState({
    fighting: target,
    inFight: 300,
  });

  const res = randomPercent();
  let toHit = 40 + 3 * getState().level;
  if ([89, 113, 114].some(armor => isWornBy(getItem(armor), target))) {
    toHit -= 10;
  }
  if (toHit < 0) {
    toHit = 0;
  }

  if (res < toHit) {
    let message = `You hit ${_p(player.name)}`;
    if (item) {
      message += ` with the ${item.name}`;
    }
    bprintf(message);
    const damage = randomPercent() % maxDamageByItem(item);

    if (player.strength - damage < 0) {
      bprintf('Your last blow did the trick');

      if (player.strength >= 0) {
        state.score += player.value;
      }
      setPlayer({
        ...player,
        strength: -1,
      });
      setState({
        fighting: null,
        inFight: 0,
      });
    }

    playerWounded(player, itemId, damage);

    setState({ score: state.score + (damage * 2) });
    updatePlayer();
  } else {
    bprintf(`You missed ${_p(player.name)}`);
    playerWounded(player, itemId, 0);
  }
};

export const killcom = (target, weaponName = null, ...args) => {
  if (!target) {
    bprintf('Kill who');
    return;
  }
  if (target === 'door') {
    bprintf('Who do you think you are, Moog?');
    return;
  }

  const item = findItemAvailable(target);
  if (item) {
    breakItem(item);
    return;
  }

  const player = findPlayerVisible(target);
  const state = getState();
  if (!player) {
    bprintf('You can\'t do that');
    return;
  }
  if (player.playerId === state.playerId) {
    bprintf('Come on, it will look better tomorrow...');
    return;
  }
  if (player.location !== state.channel) {
    bprintf('They aren\'t here');
    return;
  }

  const xwisc = (selectWeapon) => {
    if (!selectWeapon) {
      hitplayer(target, getState().weapon);
      return;
    }

    if (selectWeapon === 'with') {
      const itemName = args.length && args[0];
      if (!itemName) {
        bprintf('with what?');
        return;
      }
      xwisc(itemName);
    }

    const weapon = findItemAvailable(selectWeapon);
    if (!weapon) {
      bprintf('with what?');
      return;
    }
    hitplayer(player.playerId, weapon.itemId);
  };

  xwisc(weaponName);
};

export const bloodrcv = (data, enemyId, isMe) => {
  if (!isMe) return Promise.resolve();

  const enemy = getPlayer(enemyId);
  if (!enemy) return Promise.resolve();
  if (!enemy.name) return Promise.resolve();

  const item = getItem(data.weapon);

  const state = getState();

  setState({
    fighting: enemyId,
    inFight: 300,
  });

  if (!data.damage) {
    let message = `${_p(enemy.name)} attacks you`;
    if (item) {
      message += ` with the ${item.name}`;
    }
    bprintf(message);
    return Promise.resolve();
  }

  let message = `You are wounded by ${_p(enemy.name)}`;
  if (item) {
    message += ` with the ${item}`;
  }
  bprintf(message);

  if (state.level < 10) {
    let {
      strength,
      score,
    } = state;
    strength -= data.damage;
    if (enemyId === 16) {
      score -= 100 * data.damage;
      bprintf('You feel weaker, as the wraiths icy touch seems to drain your very life force');
      if (score < 0) {
        strength = -1;
      }
    }
    setState({
      strength,
      score,
    });
  }

  const result = Promise.resolve();
  if (state.strength < 0) {
    console.log(`${state.name} slain by ${enemy.name}`);
    dumpItems();
    result
      .then(loose)
      .then(saveWorld)
      .then(() => deleteUser(state.name))
      .then(loadWorld)
      .then(() => {
        sendMessage(state.playerId, state.channel, `${_p(state.name)} has just died.`);
        sendWizardMessage(`[ ${_p(state.name)} has been slain by ${enemy.name} ]`);
        return error('Oh dear... you seem to be slightly dead');
      });
  }
  return result
    .then(() => setState({ toUpdate: true }));
};
