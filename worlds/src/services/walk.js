import {
  Api,
} from '@/helpers';

export default {
  getRoom: () => Api
    .get('/walk/look')
    .then(({ data }) => data),
  getQuit: () => Api
    .get('/walk/quit')
    .then(({ data }) => data),
  getGoDirection: direction => Api
    .get(`/walk/go/${direction}`)
    .then(({ data }) => data),
};
