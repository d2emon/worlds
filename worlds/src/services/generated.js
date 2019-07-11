import { Api } from '@/helpers';

export default {
  getGenerated: slug => Api
    .get(`/api/generated/${slug}`)
    .then(({ data }) => data.thing),
};
