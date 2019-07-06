import data from './generators';

const realms = data.filter(item => item.generatorId === 'realm');

const getHostile = (item) => {
  if (item.itemId < 5) {
    return 0;
  }
  if (item.itemId < 10) {
    return 1;
  }
  if (item.itemId < 15) {
    return 2;
  }
  return 3;
};

export const getRandomItem = (groupId) => {
  const items = realms.filter(item => item.groupId === groupId);
  const itemId = Math.floor(Math.random() * items.length) + 1 || 1;
  const item = items.find(i => i.itemId === itemId);

  if (groupId === 4) {
    return {
      ...item,
      negative: item.itemId < 15,
    };
  }
  if (groupId === 5) {
    return {
      ...item,
      negative: item.itemId < 20,
    };
  }
  if (groupId === 7) {
    return {
      ...item,
      hostile: getHostile(item),
    };
  }
  if (groupId === 8) {
    return {
      ...item,
      hostile: getHostile(item),
    };
  }
  return item;
};

export const itemIds = [
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
  10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
  20, 21,
];
