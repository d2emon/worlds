import walkService from '@/services/walk';
import {
  wiki2html,
} from '@/helpers';


const state = {
  progname: '   --}----- ABERMUD -----{--     Playing as Player',

  name: 'Player',

  message: '',
  onMessage: null,

  brief: false,
  debugMode: true, // false,

  convflg: 0,

  player: {
    is_wizard: true,
    is_god: true,

    visible: 0,
  },
  room: null,
  exits: null,
  inventory: [],
  characters: {},
  messages: [],
};

const getters = {
  isDebugger: () => true, // this.ptstflg(this.mynum, 4)
  prompt: (state) => {
    let prompt = '';
    if (state.convflg === 0) prompt = '>';
    else if (state.convflg === 1) prompt = '"';
    else if (state.convflg === 2) prompt = '*';
    else prompt = '?';

    if (state.debugMode) prompt = `#${prompt}`;
    if (state.player.is_wizard) prompt = `----${prompt}`;
    if (state.player.visible) prompt = `(${prompt})`;

    return prompt;
  },
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
  clearMessages: (state) => { /* state.messages = []; */ },
  setMessages: (state, messages) => { state.messages.push(...messages.map(wiki2html)); },
  setInventory: (state, inventory) => { state.inventory = inventory; },
  setCharacters: (state, characters) => { state.characters = characters; },
  updateProgname: (state) => {
    if (state.player.visible > 9999) {
      state.progname = '-csh';
    } else if (!state.player.visible) {
      state.progname = `   --}----- ABERMUD -----{--     Playing as ${state.name}`;
    }
  },
};

const actions = {
  showMessage: ({ commit }, payload) => commit('setMessage', payload),
  hideMessage: ({ commit, state }) => {
    const { onMessage } = state;
    commit('setMessage', {});
    return onMessage ? onMessage() : null;
  },

  inputCommand: ({ commit, dispatch, state }, command) => {
    const onInput = (raw) => {
      if (state.convflg && raw === '**') {
        // state.convflg = 0;
        return '';
      }
      if (!raw) return '';
      if (raw[0] === '*' && raw !== '*') return raw.substring(1);
      if (state.convflg === 1) return `say ${raw}`;
      if (state.convflg) return `tss ${raw}`;
      return raw;
    };
    const executeCommand = (toExecute) => {
      console.log(toExecute);
    };

    return dispatch('wait') // ???
      .then(() => dispatch('getMessages')) // Bottom
      .then(() => commit('updateProgname')) // Title
      .then(() => dispatch('getMessages')) // Top
      .then(() => command.substring(0, 80))
      .then(onInput)
      .then(executeCommand);
  },
  getMessages: ({}, response) => {
    console.log('self.get_text()', response);
    return Promise.resolve(response);
  },
  beforeAction: ({ dispatch }, response) => dispatch('getMessages', response),
  afterAction: ({ dispatch }, response) => dispatch('getMessages', response),
  doAction: ({ dispatch }, { callback, payload }) => dispatch('beforeAction', payload)
    .then(callback)
    .then(response => dispatch('afterAction', response))
    .then(response => dispatch('processResponse', response))
    .then((response) => {
      console.log(response.message, response);
      const { message } = response;
      if (response.message) dispatch('showMessage', { message });
      return response;
    }),

  restart: ({ dispatch, state }) => Promise.all([
    walkService.getStart(state.name),
    dispatch('modalMessage', 'Entering Game ....'),
  ])
    .then(([response]) => dispatch('processResponse', response))
    .then(response => dispatch('getRoom').then(() => response))
    .then(({ message }) => message && dispatch('modalMessage', message)),

  getRoom: ({ commit, dispatch }) => walkService
    .getRoom()
    .then(({ room, messages }) => {
      if (messages) commit('setMessages', messages);
      return room;
    })
    .then(room => ({
      ...room,
      html: wiki2html(room.text),
    }))
    .then((room) => {
      if (room.not_brief) commit('setBrief', false);
      commit('setRoom', room);
    })
    .then(() => {
      dispatch('fetchExits');
      dispatch('inventory');
      dispatch('who');
    }),

  wait: ({ dispatch }) => dispatch('doAction', {
    callback: walkService.getWait,
  })
    .then(() => dispatch('getMessages')),
  goDirection: ({ commit, dispatch }, direction) => dispatch('doAction', {
    callback: walkService.getGoDirection,
    payload: direction,
  })
    // .then((response) => {
    //   commit('clearMessages');
    //   dispatch('processResponse', response);
    // })
    .then(() => dispatch('getRoom')),
  quitGame: ({ dispatch }) => dispatch('doAction', {
    callback: walkService.getQuit,
  })
    // .then(({ error, ...response }) => dispatch('modalMessage', error || 'Ok').then(() => response))
    .then(() => dispatch('restart')),
  take: ({ commit, dispatch }, item) => dispatch('doAction', {
    callback: walkService.getTake,
    payload: item,
  })
    .then(() => dispatch('getRoom')),
  drop: ({ commit, dispatch }, item) => dispatch('doAction', {
    callback: walkService.getDrop,
    payload: item,
  })
    .then(() => dispatch('getRoom')),
  inventory: ({ commit }) => walkService
    .getInventory()
    .then(({ items }) => commit('setInventory', items)),
  who: ({ commit }) => walkService
    .getWho()
    .then(({ players, mobiles }) => commit('setCharacters', { players, mobiles })),
  jump: ({ dispatch }) => dispatch('doAction', {
    callback: walkService.getJump,
  })
    .then(({ message }) => message && dispatch('modalMessage', message))
    .then(() => dispatch('getRoom')),
  fetchExits: ({ commit, dispatch }) => dispatch('doAction', {
    callback: walkService.getExits,
  })
    // .then(({ exits, ...data}) => { console.log(exits, data); return { exits }; })
    .then(({ exits }) => commit('setExits', exits)),
  dig: ({ dispatch }) => dispatch('doAction', {
    callback: walkService.getDig,
  })
    .then(({ message }) => message && dispatch('modalMessage', message))
    .then(() => dispatch('getRoom')),

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
