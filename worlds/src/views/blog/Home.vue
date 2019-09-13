<template>
  <div id="blog-home">
    <h1>{{ pageTitle }}</h1>

    <v-container>
      <transition-group
        class="layout row wrap blog__feed"
        name="preview"
      >
        <v-flex
          xs3
          v-for="post in posts"
          :key="`post--${post.slug}`"
        >
          <v-container>
            <v-card :class="classes">
              <router-link
                :to="`/blog/${post.slug}`"
              >
                <figure class="preview__figure">
                  <img
                    v-if="post.image"
                    :src="post.image"
                    alt=""
                  />
                  <img
                    v-else
                    src="http://via.placeholder.com/250x250"
                    alt=""
                  />

                  <transition name="fade">
                    <figcaption
                      v-if="!reading"
                      class="preview__title"
                    >
                      {{ post.title }}
                    </figcaption>
                  </transition>
                </figure>
              </router-link>

              <transition name="fade">
                <aside
                  v-if="!reading"
                  class="preview__details"
                >
                  <h5 class="preview__meta">
                    <router-link
                      class="preview__author"
                      :to="`/by/${post.author}`"
                      @click.native="scrollTo(0)"
                    >
                      {{ post.author }}
                    </router-link>

                    <time
                      class="preview__published"
                    >
                      {{ post.date }}
                    </time>
                  </h5>

                  <article class="media">
                    <h2>{{ post.title }}</h2>
                    <p>{{ post.summary }}</p>
                  </article>
                </aside>
              </transition>
            </v-card>
          </v-container>
        </v-flex>
      </transition-group>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'BlogHome',
  data: () => ({
    pageTitle: 'Blog',
    posts: [],

    post: null,
  }),
  computed: {
    reading() {
      // return this.filters.post;
      return this.post;
    },
    classes() {
      return {
        preview: true,
        blog__post: true,
        'preview--reading': this.reading,
      };
    },
  },
  methods: {
    scrollTo() {},
    slugify(url) { return url; },

    getPosts() {
      this.posts = [
        {
          id: 1,
          slug: 'post-1',
          title: 'Post 1',
          date: '01 May 2017',
          summary: 'Post 1',
          description: 'Post',
          // image: 'https://image.ibb.co/bF9iO5/1.jpg',
          clipPath: 'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)',
        },
        {
          id: 2,
          slug: 'post-2',
          title: 'Post 2',
          date: 'date',
          summary: 'Post 2',
          description: 'Post',
          // image: 'https://image.ibb.co/dwDXGQ/2.jpg',
          clipPath: 'polygon(31% 23%, 90% 30%, 50% 100%, 0% 50%)',
        },
        {
          id: 3,
          slug: 'post-3',
          title: 'Post 3',
          date: 'date',
          summary: 'Post 3',
          description: 'Post',
          // image: 'https://image.ibb.co/bF9iO5/1.jpg',
          clipPath: 'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)',
        },
      ];
      // const filterBy = {
      //   post: (filter, { id }) => filter === id,
      //   author: (filter, { author }) => filter === this.slugify(author),
      // };
      // (Object.keys(this.filters).length)
      //   && this.posts.filter(post => Object.keys(this.filters)
      //     .every(filter => filterBy[filter](this.filters[filter], post)));
    },
  },
  created() {
    this.getPosts();
  },
};
</script>

<style scoped>
</style>
