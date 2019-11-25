import addMessage, {
  visualName,
} from './bprintf';
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

const unarmedDamage = 4;
const onBreakItem = {
  171: () => sysReset(),
};
const onHitWithItem = {
  32: (target) => {
    if (isCarriedBy(getItem(16), target)) {
      throw new Error('The runesword flashes back away from its target, growling in anger!');
    }
    return true;
  },
};

const maxDamageByItem = (item) => {
  if (!item) return unarmedDamage;
  return item.isWeapon ? item.data[0] : null;
};

const breakItem = (item) => {
  if (!item) {
    addMessage('What is that?');
    return;
  }

  const event = onBreakItem[item.itemId];
  if (!event) {
    addMessage('You can\'t do that');
    return;
  }

  event();
};

const playerWounded = (player, weapon, damage) => {
  if (player.isBot) {
    return woundMonster(player, damage || 0);
  }

  const {
    playerId,
    channel,
  } = getState();
  return sendWound(
    player.playerId,
    playerId,
    channel,
    damage || null,
    weapon,
  );
};

const startFight = target => setState({
  fighting: target,
  inFight: 300,
});
const stopFight = () => setState({
  fighting: null,
  inFight: 0,
});

export const weapcom = (itemName) => {
  if (!itemName) {
    throw new Error('Which weapon do you wish to select though');
  }

  const item = findItemOwned(itemName);
  if (!item) {
    throw new Error('Whats one of those?');
  }

  const damage = maxDamageByItem(item);
  if (!damage) {
    return setState({ weapon: null })
      .then(() => throw new Error('That\'s not a weapon'));
  }

  return Promise.all([
    setState({ weapon: item.itemId }),
    updatePlayer(),
  ])
    .then(() => addMessage('OK...'));
};

export const hitPlayer = (target, weaponId) => {
  const player = getPlayer(target);
  if (!player.name) return Promise.resolve();

  let item = getItem(weaponId);
  const {
    playerId,
  } = getState();
  if (isCarriedBy(item, playerId)) {
    addMessage(
      `You belatedly realise you dont have the ${item.name},and are forced to use your hands instead..`,
    );
    item = null;
  }

  return setState({ weapon: item && item.itemId })
    .then((state) => {
      const event = item && onHitWithItem[item.itemId];
      if (event) {
        event();
      }

      if (maxDamageByItem(item) === null) {
        throw new Error('That\'s no good as a weapon');
      }
      if (state.inFight) {
        throw new Error('You are already fighting!');
      }

      return startFight(target);
    })
    .then((state) => {
      const ac = [89, 113, 114].some(armor => isWornBy(getItem(armor), target)) ? 10 : 0;
      const res = randomPercent();
      const toHit = 40 + 3 * state.level - ac;
      if (res < toHit) {
        const weaponMessage = item ? ` with the ${item.name}` : '';
        addMessage(`You hit ${visualName(player.name)} ${weaponMessage}`);
        const damage = randomPercent() % maxDamageByItem(item);

        const promises = [];
        if (player.strength < damage) {
          addMessage('Your last blow did the trick');

          promises.push(setState({
            score: (player.strength >= 0)
              ? state.score + player.value
              : state.score,
          }));
          promises.push(setPlayer({
            ...player,
            strength: -1,
          }));
          promises.push(stopFight());
        }
        promises.push(playerWounded(player, item.itemId, damage));
        return Promise.all(promises)
          .then(() => setState({ score: state.score + (damage * 2) }))
          .then(updatePlayer);
      }
      addMessage(`You missed ${visualName(player.name)}`);
      return playerWounded(player, item.itemId, 0);
    })
    .catch(e => addMessage(e.message));
};

export const killcom = (target, weaponName = null, ...args) => Promise.resolve()
  .then(() => {
    if (!target) {
      throw new Error('Kill who');
    }
    if (target === 'door') {
      throw new Error('Who do you think you are, Moog?');
    }

    const item = findItemAvailable(target);
    if (item) {
      return breakItem(item);
    }

    const player = findPlayerVisible(target);
    const state = getState();
    if (!player) {
      throw new Error('You can\'t do that');
    }
    if (player.playerId === state.playerId) {
      throw new Error('Come on, it will look better tomorrow...');
    }
    if (player.location !== state.channel) {
      throw new Error('They aren\'t here');
    }

    const xwisc = (selectWeapon) => {
      if (!selectWeapon) {
        return hitPlayer(player.playerId, state.weapon);
      }

      if (selectWeapon === 'with') {
        const itemName = args.length && args[0];
        if (!itemName) {
          throw new Error('with what?');
        }
        return xwisc(itemName);
      }

      const weapon = findItemAvailable(selectWeapon);
      if (!weapon) {
        throw new Error('with what?');
      }
      return hitPlayer(player.playerId, weapon.itemId);
    };

    return xwisc(weaponName);
  })
  .catch(e => addMessage(e.message));

export const bloodrcv = (data, enemyId, isMe) => {
  if (!isMe) return Promise.resolve();

  const enemy = getPlayer(enemyId);
  if (!enemy) return Promise.resolve();
  if (!enemy.name) return Promise.resolve();

  return setState({
    fighting: enemyId,
    inFight: 300,
  })
    .then((state) => {
      const item = getItem(data.weapon);
      const weaponMessage = item ? ` with the ${item.name}` : '';
      if (!data.damage) {
        throw new Error(`${visualName(enemy.name)} attacks you${weaponMessage}`);
      }

      addMessage(`You are wounded by ${visualName(enemy.name)}${weaponMessage}`);

      if (state.level < 10) {
        let {
          strength,
          score,
        } = state;
        strength -= data.damage;
        if (enemy.playerId === 16) {
          score -= 100 * data.damage;
          addMessage('You feel weaker, as the wraiths icy touch seems to drain your very life force');
          if (score < 0) {
            strength = -1;
          }
        }
        return setState({
          strength,
          score,
        });
      }
      return state;
    })
    .then((state) => {
      if (state.strength < 0) {
        console.log(`${state.name} slain by ${enemy.name}`);
        return Promise.resolve()
          .then(dumpItems)
          .then(loose)
          .then(saveWorld)
          .then(() => deleteUser(state.name))
          .then(loadWorld)
          .then(() => {
            sendMessage(state.playerId, state.channel, `${visualName(state.name)} has just died.`);
            sendWizardMessage(`[ ${visualName(state.name)} has been slain by ${enemy.name} ]`);
            return error('Oh dear... you seem to be slightly dead');
          });
      }
      return null;
    })
    .then(() => setState({ toUpdate: true }))
    .catch(e => addMessage(e.message));
};
