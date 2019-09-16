<template>
  <v-container>
    <h1 v-if="title">{{ title }} - Blog</h1>
    <h1 v-else>Welcome to Blog!</h1>

    <router-view />
  </v-container>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'Blog',
  computed: {
    ...mapState('blog', [
      'title',
    ]),
  },
  methods: {
    ...mapActions('blog', ['fetchIndex']),
  },
  created() {
    this.fetchIndex({});
  },
};
</script>

<style scoped>

</style>
