<template>
  <v-card light>
    <v-toolbar light>
      <v-toolbar-title v-if="title">{{ title }} - Blog</v-toolbar-title>
      <v-toolbar-title v-else>Blog</v-toolbar-title>

      <div class="flex-grow-1"></div>

      <v-toolbar-items>
        <v-btn
          text
          exact
          to="/blog/"
        >
          Home
        </v-btn>
        <v-btn
          text
          exact
          to="/blog/login"
        >
          Login
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <v-container v-if="messages && messages.length">
      <v-alert
        v-for="(message, messageId) in messages"
        :key="`message-${messageId}`"
        type="info"
      >
        {{message}}
      </v-alert>
    </v-container>

    <router-view />
  </v-card>
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
      'messages',
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
