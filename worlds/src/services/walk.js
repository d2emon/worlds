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
  getQuit: () => Api
    .get('/walk/quit')
    .then(({ data }) => data),
  getGoDirection: direction => Api
    .get(`/walk/go/${direction}`)
    .then(({ data }) => data),
  getExits: () => Api
    .get('/walk/exits')
    .then(({ data }) => data),
};
