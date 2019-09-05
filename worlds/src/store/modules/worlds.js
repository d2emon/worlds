import worldsService from '@/services/worlds';
import portalService from '@/services/portal';
import {
  wiki2html,
} from '@/helpers';

const state = {
  portal: [],
  worlds: [],
  world: null,
  planet: null,
  wiki: '',
};

const getters = {};

const mutations = {
  setPlanet: (state, planet) => { state.planet = planet; },
  setPortal: (state, portal) => { state.portal = portal; },
  setWorlds: (state, worlds) => { state.worlds = worlds; },
  setWorld: (state, world) => { state.world = world; },
  setWiki: (state, wiki) => { state.wiki = wiki; },
};

const actions = {
  getPortal: ({ commit }) => portalService
    .getPortal()
    .then(wiki2html)
    .then(portal => commit('setPortal', portal)),
  getWorlds: ({ commit }) => worldsService
    .getWorlds()
    .then(worlds => commit('setWorlds', worlds)),
  getWorld: ({ commit }, worldId) => worldsService
    .getWorld(worldId)
    .then(world => ({
      ...world,
      html: wiki2html(world.text, worldId),
    }))
    .then(world => commit('setWorld', world)),
  getWiki: ({ commit }, { worldId, planetId, pageId }) => (pageId
    ? worldsService.getWiki({ worldId, planetId, pageId })
    : Promise.resolve(null)
  )
    .then(wiki => wiki2html(wiki, worldId))
    .then(wiki => commit('setWiki', wiki)),
  getPlanet: ({ commit }, { worldId, planetId }) => worldsService
    .getPlanet(worldId, planetId)
    .then(planet => ({
      ...planet,
      html: wiki2html(planet.description, worldId),
    }))
    .then(planet => commit('setPlanet', planet)),
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
