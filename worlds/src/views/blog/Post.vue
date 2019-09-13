<template>
  <div id="blog-post">
    <h1>{{ post.data.title }}</h1>
    <h4>{{ post.data.author.firstName }} {{ post.data.author.lastName }}</h4>
    <div v-html="post.data.body"></div>
    <router-link
      v-if="post.meta.previousPost"
      :to="`/blog/${post.meta.previousPost.slug}`"
      class="button"
    >
      {{ post.meta.previousPost.title }}
    </router-link>
    <router-link
      v-if="post.meta.nextPost"
      :to="`/blog/${post.meta.nextPost.slug}`"
      class="button"
    >
      {{ post.meta.nextPost.title }}
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'BlogPost',
  data: () => ({
    post: {},
  }),
  methods: {
    getPost() {
      const { slug } = this.$route.params;
      this.post = {
        slug,
        data: {
          title: 'Post 1',
          author: {
            firstName: 'First',
            lastName: 'Last',
          },
          body: 'Body',
        },
        meta: {
          previousPost: {},
          nextPost: {},
        },
      };
    },
  },
  created() {
    this.getPost();
  },
  watch: {
    $route() {
      this.getPost();
    },
  },
};
</script>

<style scoped>

</style>
