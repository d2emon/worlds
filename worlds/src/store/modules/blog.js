import blogService from '@/services/blog';
import {
  wiki2html,
} from '@/helpers';

export default {
  namespaced: true,
  state: {
    title: '',
    user: null,
    messages: [],
    errors: {},
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
    setMessages: (state, messages) => { state.messages = messages; },
    setErrors: (state, { form, errors }) => {
      state.errors = {
        ...state.errors,
        [form]: errors,
      };
    },
    setPosts: (state, posts) => { state.oldPosts = posts; },
    setPost: (state, post) => { state.post = post; },
  },
  actions: {
    fetchIndex: ({ commit }) => blogService
      .getIndex()
      .then(blog => commit('setBlog', blog)),
    doLogin: ({ commit }, form) => blogService
      .postLogin(form)
      .then(({ result, errors = [] }) => {
        commit('setMessages', result ? [result] : []);
        commit('setErrors', { form: 'login', errors });
        return !!result && errors.length <= 0;
      }),
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
