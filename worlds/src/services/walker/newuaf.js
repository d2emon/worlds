const PCTL_FIND = 'PCTL_FIND';
const crapup = text => console.error(text);
const personactl = (name, mode) => Promise.resolve({
  unit: {},
  data: {
    userId: 1,
    name: 'Name',
  },
});
const writeData = (unit, itemId, data) => Promise.resolve({});
const disconnect = unit => Promise.resolve({});

export const deleteUser = name => personactl(name, PCTL_FIND)
  .then(({ unit, data }) => {
    if (name.toLowerCase() !== data.name.toLowerCase()) {
      crapup('Panic: Invalid Persona Delete');
    }
    return writeData(
      unit,
      data.userId,
      {
        ...data,
        name: '',
        level: -1,
      },
    );
  })
  .then(disconnect)
  .catch(() => {});
