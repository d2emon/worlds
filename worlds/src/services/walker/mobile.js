import addMessage from './bprintf';
import {
  getState,
  setState,
} from './state';

const RESET_N = 'RESET_N';
const tscale = () => 0;
const time = () => 0;
const rescom = () => null;
const openlock = (filename, mode) => Promise.resolve({});
const close = file => Promise.resolve(null);

export const sysReset = () => {
  if (tscale() !== 2) {
    addMessage('There are other people on.... So it wont work!');
    return Promise.resolve();
  }

  const doReset = () => {
    const { level } = getState();

    setState({ level: 10 });
    rescom();
    setState({ level });
  };

  return openlock(RESET_N, 'ruf')
    .catch(doReset)
    .then((fl) => {
      const data = fl[0];
      return close(fl).then(() => data);
    })
    .then((u) => {
      const t = time();
      if (t - 3600 < u < t) {
        addMessage('Sorry at least an hour must pass between resets');
        return;
      }
      doReset();
    });
};
