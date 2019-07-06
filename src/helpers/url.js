export default {
  imageUrl: image => (image ? `/images/worlds/${image}` : '/images/portal.jpg'),
  worldUrl: slug => (slug  ? `/world/${slug}` : '/'),
}
