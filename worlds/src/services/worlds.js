import {
  Api,
  imageUrl,
  worldUrl,
  planetUrl,
} from '@/helpers';

const wikiLink = ({
  worldId,
  planetId,
  pageId
}) => {
  const urlParts = [
    '/api/worlds/wiki',
  ];
  if (worldId) {
    urlParts.push(`world/${worldId}`);
  }
  if (planetId) {
    urlParts.push(`planet/${planetId}`);
  }
  if (pageId) {
    urlParts.push(`page/${pageId}`);
  }
  return urlParts.join('/');
};

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
  getPlanet: (worldId, planetId) => Api
    .get(`/api/worlds/world/${worldId}/planet/${planetId}`)
    .then(({ data }) => data.planet)
    .then(({
      name,
      slug,
      description,
      about,
    }) => ({
      name,
      url: planetUrl(worldId, slug),
      description,
      about,
    })),
  getWiki: ({
    worldId,
    planetId,
    pageId,
  }) => Api
    .get(wikiLink({
      worldId,
      planetId,
      pageId,
    }))
    .then(({ data }) => data.wiki),
};
