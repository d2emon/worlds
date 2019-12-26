const loseme = () => null;
const crapup = text => console.error(text);
const openworld = () => Promise.resolve(null);
const cleanup = data => null;
const longwthr = () => null;
const secRead = (unit, offset, size) => Promise.resolve({
  unit,
  data: [0, 0, 0, 0],
});
const secWrite = (unit, data , offset, size) => Promise.resolve({
  unit,
  data,
});

export const send2 = block => openworld()
  .catch(() => {
    loseme();
    crapup('AberMUD: FILE_ACCESS : Access failed');
  })
  .then(unit => secRead(unit, 0, 64))
  .then(({ unit, data }) => {
    const number = 2 * data[1] - data[0];
    const eventsMeta = [
      data[0],
      data[1] + 1,
    ];
    return Promise.all([
      Promise.resolve(number),
      Promise.resolve(data),
      secWrite(unit, block, number, 128),
      secWrite(unit, eventsMeta, 0, 64),
    ]);
  })
  .then((data) => {
    if (data[0] >= 199) {
      cleanup(data[1]);
      longwthr();
    }
  });

const sendEvent = (receiver, sender, code, channel, text) => send2({
  channel,
  code,
  receiver,
  sender,
  text,
});

export const sendMessage = (sender, channel, text) => sendEvent(
  null,
  sender,
  -10000,
  channel,
  text,
);

export const sendWound = (receiver, sender, channel, damage, weapon) => sendEvent(
  receiver,
  sender,
  -10021,
  channel,
  {
    damage,
    weapon,
  },
);

export const sendWizardMessage = text => sendEvent(
  null,
  null,
  -10113,
  null,
  text,
);
