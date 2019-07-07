import categoriesService from '@/services/categories';

const state = {
  categories: [],
};

const getters = {};

const mutations = {
  setCategories: (state, categories) => { state.categories = categories; },
};

const actions = {
  getCategories: ({ commit }) => categoriesService
    .getCategories()
    .then(categories => commit('setCategories', categories)),
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
