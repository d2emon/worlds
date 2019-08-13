import {
  Api,
} from '@/helpers';

export default {
  getStart: name => Api
    .get(`/walk/start/${name}`)
    .then(({ data }) => data),
  getRoom: () => Api
    .get('/walk/look')
    .then(({ data }) => data),
  getWait: () => Api
    .get('/walk/wait')
    .then(({ data }) => data),
  getGoDirection: direction => Api
    .get(`/walk/go/${direction}`)
    .then(({ data }) => data),
  getQuit: () => Api
    .get('/walk/quit')
    .then(({ data }) => data),
  getTake: item => Api
    .get(`/walk/take/${item}`)
    .then(({ data }) => data),
  getInventory: () => Api
    .get('/walk/inventory')
    .then(({ data }) => data),
  getExits: () => Api
    .get('/walk/exits')
    .then(({ data }) => data),
  getJump: () => Api
    .get('/walk/jump')
    .then(({ data }) => data),
  getDig: () => Api
    .get('/walk/dig')
    .then(({ data }) => data),
};
