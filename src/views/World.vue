<template>
  <v-layout justify-center>
    <v-flex xs12 sm9>
      <world-card :world="world" />
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
    ]),
  },
  methods: {
    ...mapActions('worlds', [
      'getWorld',
    ]),
  },
  mounted() {
    const { slug } = this.$route.params;
    this.getWorld(slug);
  },
};
</script>

<style scoped>

</style>
