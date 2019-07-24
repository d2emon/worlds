import config from './config';


export default {
  mediaUrl: `${config.url}/files`,
  imageUrl: image => config.url + (image || '/images/portal.jpg'),
  worldUrl: slug => (slug  ? `/world/${slug}` : '/'),
}
