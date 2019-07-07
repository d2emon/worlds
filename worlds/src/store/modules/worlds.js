import worldsService from '@/services/worlds';
import portalService from '@/services/portal';
import {
  markdown2html,
} from '@/helpers';

const state = {
  portal: [],
  worlds: [],
  world: null,
};

const getters = {};

const mutations = {
  setPortal: (state, portal) => { state.portal = portal; },
  setWorlds: (state, worlds) => { state.worlds = worlds; },
  setWorld: (state, world) => { state.world = world; },
};

const actions = {
  getPortal: ({ commit }) => portalService
    .getPortal()
    .then(portal => markdown2html(portal))
    .then(portal => commit('setPortal', portal)),
  getWorlds: ({ commit }) => worldsService
    .getWorlds()
    .then(worlds => commit('setWorlds', worlds)),
  getWorld: ({ commit }, slug) => worldsService
    .getWorld(slug)
    .then(world => ({
      ...world,
      html: world.text ? markdown2html(world.text) : undefined,
    }))
    .then(world => commit('setWorld', world)),
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
