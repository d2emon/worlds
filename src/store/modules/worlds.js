import worldsService from '@/services/worlds';
import portalService from '@/services/portal';

const state = {
  worlds: [],
  portal: [],
};

const getters = {};

const mutations = {
  setWorlds: (state, worlds) => { state.worlds = worlds; },
  setPortal: (state, portal) => { state.portal = portal; },
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
  getPortal: ({ commit }) => portalService
    .getPortal()
    .then(portal => commit('setPortal', portal)),
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
