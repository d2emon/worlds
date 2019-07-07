import { Api } from '@/helpers';


export default {
  getPortal: () => Api
    .get('/api/portal')
    .then(({ data }) => data.portal),
};
