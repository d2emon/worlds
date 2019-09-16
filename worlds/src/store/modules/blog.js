import blogService from '@/services/blog';
import {
  wiki2html,
} from '@/helpers';

export default {
  namespaced: true,
  state: {
    title: '',
    user: null,
    posts: [],
    oldPosts: [],
    post: null,
  },
  getters: {},
  mutations: {
    setBlog: (state, {
      title,
      user,
      posts,
    }) => {
      state.title = title;
      state.user = user;
      state.posts = posts;
    },
    setPosts: (state, posts) => { state.oldPosts = posts; },
    setPost: (state, post) => { state.post = post; },
  },
  actions: {
    fetchIndex: ({ commit }) => blogService
      .getIndex()
      .then(blog => commit('setBlog', blog)),
    doLogin: ({}, form) => blogService
      .postLogin(form)
      .then(console.log),
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
