<template>
  <v-layout justify-center>
    <v-flex xs12 sm9>
      <world-card
        :world="world"
        :wiki="wiki"
      />
    </v-flex>
  </v-layout>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'World',
  components: {
    WorldCard: () => import('@/components/World.vue'),
  },
  computed: {
    ...mapState('worlds', [
      'world',
      'wiki',
    ]),
  },
  methods: {
    ...mapActions('worlds', [
      'getWorld',
      'getWiki',
    ]),
    fetchAll() {
      const {
        slug,
        wiki,
      } = this.$route.params;
      this.getWiki({
        slug,
        filename: wiki,
      });
      this.getWorld(slug);
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
