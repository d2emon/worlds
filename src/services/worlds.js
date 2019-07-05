import worlds from './data/worlds';

export default {
  getWorlds: () => Promise.resolve(worlds),
};
