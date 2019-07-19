import worldsService from '@/services/worlds';
import portalService from '@/services/portal';
import {
  markdown2html,
} from '@/helpers';

const state = {
  portal: [],
  worlds: [],
  world: null,
  wiki: '',
};

const getters = {};

const mutations = {
  setPortal: (state, portal) => { state.portal = portal; },
  setWorlds: (state, worlds) => { state.worlds = worlds; },
  setWorld: (state, world) => { state.world = world; },
  setWiki: (state, wiki) => { state.wiki = wiki; },
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
  getWiki: ({commit}, {slug, filename}) => worldsService
    .getWiki(slug, filename)
    .then(wiki => (wiki ? markdown2html(wiki) : undefined))
    .then(wiki => commit('setWiki', wiki)),
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
