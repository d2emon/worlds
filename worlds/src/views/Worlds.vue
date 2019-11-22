<template>
  <v-layout justify-center>
    <v-flex xs12 xl9>
      <worlds-list :worlds="worlds" />
    </v-flex>
  </v-layout>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'Worlds',
  components: {
    WorldsList: () => import('@/components/Worlds.vue'),
  },
  computed: {
    ...mapState('worlds', [
      'worlds',
    ]),
  },
  methods: {
    ...mapActions('worlds', [
      'getWorlds',
    ]),
  },
  mounted() {
    this.getWorlds();
  },
};
</script>

<style scoped>

</style>
