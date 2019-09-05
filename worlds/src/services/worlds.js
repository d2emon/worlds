import {
  Api,
  imageUrl,
  worldUrl,
  planetUrl,
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
      pages: (pages || []).map(page => ({
        ...page,
        url: `${worldUrl(slug)}/wiki/${page.url}`,
      })),
      text,
      planets,
      data,
    })),
  getPlanet: (world, planet) => Api
    .get(`/api/worlds/world/${world}/planet/${planet}`)
    .then(({ data }) => data.planet)
    .then(({
      name,
      slug,
      description,
      about,
    }) => ({
      name,
      url: planetUrl(world, slug),
      description,
      about,
    })),
  getWiki: (world, page) => Api
    .get(`/api/worlds/wiki/${world}/${page}`)
    .then(({ data }) => data.wiki),
};
