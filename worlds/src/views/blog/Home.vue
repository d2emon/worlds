<template>
  <div id="blog-home">
    <h2 v-if="user">Hello, {{ user.username }}!</h2>

    <v-container>
      <v-layout row wrap>
        <v-flex
          xs12
          v-for="post in posts"
          :key="`post--${post.id}`"
        >
          <v-container>
            <v-card>
              <v-card-text>
                {{post.author.username}} says: <strong>{{post.body}}</strong>
              </v-card-text>
            </v-card>
          </v-container>
        </v-flex>
      </v-layout>

      <transition-group
        class="layout row wrap blog__feed"
        name="preview"
      >
        <v-flex
          xs3
          v-for="post in oldPosts"
          :key="`post--${post.slug}`"
        >
          <v-container>
            <v-card>
              <router-link
                :to="`/blog/${post.slug}`"
              >
                <figure class="preview__figure">
                  <img
                    v-if="post.image"
                    :src="post.image"
                    width="100%"
                    alt=""
                  />
                  <img
                    v-else
                    src="http://via.placeholder.com/250x250"
                    width="100%"
                    alt=""
                  />

                  <transition name="fade">
                    <figcaption
                      class="preview__title"
                    >
                      {{ post.title }}
                    </figcaption>
                  </transition>
                </figure>
              </router-link>

              <transition name="fade">
                <v-container
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
                </v-container>
              </transition>
            </v-card>
          </v-container>
        </v-flex>
      </transition-group>
    </v-container>
  </div>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'BlogHome',
  computed: {
    ...mapState('blog', [
      'user',
      'posts',
      'oldPosts',
    ]),
  },
  methods: {
    ...mapActions('blog', ['fetchPosts']),
  },
  created() {
    this.fetchPosts({});
  },
};
</script>

<style scoped>
</style>
