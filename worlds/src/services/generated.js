import { Api } from '@/helpers';

export default {
  getGenerated: slug => Api.back
    .get(`/api/generated/${slug}`)
    .then(({ data }) => data.thing),
};
