import {
  imageUrl,
  worldUrl,
} from '@/helpers';
import worlds from './data/worlds';

export default {
  getWorlds: () => Promise
    .resolve(worlds)
    .then(items => items.map(({
      title,
      image,
      slug,
    }) => ({
      title,
      image: imageUrl(image),
      url: worldUrl(slug),
    }))),
  getWorld: world => Promise
    .resolve(worlds.find(item => item.slug === world))
    .then(({
      title,
      image,
      slug,
      text,
    }) => ({
      title,
      image: imageUrl(image),
      url: worldUrl(slug),
      text,
    })),
};
