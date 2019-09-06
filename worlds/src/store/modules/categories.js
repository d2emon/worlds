import categoriesService from '@/services/categories';

export default {
  namespaced: true,
  state: {
    categories: [],
  },
  getters: {},
  mutations: {
    setCategories: (state, categories) => { state.categories = categories; },
  },
  actions: {
    getCategories: ({ commit }) => categoriesService
      .getCategories()
      .then(categories => commit('setCategories', categories)),
  },
};
