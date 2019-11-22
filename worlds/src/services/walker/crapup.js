import {
  setState,
} from './state';

const dashes = '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-';
const pbfr = () => null;
const keysetback = () => null;

export const error = (message) => {
  pbfr();
  setState({ prDue: false })
    .then(() => {
      keysetback();
      console.log(dashes);
      console.error(message);
      console.log(dashes);
      throw new Error(message);
    });
};
