import { Api } from '@/helpers';


export default {
  getPortal: () => Api.back
    .get('/api/portal')
    .then(({ data }) => data.portal),
};
