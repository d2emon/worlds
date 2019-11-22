import {
  getState,
} from './state';

const isdest = item => true;
const fobnsys = (name, mode, args) => null;
const fpbns = name => null;
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

export const findPlayerVisible = (name) => {
  const player = fpbns(name);
  return (player && seeplayer(player)) ? player : null;
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
