import {
  Api,
} from '@/helpers';

const action = command => args => Api.back
  .get(`/walk/${command}${args ? `/${args}` : ''}`)
  .then(({ data }) => data);

export default {
  getStart: action('start'),
  getRoom: action('look'),
  getWait: action('wait'),
  getGoDirection: action('go'),
  getQuit: action('quit'),
  getTake: action('take'),
  getDrop: action('drop'),
  getInventory: action('inventory'),
  getWho: action('who'),
  getExits: action('exits'),
  getJump: action('jump'),
  getDig: action('dig'),
};
