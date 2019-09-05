import {
  Api,
  imageUrl,
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
      // image,
      image: image || imageUrl,
      url: worldUrl(slug),
    }))),
  getWorld: world => Api
    .get(`/api/worlds/world/${world}`)
    .then(({ data }) => data.world)
    .then(({
      title,
      image,
      slug,
      wiki,
      pages,
      text,
      planets,
      data,
    }) => ({
      title,
      slug,
      // image,
      image: image || imageUrl,
      url: worldUrl(slug),
      wiki,
      pages,
      text,
      planets,
      data,
    })),
  getWiki: (world, page) => Api
    .get(`/api/worlds/wiki/${world}/${page}`)
    .then(({ data }) => data.wiki),
};
