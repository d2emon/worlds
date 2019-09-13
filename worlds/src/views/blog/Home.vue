<template>
  <div id="blog-home">
    <h1>{{ pageTitle }}</h1>

    <div
      v-for="(post, index) in posts"
      :key="`${post.slug}_${index}`"
    >
      <router-link
        :to="`/blog/${post.slug}`"
      >
        <article class="media">
          <figure>
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
          </figure>
          <h2>{{ post.title }}</h2>
          <p>{{ post.summary }}</p>
        </article>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BlogHome',
  data: () => ({
    pageTitle: 'Blog',
    posts: [],
  }),
  methods: {
    getPosts() {
      this.posts = [
        {
          id: 1,
          slug: 'post-1',
          title: 'Post 1',
          date: '01 May 2017',
          summary: 'Post 1',
          description: 'Post',
          image: 'https://image.ibb.co/bF9iO5/1.jpg',
          clipPath: 'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)',
        },
        {
          id: 2,
          slug: 'post-2',
          title: 'Post 2',
          date: 'date',
          summary: 'Post 2',
          description: 'Post',
          image: 'https://image.ibb.co/dwDXGQ/2.jpg',
          clipPath: 'polygon(31% 23%, 90% 30%, 50% 100%, 0% 50%)',
        },
        {
          id: 3,
          slug: 'post-3',
          title: 'Post 3',
          date: 'date',
          summary: 'Post 3',
          description: 'Post',
          image: 'https://image.ibb.co/bF9iO5/1.jpg',
          clipPath: 'polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)',
        },
      ];
    },
  },
  created() {
    this.getPosts();
  },
};
</script>

<style scoped>
</style>
