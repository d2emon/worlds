import {
  Api,
} from '@/helpers';

export default {
  getRoom: () => Api
    .get('/walk/look')
    .then(({ data }) => data.room),
};
