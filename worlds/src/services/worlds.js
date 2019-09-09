import {
  Api,
  imageUrl,
  worldUrl,
  planetUrl,
} from '@/helpers';

const wikiLink = ({
  worldId,
  planetId,
  pageId,
  isMap,
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
    urlParts.push(`${isMap ? 'map' : 'page'}/${pageId}`);
  }
  return urlParts.join('/');
};

const filterFields = fields => data => ({
  ...Object.keys(data).reduce((result, field) => (
    (fields.indexOf(field) >= 0)
      ? {
        ...result,
        [field]: data[field],
      }
      : result
  ), {}),
});

const filterFieldsWithData = fields => data => ({
  ...Object.keys(data).reduce((result, field) => (
    (fields.indexOf(field) >= 0)
      ? {
        ...result,
        [field]: data[field],
      }
      : {
        ...result,
        data: {
          ...result.data,
          [field]: data[field],
        },
      }
  ), { data: {} }),
});

const normalizePages = (baseUrl, pages) => (pages || []).map(page => ({
  ...page,
  url: `${baseUrl}/${page.url}`,
}));

const world = {
  fields: [
    'author',
    'bookPages',
    'createdAt',
    'image',
    'isbn',
    'language',
    'origin',
    'media',
    'pages',
    'planets',
    'publisher',
    'series',
    'slug',
    'text',
    'title',
    'wiki',
  ],
  addUrl: () => ({
    slug,
    ...data
  }) => ({
    ...data,
    slug,
    url: worldUrl(slug),
  }),
};

const planet = {
  fields: [
    'about',
    'description',
    'map',
    'name',
    'slug',
  ],
  addUrl: worldId => ({
    slug,
    ...data
  }) => ({
    ...data,
    slug,
    url: planetUrl(worldId, slug),
  }),
};

export default {
  getWorlds: () => Api
    .get('/api/worlds')
    .then(({ data }) => data.worlds)
    .then(filterFields(world.fields))
    .then(world.addUrl())
    .then(items => items.map(({
      // title,
      image,
      // slug,
      ...data
    }) => ({
      ...data,
      // title,
      // slug,
      // image,
      image: image || imageUrl,
      // url: worldUrl(slug),
    }))),
  getWorld: worldId => Api
    .get(`/api/worlds/world/${worldId}`)
    .then(({ data }) => data.world)
    .then(filterFieldsWithData(world.fields))
    .then(world.addUrl())
    .then(({
      image,
      pages,
      url,
      ...data
    }) => ({
      ...data,
      image: image || imageUrl,
      pages: normalizePages(`${url}/wiki`, pages),
      url,
    })),
  getPlanet: (worldId, planetId) => Api
    .get(`/api/worlds/world/${worldId}/planet/${planetId}`)
    .then(({ data }) => data.planet)
    .then(filterFields(planet.fields))
    .then(planet.addUrl(worldId))
    .then(({
      about,
      map,
      url,
      ...data
    }) => ({
      ...data,
      about: normalizePages(`${url}/page`, about),
      map: map && {
        ...map,
        wiki: normalizePages(`${url}/map`, map.wiki),
      },
      url,
    })),
  getWiki: params => Api
    .get(wikiLink(params))
    .then(({ data }) => data.wiki),
};
