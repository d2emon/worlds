import blood from './blood';

let state = {
  playerId: 0,
  name: '',
  level: 0,
  score: 0,
  channel: 0,

  toUpdate: false,

  ...blood,
};

export const getState = () => state;

export const setState = newState => new Promise((resolve) => {
  state = {
    ...state,
    ...newState,
  };
  return resolve(state);
});
