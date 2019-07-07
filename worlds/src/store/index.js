import Vue from 'vue';
import Vuex from 'vuex';
import modules from './modules';
import config from '@/helpers/config'

Vue.use(Vuex);

export default new Vuex.Store({
  modules,
  state: {
    config,
  },
  mutations: {},
  actions: {},
});
