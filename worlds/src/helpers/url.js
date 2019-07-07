import config from './config';


export default {
  imageUrl: image => config.url + (image ? image : '/images/portal.jpg'),
  worldUrl: slug => (slug  ? `/world/${slug}` : '/'),
}
