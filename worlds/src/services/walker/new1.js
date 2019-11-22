import {
  isCarriedBy,
} from './objsys';
import {
  getState,
  setState,
} from './state';
import {
  sendMessage,
  sendWizardMessage,
} from './events';

const mhitplayer = (monster, player) => null;
const dumpstuff = (monster, location) => null;

export const isWornBy = (item, player) => {
  return item
    && isCarriedBy(item, player)
    && (item.carryFlag === 2);
};

export const woundMonster = (monster, damage = 0) => {
  if (!monster) return;

  const state = getState();

  const strength = monster.strength - (damage || 0);
  setState({
    playerId: monster.playerId,
    strength,
  });

  if (strength >= 0) {
    mhitplayer(monster, state.playerId);
  } else {
    dumpstuff(monster, monster.location);
    sendMessage(null, monster.location, `${monster.name} has just died`);
    sendWizardMessage(`[ ${monster.name} has just died ]`);
    setState({
      playerId: monster.playerId,
      name: '',
    });
  }
};
