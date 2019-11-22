import blood from './blood';
import bprintf from './bprintf';

let state = {
  playerId: 0,
  name: '',
  level: 0,
  score: 0,
  channel: 0,

  toUpdate: false,

  ...blood,
  ...bprintf,
};

export const getState = () => state;

export const setState = newState => new Promise((resolve) => {
  state = {
    ...state,
    ...newState,
  };
  return resolve(state);
});
