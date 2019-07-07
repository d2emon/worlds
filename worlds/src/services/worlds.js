import {
  Api,
  // imageUrl,
  worldUrl,
} from '@/helpers';

export default {
  getWorlds: () => Api
    .get('/api/worlds')
    .then(({ data }) => data.worlds)
    .then(items => items.map(({
      title,
      image,
      slug,
    }) => ({
      title,
      slug,
      image,
      // image: imageUrl(image),
      url: worldUrl(slug),
    }))),
  getWorld: world => Api
    .get(`/api/worlds/${world}`)
    .then(({ data }) => data.world)
    .then(({
      title,
      image,
      slug,
      text,
    }) => ({
      title,
      slug,
      image,
      // image: imageUrl(image),
      url: worldUrl(slug),
      text,
    })),
};
