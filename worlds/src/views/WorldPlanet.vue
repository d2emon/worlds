<template>
  <v-layout justify-center>
    <v-flex xs12 sm9>
      <planet
        :world="world"
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
  name: 'WorldPlanet',
  components: {
    Planet: () => import('@/components/Planet.vue'),
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
        slug,
      } = this.$route.params;
      this.getWorld(slug);
    },
  },
  watch: {
    $route() { this.fetchAll(); },
  },
  mounted() { this.fetchAll(); },
};
</script>
