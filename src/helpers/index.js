import markdown from './markdown';

export const imageUrl = image => (
  image ? `/images/worlds/${image}` : '/images/portal.jpg'
);

export const worldUrl = slug => (
  slug  ? `/world/${slug}` : '/'
);

export const markdown2html = text => text && markdown(text);
