import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'worlds',
      component: () => import('@/views/Worlds.vue'),
    },
    {
      path: '/random-world',
      name: 'RandomWorld',
      component: () => import('@/views/RandomWorld.vue'),
    },
    {
      path: '/world/:slug',
      name: 'world',
      component: () => import('@/views/World.vue'),
    },
    {
      path: '/generated',
      name: 'Generated',
      component: () => import('@/views/Geneverse.vue'),
    },
    {
      path: '/hello',
      name: 'hello',
      component: () => import('@/views/Home.vue'),
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    },
    {
      path: '/categories',
      name: 'categories',
      component: () => import('@/views/Categories.vue'),
    },
  ],
});
