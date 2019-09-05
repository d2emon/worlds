<template>
  <v-container>
    <wiki
      v-if="wiki"
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
  name: 'Planet',
  components: {
    Wiki: () => import('@/components/Wiki.vue'),
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
        planetId,
        pageId,
      } = this.$route.params;
      this.getWiki({
        worldId,
        planetId,
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
