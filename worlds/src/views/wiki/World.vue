<template>
  <v-container>
    <world
      v-if="world"
      :world="world"
      :wiki="wiki"
    />
  </v-container>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'WorldWiki',
  components: {
    World: () => import('@/components/World.vue'),
  },
  computed: {
    ...mapState('worlds', [
      'world',
      'wiki',
    ]),
  },
  methods: {
    ...mapActions('worlds', [
      'getWiki',
    ]),
    fetchAll() {
      const {
        worldId,
        pageId,
      } = this.$route.params;
      this.getWiki({
        worldId,
        pageId,
      });
    },
  },
  watch: {
    $route() { this.fetchAll(); },
  },
  mounted() { this.fetchAll(); },
};
</script>

<style scoped>

</style>
