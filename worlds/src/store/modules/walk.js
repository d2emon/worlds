import walkService from '@/services/walk';
import {
  wiki2html,
} from '@/helpers';


const state = {
  name: 'Player',

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
  messages: [],
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
  clearMessages: state => { state.messages = []; },
  setMessages: (state, messages) => { state.messages.push(...messages); },
};

const actions = {
  showMessage: ({ commit }, payload) => commit('setMessage', payload),
  hideMessage: ({ commit, state }) => {
    const { onMessage } = state;
    commit('setMessage', {});
    return onMessage ? onMessage() : null;
  },

  getMessages: ({}, response) => {
    console.log('self.get_text()', response);
    return Promise.resolve(response);
  },
  beforeAction: ({ dispatch }) => dispatch('getMessages')
    .then(() => console.log('sendmsg(self)')),
  afterAction: ({ dispatch }, response) => {
    // if (state.rd_qd) {
    //   dispatch('readMessages');
    //   commit('setRdQd', False);
    // }
    // World.save()
    return dispatch('getMessages', response);
  },

  restart: ({ dispatch, state }) => Promise.all([
    walkService.getStart(state.name),
    dispatch('modalMessage', 'Entering Game ....'),
  ])
    .then(([response]) => dispatch('processResponse', response))
    .then(response => dispatch('getRoom').then(() => response))
    .then(({ message }) => message && dispatch('modalMessage', message)),

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

  wait: ({ dispatch }) => dispatch('beforeAction')
    .then(() => walkService.getWait())
    .then(response => dispatch('afterAction', response))
    .then(response => dispatch('processResponse', response))
    .then(() => dispatch('getRoom')),
  goDirection: ({ commit, dispatch }, direction) => dispatch('beforeAction')
    .then(() => walkService.getGoDirection(direction))
    .then(response => dispatch('afterAction', response))
    .then((response) => {
      commit('clearMessages');
      dispatch('processResponse', response);
    })
    .then(() => dispatch('getRoom')),
  jump: ({ dispatch }) => dispatch('beforeAction')
    .then(() => walkService.getJump())
    .then(response => dispatch('afterAction', response))
    .then(response => dispatch('processResponse', response))
    .then(({ message }) => message && dispatch('modalMessage', message))
    .then(() => dispatch('getRoom')),
  quitGame: ({ dispatch }) => dispatch('beforeAction')
    .then(() => walkService.getQuit())
    .then(response => dispatch('afterAction', response))
    .then(({ error, ...response }) => dispatch('modalMessage', error || 'Ok').then(() => response))
    .then(response => dispatch('processResponse', response))
    .then(() => dispatch('restart')),
  fetchExits: ({ commit, dispatch }) => dispatch('beforeAction')
    .then(() => walkService.getExits())
    .then(response => dispatch('afterAction', response))
    // .then(({ exits, ...data}) => { console.log(exits, data); return { exits }; })
    .then(response => dispatch('processResponse', response))
    .then(({ exits }) => commit('setExits', exits)),

  setDebugMode: ({ getters, commit }, debugMode) => {
    if (!getters.isDebugger) return;
    commit('setDebugMode', debugMode);
  },

  modalMessage: ({ dispatch }, message) => new Promise(resolve => dispatch('showMessage', {
    message,
    onMessage: resolve,
  })),
  processResponse: ({ commit, dispatch }, {
    crapup,
    error,
    messages,
    ...response
  }) => Promise.resolve()
    /*
    .then(() => console.log({
      crapup,
      error,
      messages,
      response,
    }))
     */
    .then(() => error && dispatch('modalMessage', error))
    .then(() => crapup && dispatch('modalMessage', `<hr /><div>${crapup}</div><hr />`))
    .then(() => messages && commit('setMessages', messages))
    .then(() => response),
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
