<template>
  <v-layout justify-center>
    <v-flex xs12 sm3>
      <v-container>
        <walk-controls />
      </v-container>
    </v-flex>
    <v-flex xs12 sm9>
      <v-container>
        <room />
      </v-container>
    </v-flex>
  </v-layout>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'Walk',
  components: {
    WalkControls: () => import('@/components/WalkControls.vue'),
    Room: () => import('@/components/Room.vue'),
  },
  methods: {
    ...mapActions('walk', [
      'getRoom',
    ]),
    fetchAll() {
      this.getRoom();
    },
  },
  watch: {
    $route() { this.fetchAll(); },
  },
  mounted() { this.fetchAll(); },
}
</script>

<style scoped>

</style>
