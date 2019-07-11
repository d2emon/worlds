import generatedService from '@/services/generated';

const state = {
  generated: {},
};

const getters = {};

const mutations = {
  setGenerated: (state, generated) => { state.generated = generated; },
};

const actions = {
  getGenerated: ({ commit }, slug) => generatedService
    .getGenerated(slug)
    .then(generated => commit('setGenerated', generated)),
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
