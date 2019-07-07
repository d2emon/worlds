import { Api } from '@/helpers';

export default {
  getCategories: () => Api
    .get('/api/categories')
    .then(({ data }) => data.categories),
};
