import {
  getState,
} from '../state';
import {getItem, getPlayer} from "../world";

const numobs = 0;
const items = () => {
  const result = [];
  for (let itemId = 0; itemId < numobs; itemId += 1) {
    result.push(getItem(itemId));
  }
  return result;
};

const ishere = item => false;

export const isDark = () => {
  const {
    channel,
    level,
  } = getState();

  const light = () => items().find((item) => {
    if ((item.itemId !== 32) && !item.flags[13]) {
      return false;
    }
    if (ishere(item)) {
      return true;
    }
    if ((item.carryFlag === 0) || (item.carryFlag === 3)) {
      return false;
    }
    const player = getPlayer(item.location);
    return player && (player.location === channel);
  });

  if (level > 9) {
    return false;
  }
  if ((channel === -1100) || (channel === -1101)) {
    return false;
  }
  if ((channel <= -1113) && (channel >= -1123)) {
    return light();
  }
  if ((channel < -399) || (channel > -300)) {
    return false;
  }
  return light();
};
