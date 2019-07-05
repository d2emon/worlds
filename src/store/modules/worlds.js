import worldsService from '@/services/worlds';

const state = {
  worlds: [],
};

const getters = {};

const mutations = {
  setWorlds: (state, worlds) => { state.worlds = worlds; },
};

const actions = {
  getWorlds: ({ commit }) => worldsService
    .getWorlds()
    .then(worlds => worlds.map(world => ({
      ...world,
      to: world.slug ? `/world/${world.slug}` : '/',
      image: world.image ? `/images/worlds/${world.image}` : '/images/portal.jpg',
    })))
    .then(worlds => commit('setWorlds', worlds)),
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
