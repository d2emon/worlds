import config from './config';

const { back } = config.url;
const worldUrl = worldId => (worldId ? `/world/${worldId}` : '/world/');

export default {
  mediaUrl: `${back}/files`,
  imageUrl: `${back}/images/portal.jpg`,
  worldUrl,
  wikiUrl: (worldId, url) => worldUrl(worldId) + (url ? `/planet-${url}` : '/'),
  planetUrl: (worldId, url) => worldUrl(worldId) + (url ? `/planet-${url}` : '/'),
};
