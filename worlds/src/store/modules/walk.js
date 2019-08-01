import walkService from '@/services/walk';
import {
  wiki2html,
} from '@/helpers';

const state = {
  message: '',
  onMessage: null,

  brief: false,
  debugMode: false,

  player: {
    is_wizard: true,
    is_god: true,
  },
  room: null,
};

const getters = {
  showingMessage: state => !!state.message,
  isDebugger: () => true, // this.ptstflg(this.mynum, 4)
};

const mutations = {
  setMessage: (state, { message, onMessage }) => {
    state.message = message;
    state.onMessage = onMessage;
  },
  setBrief: (state, brief) => { state.brief = brief; },
  setDebugMode: (state, brief) => { state.debugMode = debugMode; },
  setRoom: (state, room) => { state.room = room; },
};

const actions = {
  getRoom: ({ commit }) => walkService
    .getRoom()
    .then((data) => {
      console.log(data);
      return data;
    })
    .then(({ room }) => room)
    .then(room => ({
      ...room,
      html: wiki2html(room.text),
    }))
    .then((room) => {
      if (room.not_brief) commit('setBrief', false);
      commit('setRoom', room);
    }),
  goDirection: ({ dispatch }, direction) => walkService
    .getGoDirection(direction)
    .then((data) => {
      console.log(data);
      return data;
    })
    .then(({ error}) => dispatch('showMessage', {
      message: error,
      onMessage: () => dispatch('getRoom'),
    })),
  setDebugMode: ({ getters, commit }, debugMode) => {
    if (!getters.isDebugger) return;
    commit('setDebugMode', debugMode);
  },
  showMessage: ({ commit }, payload) => commit('setMessage', payload),
  hideMessage: ({ commit, state }) => {
    const { onMessage } = state;
    commit('setMessage', {});
    return onMessage ? onMessage() : null;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
