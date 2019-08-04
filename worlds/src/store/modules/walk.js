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
  exits: null,
};

const getters = {
  isDebugger: () => true, // this.ptstflg(this.mynum, 4)
};

const mutations = {
  setMessage: (state, { message, onMessage }) => {
    state.message = message;
    state.onMessage = onMessage;
  },
  setBrief: (state, brief) => { state.brief = brief; },
  setDebugMode: (state, debugMode) => { state.debugMode = debugMode; },
  setRoom: (state, room) => { state.room = room; },
  setExits: (state, exits) => { state.exits = exits; },
};

const actions = {
  getRoom: ({ commit, dispatch }) => walkService
    .getRoom()
    .then(({ room }) => room)
    .then(room => ({
      ...room,
      html: wiki2html(room.text),
    }))
    .then((room) => {
      if (room.not_brief) commit('setBrief', false);
      commit('setRoom', room);
    })
    .then(() => dispatch('fetchExits')),

  goDirection: ({ dispatch }, direction) => walkService
    .getGoDirection(direction)
    .then(response => dispatch('processResponse', response)),
  quitGame: ({ dispatch }) => walkService
    .getQuit()
    .then(({ error, ...response }) => dispatch('modalMessage', error || 'Ok')
      .then(() => dispatch('processResponse', response))),
  fetchExits: ({ commit }) => walkService
    .getExits()
    // .then(({ exits, ...data}) => { console.log(exits, data); return { exits }; })
    .then(({ exits }) => commit('setExits', exits)),

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

  modalMessage: ({ dispatch }, message) => new Promise(resolve => dispatch('showMessage', {
    message,
    onMessage: resolve,
  })),
  processResponse: ({ dispatch }, {
    crapup,
    error,
    ...response
  }) => Promise.resolve()
    /*
    .then(() => console.log({
      crapup,
      error,
      response,
    }))
     */
    .then(() => error && dispatch('modalMessage', error))
    .then(() => crapup && dispatch('modalMessage', `<hr /><div>${crapup}</div><hr />`))
    .then(() => dispatch('getRoom'))
    .then(() => response),
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
