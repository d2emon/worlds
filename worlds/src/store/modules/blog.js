import blogService from '@/services/blog';
import {
  wiki2html,
} from '@/helpers';

export default {
  namespaced: true,
  state: {
    posts: [],
    post: null,
  },
  getters: {},
  mutations: {
    setPosts: (state, posts) => { state.posts = posts; },
    setPost: (state, post) => { state.post = post; },
  },
  actions: {
    fetchPosts: ({ commit }) => blogService
      .getPosts()
      .then(posts => commit('setPosts', posts)),
    fetchPost: ({ commit }, postId) => blogService
      .getPost(postId)
      .then(({ data, meta }) => ({
        data: {
          ...data,
          html: wiki2html(data.text),
        },
        meta,
      }))
      .then(post => commit('setPost', post)),
  },
};
