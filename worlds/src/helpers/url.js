import config from './config';

const worldUrl = worldId => (worldId ? `/world/${worldId}` : '/world/');

export default {
  mediaUrl: `${config.url}/files`,
  imageUrl: `${config.url}/images/portal.jpg`,
  worldUrl,
  wikiUrl: (worldId, url) => worldUrl(worldId) + (url ? `/planet-${url}` : '/'),
  planetUrl: (worldId, url) => worldUrl(worldId) + (url ? `/planet-${url}` : '/'),
};
