<template>
  <div id="blog-post">
    <v-card
      v-if="post && post.data"
    >
      <v-card-title>
        <h1>{{ post.data.title }}</h1>
        <h4 v-if="post.data.author">
          {{ post.data.author.firstName }} {{ post.data.author.lastName }}
        </h4>
      </v-card-title>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          text
        >
          Edit
        </v-btn>
        <v-btn
          text
        >
          Delete
        </v-btn>
      </v-card-actions>
      <v-container>
        <v-card-text v-html="post.data.html"></v-card-text>
      </v-container>
      <v-card-actions
        v-if="post.meta"
      >
        <v-btn
          v-if="post.meta.previousPost"
          :to="`/blog/${post.meta.previousPost.slug}`"
        >
          {{ post.meta.previousPost.title }}
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn
          v-if="post.meta.nextPost"
          :to="`/blog/${post.meta.nextPost.slug}`"
        >
          {{ post.meta.nextPost.title }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'BlogPost',
  computed: {
    ...mapState('blog', ['post']),
  },
  methods: {
    ...mapActions('blog', ['fetchPost']),
  },
  created() {
    const { postId } = this.$route.params;
    this.fetchPost(postId);
  },
  watch: {
    $route() {
      const { postId } = this.$route.params;
      this.fetchPost(postId);
    },
  },
};
</script>

<style scoped>

</style>
