import axios from 'axios';
import config from './config';

const { url } = config;

export default Object.keys(url).reduce(
  (result, key) => ({
    ...result,
    [key]: axios.create({
      baseURL: url[key],
    }),
  }),
  {},
);
