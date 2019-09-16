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
      path: '/world/:worldId',
      component: () => import('@/views/World.vue'),
      children: [
        {
          path: '',
          name: 'world',
          component: () => import('@/views/wiki/World.vue'),
        },
        {
          path: 'wiki/:pageId',
          name: 'world-wiki',
          component: () => import('@/views/wiki/World.vue'),
        },
        {
          path: 'planet-:planetId',
          component: () => import('@/views/WorldPlanet.vue'),
          children: [
            {
              path: '',
              name: 'planet',
              component: () => import('@/views/WorldPlanetMain.vue'),
            },
            {
              path: 'wiki/:pageId',
              name: 'planet-wiki',
              component: () => import('@/views/wiki/Planet.vue'),
            },
            {
              path: 'map/:pageId?',
              name: 'planet-map',
              component: () => import('@/views/wiki/PlanetMap.vue'),
            },
          ],
        },
      ],
    },
    {
      path: '/wiki/:worldId/:wiki',
      name: 'wiki',
      component: () => import('@/views/World.vue'),
    },
    {
      path: '/generated/:thing?',
      name: 'Generated',
      component: () => import('@/views/Geneverse.vue'),
    },
    {
      path: '/walk',
      name: 'walk',
      component: () => import('@/views/Walk.vue'),
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
    {
      path: '/blog',
      component: () => import('@/views/blog/Blog.vue'),
      children: [
        {
          path: '',
          name: 'blog-home',
          component: () => import('@/views/blog/Home.vue'),
        },
        {
          path: 'login',
          name: 'blog-log-in',
          component: () => import('@/views/blog/Login.vue'),
        },
        {
          path: ':postId',
          name: 'blog-post',
          component: () => import('@/views/blog/Post.vue'),
        },
      ],
    },
  ],
});
