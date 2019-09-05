<template>
  <planet
    :world="world"
    :planet="planet"
  />
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'WorldPlanet',
  components: {
    Planet: () => import('@/components/Planet.vue'),
  },
  computed: {
    ...mapState('worlds', [
      'world',
      'planet',
    ]),
  },
  methods: {
    ...mapActions('worlds', [
      'getPlanet',
    ]),
    fetchAll() {
      const {
        worldId,
        planetId,
      } = this.$route.params;
      this.getPlanet({
        worldId,
        planetId,
      });
    },
  },
  watch: {
    $route() { this.fetchAll(); },
  },
  mounted() { this.fetchAll(); },
};
</script>
