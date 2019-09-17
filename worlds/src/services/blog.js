import {
  Api,
} from '@/helpers';

const __posts = [
  {
    id: 1,
    slug: 'post-1',
    author: {
      firstName: 'First',
      lastName: 'Last',
    },
    title: 'Post 1',
    date: '01 May 2017',
    summary: 'Post 1',
    text: 'Post',
    image: 'https://image.ibb.co/bF9iO5/1.jpg',
  },
  {
    id: 2,
    slug: 'post-2',
    author: {
      firstName: 'First',
      lastName: 'Last',
    },
    title: 'Post 2',
    date: '01 May 2017',
    summary: 'Post 2',
    text: 'Post',
    image: 'https://image.ibb.co/bF9iO5/1.jpg',
  },
  {
    id: 3,
    slug: 'post-3',
    author: {
      firstName: 'First',
      lastName: 'Last',
    },
    title: 'Post 3',
    date: '01 May 2017',
    summary: 'Post 3',
    text: 'Post',
    image: 'https://image.ibb.co/bF9iO5/1.jpg',
  },
];

const briefFields = [
  'id',
  'slug',
  'author',
  'title',
  'date',
  'summary',
  'image',
];

const filterFields = fields => post => Object.keys(post).reduce(
  (result, field) => (fields.indexOf(field) >= 0
    ? {
      ...result,
      [field]: post[field],
    }
    : result),
  {},
);

const makeForm = (data) => {
  const form = new FormData();
  Object.keys(data).forEach(key => form.append(key, data[key]));
  return form;
};

export default {
  getIndex: () => Api.blog.get('/')
    .then(({ data }) => data),
  postLogin: values => Api.blog.post('/login', makeForm(values))
    .then(({ data }) => data),
  getPosts: () => Promise.resolve(__posts)
    .then(posts => posts.map(filterFields(briefFields))),
  getPost: postId => Promise.resolve(__posts.find(post => post.slug === postId))
    .then(data => ({
      data,
      meta: {
        previousPost: (__posts.indexOf(data) > 0)
          && filterFields(briefFields)(__posts[__posts.indexOf(data) - 1]),
        nextPost: (__posts.indexOf(data) < __posts.length - 1)
          && filterFields(briefFields)(__posts[__posts.indexOf(data) + 1]),
      },
    })),
};
