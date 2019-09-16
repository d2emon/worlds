import { Api } from '@/helpers';

export default {
  getCategories: () => Api.back
    .get('/api/categories')
    .then(({ data }) => data.categories),
};
