import {
  getState,
  setState,
} from './state';
import {
  getPlayer,
  loadWorld, saveWorld, setPlayer,
} from './world';
import {
  dumpItems,
} from './objsys';
import {
  sendWizardMessage,
} from './events';

const sigAloff = () => null;
const saveme = () => null;
const chksnp = () => null;

export const loose = () => {
  sigAloff();
  setState({
    iSetup: false,
  })
    .then(loadWorld)
    .then(() => {
      dumpItems();
      const {
        playerId,
        name,
      } = getState();
      const player = getPlayer(playerId);
      if (player.visible < 10000) {
        sendWizardMessage(`${name} has departed from AberMUDII`);
      }
      return setPlayer({
        playerId,
        name: '',
      });
    })
    .then(saveWorld)
    .then(() => {
      const { zapped } = getState();
      if (!zapped) {
        saveme();
      }
      chksnp();
    });
};
