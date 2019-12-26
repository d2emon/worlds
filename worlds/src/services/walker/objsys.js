import {
  getState,
} from './state';
import {getPlayer} from "./world";

const isdest = item => true;
const fobnsys = (name, mode, args) => null;
const seeplayer = player => false;
const dumpstuff = (player, channel) => null;

export const isCarriedBy = (item, player) => {
  const state = getState();
  if (!item) {
    return false;
  }
  if ((state.level < 10) && isdest(item.itemId)) {
    return false;
  }
  if ((item.carryFlag !== 1) && (item.carryFlag !== 2)) {
    return false;
  }
  if (item.location !== player) {
    return false;
  }
  return true;
};

export const findPlayer = (name) => {
  for (let playerId = 0; playerId < 48; playerId += 1) {
    const player = getPlayer(playerId);
    if (player.name) {
      const n1 = name.toLowerCase();
      const n2 = player.name.toLowerCase();

      if (n1 === n2) {
        return player;
      }
      if ((n2.substr(0, 4) === 'the')
        && (n1 === n2.substr(4))
      ) {
        return player;
      }
    }
  }
  return false;
};

export const findPlayerVisible = (name) => {
  const player = findPlayer(name);
  return Promise.resolve((player && seeplayer(player)) ? player : null);
};

export const findItemAvailable = name => fobnsys(name, 1, 0);

export const findItemOwned = name => fobnsys(name, 2, 0);

export const dumpItems = () => {
  const {
    playerId,
    channel,
  } = getState();
  dumpstuff(playerId, channel);
};
