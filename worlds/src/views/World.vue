<template>
  <v-layout justify-center>
    <v-flex xs12 sm9>
      <world-card
        v-if="world"
        :world="world"
      >
        <!-- world-page
          :world="world"
          :wiki="wiki"
        / -->
        <router-view />
      </world-card>
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
    WorldCard: () => import('@/components/WorldCard.vue'),
    WorldPage: () => import('@/components/World.vue'),
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
        worldId,
        wiki,
      } = this.$route.params;
      this.getWorld(worldId);
      if (wiki) {
        this.getWiki({
          slug: worldId,
          filename: wiki,
        });
      }
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
