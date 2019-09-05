<template>
  <v-layout justify-center>
    <v-flex xs12 sm9>
      <world-card
        v-if="world"
        :world="world"
      >
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
    WorldCard: () => import('@/components/cards/World.vue'),
  },
  computed: {
    ...mapState('worlds', [
      'world',
    ]),
  },
  methods: {
    ...mapActions('worlds', [
      'getWorld',
    ]),
    fetchAll() {
      const {
        worldId,
      } = this.$route.params;
      this.getWorld(worldId);
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
