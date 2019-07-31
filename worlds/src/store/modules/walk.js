import walkService from '@/services/walk';
import {
  wiki2html,
} from '@/helpers';

const state = {
  brief: false,
  player: {
    is_wizard: false,
    is_god: false,
  },
  room: null,
};

const getters = {};

const mutations = {
  setBrief: (state, brief) => { state.brief = brief },
  setRoom: (state, room) => { state.room = room; },
};

const actions = {
  getRoom: ({ commit }) => walkService
    .getRoom()
    .then(room => ({
      ...room,
      html: wiki2html(room.text),
    }))
    .then((room) => {
      if (room.not_brief) commit('setBrief', false);
      commit('setRoom', room);
    }),
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
