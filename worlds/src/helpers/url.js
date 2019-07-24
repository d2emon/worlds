import config from './config';


export default {
  mediaUrl: `${config.url}/files`,
  imageUrl: `${config.url}/images/portal.jpg`,
  worldUrl: slug => (slug  ? `/world/${slug}` : '/'),
}
