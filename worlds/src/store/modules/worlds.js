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
  getWorld: ({ commit }, slug) => worldsService
    .getWorld(slug)
    .then(world => ({
      ...world,
      html: wiki2html(world.text, world.slug),
    }))
    .then(world => commit('setWorld', world)),
  getWiki: ({ commit }, { slug, filename }) => (filename
    ? worldsService.getWiki(slug, filename)
    : Promise.resolve(null)
  )
    .then(wiki => wiki2html(wiki, slug))
    .then(wiki => commit('setWiki', wiki)),
  getPlanet: ({ commit }, { world, slug }) => worldsService
    .getPlanet(world, slug)
    .then(planet => ({
      ...planet,
      html: wiki2html(planet.description, world),
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
