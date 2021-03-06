import {
  Api,
  defaultImage,
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
    'books',
    'createdAt',
    'image',
    'imageUrl',
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
    'magnet',
    'map',
    'name',
    'slug',
    'surface',
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

const loadWorld = ({ data }) => Promise.resolve(data.world)
  .then(filterFieldsWithData(world.fields))
  .then(world.addUrl())
  .then(({
    imageUrl,
    pages,
    url,
    ...args
  }) => ({
    ...args,
    editUrl: `${url}/edit`,
    imageUrl: imageUrl || defaultImage,
    pages: normalizePages(`${url}/wiki`, pages),
    url,
  }));

export default {
  getWorlds: () => Api.back
    .get('/api/worlds')
    .then(({ data }) => data.worlds)
    .then(items => items.map(filterFields(world.fields)))
    .then(items => items.map(world.addUrl()))
    .then(items => items.map(({
      // title,
      imageUrl,
      // slug,
      ...data
    }) => ({
      ...data,
      // title,
      // slug,
      // image,
      imageUrl: imageUrl || defaultImage,
      // url: worldUrl(slug),
    }))),
  getWorld: slug => Api.back
    .get(`/api/worlds/world/${slug}`)
    .then(loadWorld),
  putWorld: (slug, args) => Api.back
    .put(`/api/worlds/world/${slug}`, args)
    .then(loadWorld),
  getPlanet: (worldId, planetId) => Api.back
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
  getWiki: params => Api.back
    .get(wikiLink(params))
    .then(({ data }) => data.wiki),
};
