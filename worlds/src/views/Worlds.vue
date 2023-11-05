<template>
  <v-layout justify-center>
    <v-flex xs12 xl9>
      <worlds-list :worlds="sorted" />
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
  data: () => ({
    sorted: [],
  }),
  methods: {
    ...mapActions('worlds', [
      'getWorlds',
    ]),
    sortWorlds(worlds, mode) {
      if (mode === 'title') {
        return worlds.sort((a, b) => {
          if (a.title > b.title) return 1;
          if (a.title < b.title) return -1;
          return 0;
        });
      }
      return worlds;
    },
  },
  watch: {
    worlds(value) {
      this.sorted = value ? this.sortWorlds([...value], 'title') : [];
    },
  },
  mounted() {
    this.getWorlds();
  },
};
</script>

<style scoped>

</style>
